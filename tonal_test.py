import unittest
import tonal
import mingus.core.notes
from scales import SCALE_NAMES, TonalScale
import mingus.core.scales as scales


notes = mingus.core.notes
to = tonal.Tonal()
ts = TonalScale()


class TestTonal(unittest.TestCase):

    def test_scale_octave(self):
        self.assertEqual(12, to.add_octave(0, 1))

    def test_to_int(self):
        self.assertEqual(0, to.note_to_int("C"))
        self.assertEqual(11, notes.note_to_int("Cb"))
        with self.assertRaises(TypeError):
            to.note_to_int(0)

    def test_pick_scale(self):
        self.assertIsNotNone(to.pick_scale())
        self.assertIn(to.pick_scale(), SCALE_NAMES)

    def test_pick_base_note(self):
        self.assertIn(notes.note_to_int(to.pick_base_note()), range(0, 13))


class TestScales(unittest.TestCase):

    def test_select_scale(self):
        self.assertIsInstance(
            ts.select_scale("HarmonicMajor", "C"),
            scales.HarmonicMajor
        )
