import subprocess
import argparse

def convert_mkv_to_mp4(input_file, output_file):
    # ffmpeg 명령어를 subprocess를 통해 실행
    command = [
        'ffmpeg',
        '-i', input_file,        # 입력 파일
        '-codec', 'copy',        # 코덱을 변경하지 않고 복사
        output_file              # 출력 파일
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MKV to MP4 without losing quality')
    parser.add_argument('input_file', type=str, help='Path to the input MKV file')
    parser.add_argument('output_file', type=str, help='Path to the output MP4 file')
    
    args = parser.parse_args()
    
    convert_mkv_to_mp4(args.input_file, args.output_file)

