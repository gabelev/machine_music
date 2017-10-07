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


def convert_hex_file_with_time(infile, outfile):
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)
    line_num = 0
    errors = 0

    for line in infile:
        line_num += 1
        try:
            hex_str = line.rstrip("\n").split(",")
            msg = (mido.Message.from_hex(hex_str[0]))
            if len(hex_str) > 1:
                msg.time = int(float(hex_str[1]) * 1000)
            track.append(msg)
        except ValueError:
            # We don't want to stop when our ML algo makes nonsense
            errors += 1
            # print e.message
            continue

    # G-d save the queen
    midi_file.save(outfile)

    print("Done!\nOut of {} messages, there were {} errors".format(line_num, errors))


def convert_hex_file_with_key(infile, outfile):
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)
    line_num = 0
    errors = 0

    for line in infile:
        line_num += 1
        try:
            hex_str = line.rstrip("\n").split(",")
            msg = (mido.Message.from_hex(hex_str[0]))
            if len(hex_str) == 3:
                msg.time = int(float(hex_str[2]) * 1000)
            track.append(msg)
        except Exception as e:
            # We don't want to stop when our ML algo makes nonsense
            errors += 1
            print(e)
            continue

    # G-d save the queen
    midi_file.save(outfile)

    print("Done!\nOut of {} messages, there were {} errors".format(line_num, errors))



if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        outfile = sys.argv[2]
        if sys.argv[3] == "time":
            convert_hex_file_with_time(infile, outfile)
        if sys.argv[3] == "key":
            convert_hex_file_with_key(infile, outfile)
        else:
            convert_hex_file(infile, outfile)

