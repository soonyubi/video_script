import subprocess
import sys

def merge_videos(output_name, input_videos):
    # 일시적인 파일 리스트를 만든다
    with open("filelist.txt", "w") as file:
        for video in input_videos:
            file.write(f"file '{video}'\n")
    
    # ffmpeg 명령어를 구성하여 비디오 파일들을 병합
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'filelist.txt',
        '-c', 'copy',
        output_name
    ]
    
    # 명령어 실행
    subprocess.run(command, check=True)
    
    # 사용이 끝난 리스트 파일을 삭제
    subprocess.run(['rm', 'filelist.txt'])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_video.py [output name] [input video1, input video2, ...]")
        sys.exit(1)

    output_name = sys.argv[1]
    input_videos = sys.argv[2:]
    merge_videos(output_name, input_videos)

