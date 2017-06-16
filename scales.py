import mingus.core.scales as scales


SCALE_NAMES = ["Diatonic", "Ionian", "Dorian", "Phrygian", "Lydian",
               "Mixolydian", "Aeolian", "Locrian", "Major", "HarmonicMajor",
               "NaturalMinor", "HarmonicMinor", "MelodicMinor", "Bachian",
               "MinorNeapolitan", "Chromatic", "WholeTone", "Octatonic"]


class TonalScale(object):
    """
    Builds scales (integer arrays of notes that belong together) based on
    Notes in a given scale in Western music.
    """

    def __init__(self, scales=scales):
        self.scales = scales

    def select_scale(self, name, base_note):
        if not isinstance(base_note, str):
            return TypeError
        if name == "Diatonic":
            return self.scales.Diatonic(base_note, (0, 7))
        if name == "Ionian":
            return scales.Ionian(base_note)
        if name == "Dorian":
            return scales.Dorian(base_note)
        if name == "Phrygian":
            return scales.Phrygian(base_note)
        if name == "Lydian":
            return scales.Lydian(base_note)
        if name == "Mixolydian":
            return scales.Mixolydian(base_note)
        if name == "Aeolian":
            return scales.Aeolian(base_note)
        if name == "Locrian":
            return scales.Locrian(base_note)
        if name == "Major":
            return scales.Major(base_note)
        if name == "HarmonicMajor":
            return scales.HarmonicMajor(base_note)
        if name == "NaturalMinor":
            return scales.NaturalMinor(base_note)
        if name == "HarmonicMinor":
            return scales.HarmonicMinor(base_note)
        if name == "MelodicMinor":
            return scales.MelodicMinor(base_note)
        if name == "Bachian":
            return scales.Bachian(base_note)
        if name == "MinorNeapolitan":
            return scales.MinorNeapolitan(base_note)
        if name == "Chromatic":
            return scales.Chromatic(base_note)
        if name == "WholeTone":
            return scales.WholeTone(base_note)
        if name == "Octatonic":
            return scales.Octatonic(base_note)
