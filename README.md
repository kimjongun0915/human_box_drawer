# 👤 YOLOv8 기반 사람 인식기 (Person Detector)

이 프로젝트는 YOLOv8을 이용해 영상 속 사람만을 인식하고, 해당 객체를 실시간으로 추적하며 박스를 그리는 파이썬 프로그램입니다.

🎥 참고 영상  
📹 실행 결과 영상: https://youtu.be/jfDyokxrWHs  
📂 사용한 원본 영상: https://youtu.be/X28uGaImYNs

## ✅ 주요 기능

- YOLOv8n.pt 모델을 사용하여 영상에서 사람(person)만 감지
- 인식된 사람 객체에 사각형 박스와 텍스트("Person") 표시
- 약 30프레임마다 FPS(초당 프레임 수) 출력
- 실시간 프레임 디스플레이
- q 키 입력 시 프로그램 종료

## 🧾 코드 설명

- YOLO("yolov8n.pt"): 사전 학습된 YOLOv8 nano 모델 로드
- cap = cv2.VideoCapture(...): 영상 불러오기
- results = model(frame)[0]: 프레임에 대한 YOLO 예측 결과 얻기
- model.names[cls_id] != "person": 사람 클래스만 필터링
- cv2.rectangle(), cv2.putText(): 박스 및 레이블 시각화
- cv2.imshow(): 실시간 프레임 출력
- cv2.waitKey(1): q 키 입력 시 종료

## 📁 파일 구성

person_detector.py         # 메인 실행 파일  
nmixx_dance.mp4.webm       # 입력 비디오 (사용자 로컬 경로 기준)

## 🛠️ 설치 방법

Python 3.8 이상 환경이 필요하며, 아래 명령어로 필수 패키지를 설치하세요:

pip install opencv-python ultralytics numpy

## ▶️ 실행 방법

python person_detector.py

※ VIDEO_PATH 경로를 실제 본인의 영상 경로로 수정해야 합니다.

## 🧠 사용된 기술

YOLOv8 (Ultralytics): 객체 탐지를 위한 최신 딥러닝 모델  
OpenCV: 영상 스트림 처리, 프레임 단위 시각화에 사용

## 🖼️ 결과 예시

- 초록색 사각형으로 사람 인식 영역이 표시됩니다
- 콘솔에 FPS가 30프레임 단위로 출력됩니다
- q 키로 프로그램 종료가 가능합니다

## 📩 문의

프로젝트 관련 문의사항은 저장소의 이슈 또는 댓글로 남겨주세요.
