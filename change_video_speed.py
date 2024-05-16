import subprocess
import argparse

def change_video_speed(input_file, output_file, speed):
    # ffmpeg 명령어를 subprocess를 통해 실행
    command = [
        'ffmpeg',
        '-i', input_file,           # 입력 파일
        '-filter:v', f'setpts={1/speed}*PTS',  # 비디오 속도 변경
        '-filter:a', f'atempo={speed}',        # 오디오 속도 변경
        output_file                  # 출력 파일
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Video speed changed successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video speed change: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Change the speed of a video')
    parser.add_argument('input_file', type=str, help='Path to the input video file')
    parser.add_argument('output_file', type=str, help='Path to the output video file')
    parser.add_argument('speed', type=float, help='Speed factor (e.g., 2.0 for 2x speed, 0.5 for half speed)')
    
    args = parser.parse_args()
    
    change_video_speed(args.input_file, args.output_file, args.speed)

