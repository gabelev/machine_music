import random
import mingus.core.notes as notes

from scales import SCALE_NAMES, TonalScale


TS = TonalScale()

NOTES_MAP = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)

BASE_SCALE = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


class Tonal(object):
    """
    Tonal builds melodic scales and converts them into MIDI friendly integer arrays.
    """

    def __init__(self):
        return

    def note_to_int(self, note):
        """
        Converts a Letter note into a midi friendly int.

        :param note: whole tone note
        :return: integer corresponding to the note
        """
        if not isinstance(note, str) or len(note) != 1:
            raise TypeError
        else:
            return NOTES_MAP.get(note)

    def add_octave(self, note_int, scale):
        """
        Bump to the next octave!

        :param note_int: base note
        :param scale: scalar multiplier
        :return:
        """
        return note_int + scale * 12

    def pick_scale(self, scale=None):
        """
        Randomly picks a scale if not chosen
        TODO: weight the "normal" scales
        :param scale:
        :return:
        """
        if not scale:
            return SCALE_NAMES[random.randint(0, len(SCALE_NAMES) - 1)]
        else:
            return scale

    def pick_base_note(self):
        """
        Randomly chooses a starting point for the scale when needed.
        :return:
        """
        return notes.int_to_note(random.randint(0, 11))

    def create_scale_object(self, scale=None, base_note='C'):
        """
        Builds an array of integer notes that sit well together (aka a scale).

        :param scale:
        :param base_note:
        :return:
        """
        if not scale:
            return TS.select_scale(self.pick_scale())
        else:
            return TS.select_scale(scale, base_note)

    def create_midi_note_range(self, scale, base_note):
        """
        Builds a note range within a given scale and starting note.

        :param scale:
        :param base_note:
        :return:
        """
        beginning_scale = TS.select_scale(scale, base_note).ascending()
        begin_midi = [notes.note_to_int(note) for note in beginning_scale]
        midi_range = [note for note in begin_midi]
        for item in begin_midi:
            for x in range(16):
                new = self.add_octave(item, x)
                if new <= 120:
                    midi_range.append(new)
        return midi_range

    def create_sorted_midi(self, scale, base):
        """
        Results in an ascending melodic form.

        :param scale:
        :param base:
        :return:
        """
        midi = set(self.create_midi_note_range(scale, base))
        return sorted(midi)


def mapping(value, midi):
    if value >= 120:
        return mapping(value % 10, midi)
    if value < 0:
        return mapping(int(value * 10), midi)
    for item in midi:
        if item == value:
            return value
        if item > value:
            return item
