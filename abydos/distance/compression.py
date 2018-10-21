# -*- coding: utf-8 -*-

# Copyright 2014-2018 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.distance.compression.

The distance.compression module implements compression distance measures.
"""

from __future__ import division, unicode_literals

from codecs import encode
from sys import modules

from ..compression import arithmetic, rle

try:
    import lzma
except ImportError:  # pragma: no cover
    # If the system lacks the lzma library, that's fine, but lzma compression
    # similarity won't be supported.
    lzma = None

__all__ = ['dist_compression', 'sim_compression']


def dist_ncd_arith(src, tar, probs=None):
    """Return the NCD between two strings using arithmetic coding.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param dict probs: a dictionary trained with arithmetic.train (for the
        arith compressor only)
    :returns: compression distance
    :rtype: float
    """
    if src == tar:
        return 0.0

    src = src.encode('utf-8')
    tar = tar.encode('utf-8')

    if probs is None:
        # lacking a reasonable dictionary, train on the strings themselves
        probs = arithmetic.train(src + tar)
    src_comp = arithmetic.encode(src, probs)[1]
    tar_comp = arithmetic.encode(tar, probs)[1]
    concat_comp = arithmetic.encode(src + tar, probs)[1]
    concat_comp2 = arithmetic.encode(tar + src, probs)[1]

    return ((min(concat_comp, concat_comp2) - min(src_comp, tar_comp)) /
            max(src_comp, tar_comp))


def sim_ncd_arith(src, tar, probs=None):
    """Return the NCD similarity between two strings using arithmetic coding.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param dict probs: a dictionary trained with arithmetic.train (for the
        arith compressor only)
    :returns: compression distance
    :rtype: float
    """
    return 1-dist_ncd_arith(src, tar, probs)


def dist_ncd_rle(src, tar, use_bwt=False):
    """Return the NCD between two strings using RLE.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param bool use_bwt: boolean indicating whether to perform BWT encoding
        before RLE encoding
    :returns: compression distance
    :rtype: float
    """
    if src == tar:
        return 0.0

    src = src.encode('utf-8')
    tar = tar.encode('utf-8')

    src_comp = rle.encode(src, use_bwt)
    tar_comp = rle.encode(tar, use_bwt)
    concat_comp = rle.encode(src + tar, use_bwt)
    concat_comp2 = rle.encode(tar + src, use_bwt)

    return ((min(len(concat_comp), len(concat_comp2)) -
             min(len(src_comp), len(tar_comp))) /
            max(len(src_comp), len(tar_comp)))


def sim_ncd_rle(src, tar, use_bwt=False):
    """Return the NCD similarity between two strings using RLE.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param bool use_bwt: boolean indicating whether to perform BWT encoding
        before RLE encoding
    :returns: compression distance
    :rtype: float
    """
    return 1 - dist_ncd_rle(src, tar, use_bwt)


def dist_ncd_bwtrle(src, tar):
    """Return the NCD between two strings using BWT plus RLE.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :returns: compression distance
    :rtype: float
    """
    return dist_ncd_rle(src, tar, True)


def sim_ncd_bwtrle(src, tar):
    """Return the NCD similarity between two strings using BWT plus RLE.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :returns: compression distance
    :rtype: float
    """
    return 1 - dist_ncd_bwtrle(src, tar)


def dist_compression(src, tar, compressor='bz2', probs=None):
    """Return the normalized compression distance between two strings.

    Normalized compression distance (NCD) :cite:`Cilibrasi:2005`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param str compressor: a compression scheme to use for the similarity
        calculation, from the following:

            - `zlib` -- standard zlib/gzip
            - `bz2` -- bzip2 (default)
            - `lzma` -- Lempel–Ziv–Markov chain algorithm
            - `arith` -- arithmetic coding
            - `rle` -- run-length encoding
            - `bwtrle` -- Burrows-Wheeler transform followed by run-length
              encoding

    :param dict probs: a dictionary trained with arithmetic.train (for the
        arith compressor only)
    :returns: compression distance
    :rtype: float

    >>> dist_compression('cat', 'hat')
    0.08
    >>> dist_compression('Niall', 'Neil')
    0.037037037037037035
    >>> dist_compression('aluminum', 'Catalan')
    0.20689655172413793
    >>> dist_compression('ATCG', 'TAGC')
    0.037037037037037035

    >>> dist_compression('Niall', 'Neil', compressor='zlib')
    0.45454545454545453
    >>> dist_compression('Niall', 'Neil', compressor='bz2')
    0.037037037037037035
    >>> dist_compression('Niall', 'Neil', compressor='lzma')
    0.16
    >>> dist_compression('Niall', 'Neil', compressor='arith')
    0.6875
    >>> dist_compression('Niall', 'Neil', compressor='rle')
    1.0
    >>> dist_compression('Niall', 'Neil', compressor='bwtrle')
    0.8333333333333334
    """
    if src == tar:
        return 0.0

    if compressor == 'bz2':
        src_comp = encode(src, 'bz2_codec')[15:]
        tar_comp = encode(tar, 'bz2_codec')[15:]
        concat_comp = encode(src+tar, 'bz2_codec')[15:]
        concat_comp2 = encode(tar+src, 'bz2_codec')[15:]
    elif compressor == 'lzma':
        if 'lzma' in modules:
            src_comp = lzma.compress(src)[14:]
            tar_comp = lzma.compress(tar)[14:]
            concat_comp = lzma.compress(src+tar)[14:]
            concat_comp2 = lzma.compress(tar+src)[14:]
        else:
            raise ValueError('Install the PylibLZMA module in order to use ' +
                             'lzma compression similarity')
    else:  # zlib
        src_comp = encode(src, 'zlib_codec')[2:]
        tar_comp = encode(tar, 'zlib_codec')[2:]
        concat_comp = encode(src+tar, 'zlib_codec')[2:]
        concat_comp2 = encode(tar+src, 'zlib_codec')[2:]
    return ((min(len(concat_comp), len(concat_comp2)) -
             min(len(src_comp), len(tar_comp))) /
            max(len(src_comp), len(tar_comp)))


def sim_compression(src, tar, compressor='bz2', probs=None):
    """Return the normalized compression similarity of two strings.

    Normalized compression similarity is the complement of normalized
    compression distance:
    :math:`sim_{NCS} = 1 - dist_{NCD}`.

    :param str src: source string for comparison
    :param str tar: target string for comparison
    :param str compressor: a compression scheme to use for the similarity
        calculation:

            - `zlib` -- standard zlib/gzip
            - `bz2` -- bzip2 (default)
            - `lzma` -- Lempel–Ziv–Markov chain algorithm
            - `arith` -- arithmetic coding
            - `rle` -- run-length encoding
            - `bwtrle` -- Burrows-Wheeler transform followed by run-length
              encoding

    :param dict probs: a dictionary trained with arithmetic.train (for the
        arith compressor only)
    :returns: compression similarity
    :rtype: float

    >>> sim_compression('cat', 'hat')
    0.92
    >>> sim_compression('Niall', 'Neil')
    0.962962962962963
    >>> sim_compression('aluminum', 'Catalan')
    0.7931034482758621
    >>> sim_compression('ATCG', 'TAGC')
    0.962962962962963

    >>> sim_compression('Niall', 'Neil', compressor='zlib')
    0.5454545454545454
    >>> sim_compression('Niall', 'Neil', compressor='bz2')
    0.962962962962963
    >>> sim_compression('Niall', 'Neil', compressor='lzma')
    0.84
    >>> sim_compression('Niall', 'Neil', compressor='arith')
    0.3125
    >>> sim_compression('Niall', 'Neil', compressor='rle')
    0.0
    >>> sim_compression('Niall', 'Neil', compressor='bwtrle')
    0.16666666666666663
    """
    return 1 - dist_compression(src, tar, compressor, probs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
