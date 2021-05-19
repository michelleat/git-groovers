class PercussionInstrument:
    def __init__(self, number_of_drums: int, electric: bool, name: str):
        self.number_of_strings = number_of_strings
        self.electric = electric
        self.name = name
        self.type = "string"

    def play_beat(self):
        print("playing the beat")
