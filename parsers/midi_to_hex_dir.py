import os
import sys
from mido import MidiFile


def parse_single_midi_file_with_time(infile, outfile):
    try:
        for msg in MidiFile(infile):
            if msg.time != 0:
                outfile.write(str(msg.hex()) + "," + str(msg.time) + '\n')
            else:
                outfile.write(str(msg.hex()) + '\n')
        outfile.write("\n")
    except IOError as e:
        print(e.message)
        pass



if __name__ == "__main__":
    num_files = 1
    with open(sys.argv[2], 'a+') as outfile:
        directory = sys.argv[1]
        for filename in os.listdir(directory):
            try:
                parse_single_midi_file_with_time(directory + "/" + filename, outfile)
                print(num_files)
                num_files += 1
            except Exception as e:
                print e.message
                continue
