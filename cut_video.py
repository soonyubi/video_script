import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_video_path, output_video_path, start_second, end_second):
    ffmpeg_extract_subclip(input_video_path, start_second, end_second, targetname=output_video_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut a video file to a specific time range.")
    parser.add_argument("input_video_path", type=str, help="Path to the input video file.")
    parser.add_argument("output_video_path", type=str, help="Path to the output video file.")
    parser.add_argument("start_second", type=int, help="Start time in seconds.")
    parser.add_argument("end_second", type=int, help="End time in seconds.")

    args = parser.parse_args()

    cut_video(args.input_video_path, args.output_video_path, args.start_second, args.end_second)

