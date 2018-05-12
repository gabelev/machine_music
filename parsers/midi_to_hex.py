import sys
from mido import MidiFile


def parse_single_midi_file(infile, outfile):
    for msg in MidiFile(infile):
        outfile.write(str(msg.hex()) + '\n')
    outfile.write("\n")

def parse_single_midi_file_with_time(infile, outfile):
    for msg in MidiFile(infile):
        if msg.time != 0:
            outfile.write(str(msg.hex()) + "," + str(msg.time) + '\n')
        else:
            outfile.write(str(msg.hex()) + '\n')
    outfile.write("\n")


if __name__ == "__main__":
    with open(sys.argv[2], 'w') as outfile:
        if sys.argv[3] == "time":
            parse_single_midi_file_with_time(sys.argv[1], outfile)
        else:
            parse_single_midi_file(sys.argv[1], outfile)
