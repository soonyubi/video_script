from moviepy.editor import VideoFileClip
import sys

def extract_audio(video_path, output_path):
    # 비디오 파일 불러오기
    video = VideoFileClip(video_path)
    # 비디오에서 오디오 추출
    audio = video.audio
    # 오디오 파일로 저장
    audio.write_audiofile(output_path)
    # 자원 해제
    audio.close()
    video.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python extract_audio.py [video_path] [output_audio_path]")
        sys.exit(1)

    _, video_path, output_audio_path = sys.argv
    extract_audio(video_path, output_audio_path)

