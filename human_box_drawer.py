import cv2
import numpy as np
from ultralytics import YOLO
import time

VIDEO_PATH = r"D:\python\nmixx_dance_faceid\nmixx_dance.mp4.webm"

print("[INFO] 영상 분석 시작...")

# YOLOv8 Detect 모델 로드
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"❌ 영상 열기 실패: {VIDEO_PATH}")
    exit()

target_width = 960
cv2.namedWindow("YOLOv8 Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLOv8 Detection", target_width, 720)

frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1

    h, w = frame.shape[:2]
    scale = target_width / w
    frame = cv2.resize(frame, (int(w * scale), int(h * scale)))

    results = model(frame)[0]  # 예측 결과

    for box in results.boxes:
        cls_id = int(box.cls[0])
        if model.names[cls_id] != "person":
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, "Person", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # FPS 표시
    if frame_count % 30 == 0:
        fps = 30 / (time.time() - start_time)
        print(f"[INFO] FPS: {fps:.2f}")
        start_time = time.time()

    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
