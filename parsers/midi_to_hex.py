import sys
from mido import MidiFile


def parse_single_midi_file(infile, outfile):
    for msg in MidiFile(infile):
        outfile.write(str(msg.hex()) + '\n')
    outfile.write("\n")


if __name__ == "__main__":
    with open(sys.argv[2], 'w') as outfile:
        parse_single_midi_file(sys.argv[1], outfile)
