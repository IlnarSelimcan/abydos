# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_aline.

This module contains unit tests for abydos.distance.ALINE
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import ALINE


class ALINETestCases(unittest.TestCase):
    """Test ALINE functions.

    abydos.distance.ALINE
    """

    cmp = ALINE()
    cmp_downey = ALINE(normalizer=lambda x: sum(x) / len(x))

    def test_aline_alignment(self):
        """Test abydos.distance.ALINE.alignment."""
        # test cases from Kondrak (2000)
        self.assertEqual(
            self.cmp.alignment('driy', 'tres'),
            [(75.0, '‖ d r iy ‖', '‖ t r e  ‖ s')],
        )
        self.assertEqual(
            self.cmp.alignment('blow', 'flare'),
            [(53.0, '‖ b l o ‖ w', '‖ f l a ‖ re')],
        )
        self.assertEqual(
            self.cmp.alignment('ful', 'plenus'),
            [(48.0, '‖ f u l ‖', '‖ p - l ‖ enus')],
        )
        self.assertEqual(
            self.cmp.alignment('fiz', 'piskis'),
            [(63.0, '‖ f i z ‖', '‖ p i s ‖ kis')],
        )
        self.assertEqual(
            self.cmp.alignment('ay', 'ego'), [(17.5, '‖ ay ‖', '‖ e  ‖ go')]
        )
        self.assertEqual(
            self.cmp.alignment('tuwz', 'dentis'),
            [(75.0, '‖ t uw z ‖', 'den ‖ t i  s ‖')],
        )

        # test cases from Kondrak (2002) after Covington (1996)
        # Some of these alignments are a little different from what's in the
        # thesis because of the differing encoding used.
        self.assertEqual(
            self.cmp.alignment('jo', 'zPe'), [(29.0, '‖ j  o ‖', '‖ zP e ‖')]
        )
        self.assertEqual(
            self.cmp.alignment('tu', 'tuF'), [(45.0, '‖ t u  ‖', '‖ t uF ‖')]
        )
        self.assertEqual(
            self.cmp.alignment('nostros', 'nu'),
            [(47.5, '‖ n o ‖ stros', '‖ n u ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('kyen', 'ki'),
            [(47.5, '‖ k ye ‖ n', '‖ k i  ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ke', 'kwa'), [(42.5, '‖ k e  ‖', '‖ k wa ‖')]
        )
        self.assertEqual(
            self.cmp.alignment('todos', 'tu'),
            [(47.5, '‖ t o ‖ dos', '‖ t u ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('una', 'uFn'),
            [(45.0, '‖ u  n ‖ a', '‖ uF n ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('dos', 'doF'),
            [(45.0, '‖ d o  ‖ s', '‖ d oF ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('tres', 'trwa'),
            [(77.5, '‖ t r e  ‖ s', '‖ t r wa ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ombre', 'om'),
            [
                (50.0, '‖ o m ‖ bre', '‖ o m ‖'),
                (50.0, '‖ o mb ‖ re', '‖ o m  ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('arbol', 'arbreC'),
            [(88.0, '‖ a r b o l ‖', '‖ a r b - r ‖ eC')],
        )
        self.assertEqual(
            self.cmp.alignment('pluFma', 'plum'),
            [(115.0, '‖ p l uF m ‖ a', '‖ p l u  m ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('kabetSa', 'kap'),
            [(75.0, '‖ k a b ‖ etSa', '‖ k a p ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('boka', 'busP'),
            [(68.5, '‖ b o k  ‖ a', '‖ b u sP ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('pye', 'pye'),
            [(65.0, '‖ p y e ‖', '‖ p y e ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('koratSon', 'koFr'),
            [(80.0, '‖ k o  r ‖ atSon', '‖ k oF r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ber', 'vwar'),
            [(60.5, '‖ b e  r ‖', '‖ v wa r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('benir', 'veCnir'),
            [(115.5, '‖ b e  n i r ‖', '‖ v eC n i r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('detSir', 'dir'),
            [
                (65.0, 'de ‖ tS i r ‖', '‖ d  i r ‖'),
                (65.0, '‖ d e tS i r ‖', '‖ d - -  i r ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('pobre', 'povreC'),
            [(115.5, '‖ p o b r e  ‖', '‖ p o v r eC ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('dSis', 'diHzes'),
            [(77.5, '‖ dS i s ‖', 'diH ‖ z  e s ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('dSaFt', 'das'),
            [(62.5, '‖ dS aF t ‖', '‖ d  a  s ‖')],
        )
        # Different from paper:
        # TODO: Implement 'double' and see if it changes
        self.assertEqual(
            self.cmp.alignment('wat', 'vas'),
            [(40.0, 'w ‖ a t ‖', 'v ‖ a s ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('nat', 'nixt'),
            [
                (62.5, '‖ n a - t ‖', '‖ n i x t ‖'),
                (62.5, '‖ n a t  ‖', '‖ n i xt ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('logN', 'lagN'),
            [(75.0, '‖ l o gN ‖', '‖ l a gN ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('maFn', 'man'),
            [(82.5, '‖ m aF n ‖', '‖ m a  n ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('flesP', 'flaysP'),
            [(122.5, '‖ f l e  sP ‖', '‖ f l ay sP ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('bleCd', 'bluHt'),
            [(99.0, '‖ b l eC d ‖', '‖ b l uH t ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('fedSeCr', 'feHdeCr'),
            [(124.0, '‖ f e  dS eC r ‖', '‖ f eH d  eC r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('haFr', 'haHr'),
            [(81.5, '‖ h aF r ‖', '‖ h aH r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ir', 'oHr'), [(41.5, '‖ i  r ‖', '‖ oH r ‖')]
        )
        self.assertEqual(
            self.cmp.alignment('ay', 'awgeC'),
            [(20.0, '‖ a y ‖', '‖ a w ‖ geC')],
        )
        self.assertEqual(
            self.cmp.alignment('nowz', 'naHzeC'),
            [(70.5, '‖ n ow z ‖', '‖ n aH z ‖ eC')],
        )
        self.assertEqual(
            self.cmp.alignment('mawtS', 'munt'),
            [(62.5, '‖ m aw - tS ‖', '‖ m u  n t  ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('teCgN', 'tsugNeC'),
            [(75.0, '‖ t  eC gN ‖', '‖ ts u  gN ‖ eC')],
        )
        self.assertEqual(
            self.cmp.alignment('fut', 'fuHs'),
            [(74.0, '‖ f u  t ‖', '‖ f uH s ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('niy', 'kniH'),
            [(53.0, '‖ n iy ‖', 'k ‖ n iH ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('haFnd', 'hant'),
            [(107.5, '‖ h aF n d ‖', '‖ h a  n t ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('hart', 'herts'),
            [
                (115.0, '‖ h a r t ‖', '‖ h e r t ‖ s'),
                (115.0, '‖ h a r t  ‖', '‖ h e r ts ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('liveCr', 'leHbeCr'),
            [(109.5, '‖ l i  v eC r ‖', '‖ l eH b eC r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('aFnd', 'ante'),
            [(72.5, '‖ aF n d ‖', '‖ a  n t ‖ e')],
        )
        self.assertEqual(
            self.cmp.alignment('aFt', 'ad'), [(37.5, '‖ aF t ‖', '‖ a  d ‖')]
        )
        self.assertEqual(
            self.cmp.alignment('blow', 'flaHre'),
            [(52.0, '‖ b l o  ‖ w', '‖ f l aH ‖ re')],
        )
        # Different from paper:
        self.assertEqual(
            self.cmp.alignment('ir', 'awris'),
            [(45.0, '‖ i r ‖', 'a ‖ w r ‖ is')],
        )
        self.assertEqual(
            self.cmp.alignment('iyt', 'edere'),
            [(40.0, '‖ iy t ‖', '‖ e  d ‖ ere')],
        )
        self.assertEqual(
            self.cmp.alignment('fisS', 'piskis'),
            [(73.0, '‖ f i sS ‖', '‖ p i s  ‖ kis')],
        )
        self.assertEqual(
            self.cmp.alignment('flow', 'fluere'),
            [(92.5, '‖ f l ow ‖', '‖ f l u  ‖ ere')],
        )
        self.assertEqual(
            self.cmp.alignment('star', 'steHlla'),
            [(92.0, '‖ s t a  r ‖', '‖ s t eH l ‖ la')],
        )
        self.assertEqual(
            self.cmp.alignment('ful', 'pleHnus'),
            [(48.0, '‖ f u l ‖', '‖ p - l ‖ eHnus')],
        )
        self.assertEqual(
            self.cmp.alignment('graFs', 'graHmen'),
            [(81.5, '‖ g r aF ‖ s', '‖ g r aH ‖ men')],
        )
        self.assertEqual(
            self.cmp.alignment('hart', 'kordis'),
            [(70.0, '‖ h a r t ‖', '‖ k o r d ‖ is')],
        )
        self.assertEqual(
            self.cmp.alignment('horn', 'kornuH'),
            [(90.0, '‖ h o r n ‖', '‖ k o r n ‖ uH')],
        )
        self.assertEqual(
            self.cmp.alignment('ay', 'ego'), [(17.5, '‖ ay ‖', '‖ e  ‖ go')]
        )
        self.assertEqual(
            self.cmp.alignment('niy', 'genuH'),
            [(44.0, '‖ n i  ‖ y', 'ge ‖ n uH ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('meCdSeCr', 'maHter'),
            [(109.0, '‖ m eC dS eC r ‖', '‖ m aH t  e  r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('mawnteCn', 'moHns'),
            [(105.5, '‖ m aw n t ‖ eCn', '‖ m oH n s ‖')],
        )
        # The example below is different from the expected, but
        # (73.0, '‖ n ey m ‖', '‖ n oH m ‖ en') is the #2 alignment.
        # This is probably due to slightly differing weights/costs/features.
        self.assertEqual(
            self.cmp.alignment('neym', 'noHmen'),
            [(80.5, '‖ n ey m ‖', 'noH ‖ m e  n ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('nyuw', 'nowus'),
            [(70.0, '‖ n yu w  ‖', '‖ n o  wu ‖ s')],
        )
        self.assertEqual(
            self.cmp.alignment('weCn', 'uHnus'),
            [(48.0, '‖ weC n ‖', '‖ uH  n ‖ us')],
        )
        self.assertEqual(
            self.cmp.alignment('rawnd', 'rotundus'),
            [(115.0, '‖ r a - w n d ‖', '‖ r o t u n d ‖ us')],
        )
        self.assertEqual(
            self.cmp.alignment('sow', 'suere'),
            [(57.5, '‖ s ow ‖', '‖ s u  ‖ ere')],
        )
        self.assertEqual(
            self.cmp.alignment('sit', 'seHdere'),
            [(66.5, '‖ s i  t ‖', '‖ s eH d ‖ ere')],
        )
        self.assertEqual(
            self.cmp.alignment('tSriy', 'treHs'),
            [(73.0, '‖ tS r iy ‖', '‖ t  r eH ‖ s')],
        )
        self.assertEqual(
            self.cmp.alignment('tuwtS', 'dentis'),
            [(85.0, '‖ t uw tS ‖', 'den ‖ t i  s  ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('tSin', 'tenuis'),
            [(67.5, '‖ tS i n ‖', '‖ t  e n ‖ uis')],
        )
        self.assertEqual(
            self.cmp.alignment('kiHnwaHwa', 'kenuaq'),
            [(105.5, '‖ k iH n w aH ‖ wa', '‖ k e  n u a  ‖ q')],
        )
        self.assertEqual(
            self.cmp.alignment('niHna', 'nenah'),
            [(91.5, '‖ n iH n a ‖', '‖ n e  n a ‖ h')],
        )
        self.assertEqual(
            self.cmp.alignment('naHpeHwa', 'naHpeHw'),
            [(115.0, '‖ n aH p eH w ‖ a', '‖ n aH p eH w ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('waHpimini', 'waHpemen'),
            [(150.0, '‖ w aH p i m i n ‖ i', '‖ w aH p e m e n ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('nameHsa', 'nameHqs'),
            [(125.0, '‖ n a m eH - s ‖ a', '‖ n a m eH q s ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('okimaHwa', 'okeHmaHw'),
            [(121.5, '‖ o k i  m aH w ‖ a', '‖ o k eH m aH w ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('sPiHsPiHpa', 'seHqsep'),
            [(97.0, '‖ sP iH - sP iH p ‖ a', '‖ s  eH q s  e  p ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ahkohkwa', 'ahkeHh'),
            [(124.0, '‖ a h k o  h ‖ kwa', '‖ a h k eH h ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('pemaHtesiweni', 'pemaHtesewen'),
            [
                (
                    257.5,
                    '‖ p e m aH t e s i w e n ‖ i',
                    '‖ p e m aH t e s e w e n ‖',
                )
            ],
        )
        self.assertEqual(
            self.cmp.alignment('asenya', 'aqsen'),
            [(90.0, '‖ a - s e n ‖ ya', '‖ a q s e n ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('didoHmi', 'doH'),
            [(50.0, 'di ‖ d oH ‖ mi', '‖ d oH ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('tAugateEr', 'toxteCr'),
            [(130.0, '‖ tA u g a t e  r ‖', '‖ t  o x - t eC r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('doteCr', 'tAugateEr'),
            [(112.5, '‖ d o t eC r ‖', 'tAu ‖ g a t e  r ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('ager', 'azPras'),
            [(61.0, '‖ a g  e r ‖', '‖ a zP - r ‖ as')],
        )
        self.assertEqual(
            self.cmp.alignment('bAaraHmi', 'pAero'),
            [(74.0, '‖ bA a r aH ‖ mi', '‖ pA e r o  ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('kentum', 'hekaton'),
            [
                (111.5, '‖ k e n t u m ‖', 'he ‖ k a - t o n ‖'),
                (111.5, '‖ k e nt u m ‖', 'he ‖ k a t  o n ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('kentum', 'sateCm'),
            [
                (90.0, '‖ k e n t u  m ‖', '‖ s a - t eC m ‖'),
                (90.0, '‖ k e nt u  m ‖', '‖ s a t  eC m ‖'),
            ],
        )

        # test cases from Downey, et al. (2008)
        self.assertEqual(
            self.cmp.alignment('api', 'api'),
            [(65.0, '‖ a p i ‖', '‖ a p i ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('apik', 'apik'),
            [(100.0, '‖ a p i k ‖', '‖ a p i k ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('apila', 'apila'),
            [(115.0, '‖ a p i l a ‖', '‖ a p i l a ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('api', 'apik'),
            [(65.0, '‖ a p i ‖', '‖ a p i ‖ k')],
        )
        self.assertEqual(
            self.cmp.alignment('api', 'apila'),
            [(65.0, '‖ a p i ‖', '‖ a p i ‖ la')],
        )
        self.assertEqual(
            self.cmp.alignment('apik', 'apila'),
            [(65.0, '‖ a p i ‖ k', '‖ a p i ‖ la')],
        )
        self.assertEqual(
            self.cmp.alignment('kalarita', 'kalarita'),
            [(200.0, '‖ k a l a r i t a ‖', '‖ k a l a r i t a ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('kalara', 'kalara'),
            [(150.0, '‖ k a l a r a ‖', '‖ k a l a r a ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('makebela', 'makebela'),
            [(200.0, '‖ m a k e b e l a ‖', '‖ m a k e b e l a ‖')],
        )
        # The following case has a different score, but the same alignment as
        # in Downey, et. al (2008)
        self.assertEqual(
            self.cmp.alignment('kalarita', 'kalara'),
            [(137.5, '‖ k a l a r i ‖ ta', '‖ k a l a r a ‖')],
        )
        self.assertEqual(
            self.cmp.alignment('kalarita', 'makebela'),
            [
                (75.0, '‖ k - - a l a ‖ rita', 'ma ‖ k e b e l a ‖'),
                (75.0, '‖ k a - - l a ‖ rita', 'ma ‖ k e b e l a ‖'),
            ],
        )
        self.assertEqual(
            self.cmp.alignment('kalara', 'makebela'),
            [(82.0, '‖ k a l a r a ‖', 'ma ‖ k e b e l a ‖')],
        )

        # other alignment styles:
        # TODO: verify that these are functioning correctly, since the don't match thesis
        cmp2 = ALINE(mode='local')
        self.assertEqual(
            cmp2.alignment('aHpakosiHs', 'waHpikonoHha'),
            [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')],
        )
        cmp2 = ALINE(mode='semi-global')
        self.assertEqual(
            cmp2.alignment('aHpakosiHs', 'waHpikonoHha'),
            [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')],
        )
        cmp2 = ALINE(mode='half-local')
        self.assertEqual(
            cmp2.alignment('aHpakosiHs', 'waHpikonoHha'),
            [(110.0, '‖ aH p a k o s iH s - ‖', 'w ‖ aH p i k o n oH h a ‖')],
        )
        cmp2 = ALINE(mode='global')
        self.assertEqual(
            cmp2.alignment('aHpakosiHs', 'waHpikonoHha'),
            [(106.5, '‖ aH  p a k o s iH s - ‖', '‖ waH p i k o n oH h a ‖')],
        )
        # The following just confirms that unknown values of mode use 'local'
        cmp2 = ALINE(mode='universal')
        self.assertEqual(
            cmp2.alignment('aHpakosiHs', 'waHpikonoHha'),
            [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')],
        )
        self.assertEqual(
            cmp2.alignment('kan', 'kaABCDHn'),
            [(84.0, '‖ k a      n ‖', '‖ k aABCDH n ‖')],
        )
        self.assertEqual(
            cmp2.alignment('kaABCDHn', 'kan'),
            [(84.0, '‖ k aABCDH n ‖', '‖ k a      n ‖')],
        )
        cmp2 = ALINE(phones='ipa')
        self.assertEqual(
            cmp2.alignment('kɒgneit', 'kognaːtus'),
            [(163.0, '‖ k ɒ g n ei t ‖', '‖ k o g n aː t ‖ us')],
        )

    def test_aline_sim(self):
        """Test abydos.distance.ALINE.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 1.0)
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.425)

        self.assertAlmostEqual(self.cmp.sim('nigel', 'niall'), 0.7037037037)
        self.assertAlmostEqual(self.cmp.sim('niall', 'nigel'), 0.7037037037)
        self.assertAlmostEqual(self.cmp.sim('colin', 'coiln'), 0.8333333333)
        self.assertAlmostEqual(self.cmp.sim('coiln', 'colin'), 0.8333333333)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT'.lower(), 'AACGATTAG'.lower()),
            0.685185185,
        )

        # test cases from Downey, et al. (2008)
        self.assertAlmostEqual(self.cmp_downey.sim('api', 'api'), 1.0)
        self.assertAlmostEqual(self.cmp_downey.sim('apik', 'apik'), 1.0)
        self.assertAlmostEqual(self.cmp_downey.sim('apila', 'apila'), 1.0)
        self.assertAlmostEqual(
            self.cmp_downey.sim('api', 'apik'), 0.7878787879
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('api', 'apila'), 0.7222222222
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('apik', 'apila'), 0.6046511628
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('kalarita', 'kalarita'), 1.0
        )
        self.assertAlmostEqual(self.cmp_downey.sim('kalara', 'kalara'), 1.0)
        self.assertAlmostEqual(
            self.cmp_downey.sim('makebela', 'makebela'), 1.0
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('kalarita', 'kalara'), 0.785714286
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('kalarita', 'makebela'), 0.375
        )
        self.assertAlmostEqual(
            self.cmp_downey.sim('kalara', 'makebela'), 0.468571429
        )

    def test_aline_sim_abs(self):
        """Test abydos.distance.ALINE.sim_abs."""
        # Base cases
        self.assertEqual(self.cmp.sim_abs('', ''), 1.0)
        self.assertEqual(self.cmp.sim_abs('a', ''), 0.0)
        self.assertEqual(self.cmp.sim_abs('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim_abs('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim_abs('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim_abs('abc', 'abc'), 85.0)
        self.assertEqual(self.cmp.sim_abs('abcd', 'efgh'), 51.0)

        self.assertAlmostEqual(self.cmp.sim_abs('nigel', 'niall'), 95.0)
        self.assertAlmostEqual(self.cmp.sim_abs('niall', 'nigel'), 95.0)
        self.assertAlmostEqual(self.cmp.sim_abs('colin', 'coiln'), 112.5)
        self.assertAlmostEqual(self.cmp.sim_abs('coiln', 'colin'), 112.5)
        self.assertAlmostEqual(
            self.cmp.sim_abs('ATCAACGAGT'.lower(), 'AACGATTAG'.lower()), 185.0
        )


if __name__ == '__main__':
    unittest.main()
