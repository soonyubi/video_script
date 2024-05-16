import argparse
import os
import cv2

def extract_frames(video_path, output_path):
    # 비디오 불러오기
    video_capture = cv2.VideoCapture(video_path)
    
    # 비디오의 FPS (프레임 속도) 가져오기
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    # 현재 프레임 수
    frame_count = 1
    
    while True:
        # 프레임별로 비디오 읽기
        ret, frame = video_capture.read()
        
        if not ret:
            break
        
        # 프레임 저장
        cv2.imwrite(f"{output_path}/{frame_count}.png", frame)
        
        frame_count += 1
    
    # 비디오 캡쳐 객체 해제
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 명령줄 인수 파싱
    parser = argparse.ArgumentParser(description="Extract frames from a video file")
    parser.add_argument("video_file_path", help="Path to the input video file")
    parser.add_argument("output_directory", help="Directory to save the extracted frames")
    args = parser.parse_args()

    # 입력된 디렉토리가 없다면 생성
    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    # 프레임 추출 함수 호출
    extract_frames(args.video_file_path, args.output_directory)