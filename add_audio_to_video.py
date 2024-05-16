import subprocess
import argparse

def add_audio_to_video(input_video_path, input_mp3_path, start_second, output_video_path):
    # ffmpeg 명령어를 subprocess를 통해 실행
    command = [
        'ffmpeg',
        '-i', input_video_path,          # 입력 비디오 파일
        '-itsoffset', str(start_second), # 오디오 시작 시간 오프셋
        '-i', input_mp3_path,            # 입력 오디오 파일
        '-map', '0:v',                   # 비디오 스트림을 첫 번째 입력 파일에서 사용
        '-map', '1:a',                   # 오디오 스트림을 두 번째 입력 파일에서 사용
        '-c:v', 'copy',                  # 비디오 코덱을 변경하지 않고 복사
        '-c:a', 'aac',                   # 오디오 코덱을 AAC로 설정
        '-strict', 'experimental',       # ffmpeg에서 AAC 코덱을 사용하는 경우 필요할 수 있음
        '-shortest',                     # 비디오 또는 오디오의 짧은 쪽에 맞춤
        output_video_path                # 출력 비디오 파일
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Audio added successfully: {output_video_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during audio addition: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add audio to a video from a specified start time')
    parser.add_argument('input_video_path', type=str, help='Path to the input video file')
    parser.add_argument('input_mp3_path', type=str, help='Path to the input MP3 file')
    parser.add_argument('start_second', type=int, help='Start time in seconds for the audio to begin in the video')
    parser.add_argument('output_video_path', type=str, help='Path to the output video file')
    
    args = parser.parse_args()
    
    add_audio_to_video(args.input_video_path, args.input_mp3_path, args.start_second, args.output_video_path)

