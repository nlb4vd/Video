import argparse
import ffmpeg

def arg_parse():
    """
    Parse arguements to the detect module

    """


    parser = argparse.ArgumentParser(description='Crops and Stabilizes Videos')

    parser.add_argument("--video", dest = 'video', help =
                        "Video to compress",
                        default = "video.avi", type = str)
    parser.add_argument("--outvid", dest = 'outvid_name', help =
                        "Name of the output compressed video", default = "compressed.avi",
                        type = str)
    return parser.parse_args()

def compress(video, outvid_name):
    (
        ffmpeg
        .input(video)
        .output(outvid_name, crf=35 , vcodec='h264')
        .run()
    )
    
if __name__=="__main__":
    args = arg_parse()
    compress(args.video, args.outvid_name)
