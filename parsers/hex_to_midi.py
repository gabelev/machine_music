import sys
from mido import Message, MidiFile, MidiTrack


def convert_hex_file(infile, outfile):
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    for line in infile:
        try:
            track.append(Message.from_hex(line))
        except ValueError:
            # We don't want to stop when our ML algo makes nonsense
            continue

    # G-d save the queen
    midi_file.save(outfile)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        outfile = sys.argv[2]
        convert_hex_file(infile, outfile)
