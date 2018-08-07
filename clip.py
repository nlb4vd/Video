import os
import argparse

def arg_parse():
    """
    Parse arguements to the detect module

    """
    parser = argparse.ArgumentParser(description='Clips a video file')

    parser.add_argument("--input", dest = 'input', help=
                        "input video")
    parser.add_argument("--start", dest = 'start', help=
                        "start time in seconds")
    parser.add_argument("--end", dest='end', help=
                        "end time in seconds")
    parser.add_argument("--output", dest="output", help=
                        "output file")
    return parser.parse_args()

args = arg_parse()

def runBash(command):
    os.system(command)

def crop(input, start, end, output):
    cropped = "ffmpeg -ss " + start + " -i  " + input + " -t " + str(int(end)-int(start)-1) + " -c copy " + output
    runBash(cropped)

crop(args.input, args.start, args.end, args.output)
