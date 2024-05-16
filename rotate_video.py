import cv2
import sys

def rotate_frame(frame, direction):
    if direction == 'left':
        # 시계 반대 방향으로 90도 회전
        return cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif direction == 'right':
        # 시계 방향으로 90도 회전
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    else:
        raise ValueError("Direction should be 'left' or 'right'")

def rotate_video(input_path, output_path, direction):
    # 비디오 파일을 읽기
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise FileNotFoundError("Video file not found")

    # 비디오 프레임의 높이와 너비 구하기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 회전된 비디오의 높이와 너비 조정
    if direction in ['left', 'right']:
        width, height = height, width

    # 결과 비디오 파일 설정
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임 회전
        frame = rotate_frame(frame, direction)
        out.write(frame)

    # 모든 작업 완료 후 파일 닫기
    cap.release()
    out.release()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python rotate_video.py [input_path] [output_path] [left or right]")
        sys.exit(1)

    _, input_path, output_path, direction = sys.argv
    rotate_video(input_path, output_path, direction)

