import argparse
import random
import time
import os

NOTES = [
    "A", 
    "Bb",
    "B", 
    "C",
    "C#",
    "D",
    "Eb",
    "E", 
    "F", 
    "F#",
    "G"
]

CHORD_TYPES = [
    "maj7", "min7", "7", "m7b5", "dim"
]

class ChordMaker(object):
    def __init__(self, time_interval=3, show_root_string=True, 
                 root_strings=None):
        self._last_chord = None
        self._show_root_string = show_root_string
        self.root_strings = root_strings or [6, 5]
        self.time_interval = time_interval

    def make_chord(self):
        chord = random.choice(NOTES) + random.choice(CHORD_TYPES)
        while chord == self._last_chord:
            chord = random.choice(NOTES) + random.choice(CHORD_TYPES)
        self._last_chord = chord
        return chord

    def print_chord(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.make_chord())
        if self._show_root_string is True:
            print("Root: {}".format(random.choice(self.root_strings)))
        time.sleep(self.time_interval)

    def main_loop(self):
        while True:
            try:
                self.print_chord()
            except KeyboardInterrupt:
                exit()


def go_through_chords(time_interval):
    chord_maker = ChordMaker()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", type=int, nargs="?", default=3,
                        help="Seconds to show chord")
    args = parser.parse_args()
    chord_maker = ChordMaker(args.interval)
    chord_maker.main_loop()

if __name__ == "__main__":
    main()
