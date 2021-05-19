from git_groovers import Chords


class StringInstrument:
    def __init__(self, number_of_strings: int, acoustic: bool, name: str):
        self.number_of_strings = number_of_strings
        self.acoustic = acoustic
        self.name = name
        self.type = "string"

    def play_chord(self, chord: Chords):
        print("playing the chord")
