import sys
import mido


def convert_hex_file(infile, outfile):
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)
    line_num = 0
    errors = 0

    for line in infile:
        line_num += 1
        try:
            msg = (mido.Message.from_hex(line.rstrip('\n')))
            msg.time = 64
            track.append(msg)
        except ValueError:
            # We don't want to stop when our ML algo makes nonsense
            errors += 1
            # print e.message
            continue

    # G-d save the queen
    midi_file.save(outfile)

    print("Done!\nOut of {} messages, there were {} errors".format(line_num, errors))


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        outfile = sys.argv[2]
        convert_hex_file(infile, outfile)
