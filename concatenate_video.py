# video_concat.py
import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(input_path, output_path, num_copies):
    clip = VideoFileClip(input_path)
    clips = [clip] * int(num_copies)  # 입력된 개수만큼 비디오 클립 복사
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, codec='libx264', fps=clip.fps)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python video_concat.py [input video path] [output video path] [number of copies]")
        sys.exit(1)
    
    input_video_path = sys.argv[1]
    output_video_path = sys.argv[2]
    num_copies = sys.argv[3]

    concatenate_videos(input_video_path, output_video_path, num_copies)

