# 프로젝트 제목
```
MusicGeneration
```

# 프로젝트 설명
```
1. 프롬프트 입력
2. 오디오 파일 길이 선택
3. Gemini AI 오디오 파일 생성
4. 오디오 파일 듣기 및 다운로드
```

# 가상환경 설정
```
conda create -n gem python=3.9
```

# API_KEY 설정
```
export GENAI_API_KEY=""
```

# 라이브러리 설치
```
pip install -r requirements.txt
```

# 앱 실행
```
./run.sh
```

# 웹 구성
<p align="center">
  <img src="https://github.com/user-attachments/assets/537bc43d-a7e4-4d90-a4c2-a77b4b37b3d4" width="700">
  <img src="https://github.com/user-attachments/assets/6de8efa8-a5d8-48e7-ba90-f258628bb630" width="700">
  <img src="https://github.com/user-attachments/assets/d2649016-aae3-4872-a23a-ab0bd54f70f8" width="700">
  <img src="https://github.com/user-attachments/assets/5c333911-73ba-48b5-8d7b-79a0ff922412" width="700">
  <img src="https://github.com/user-attachments/assets/485cbb68-7e33-4bc4-aba9-f1459405d657" width="700">
</p>

# Ngrok
(로컬 서버 => 공개 서버로 전환)
```
<Mac M1 설치 기준>
https://ngrok.com/downloads/mac-os
brew install ngrok
ngrok config add-authtoken <token>
ngrok http 80
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/5ca755c3-d8f8-4088-b3b4-1b735945d351" width="700">
</p>

# Ngrok(공개 서버 접속)
[Ngrok 공개 서버 접속](https://c83c0967a9dd.ngrok-free.app/)<br>

# Ngrok 참고 문서
[위키독스](https://cordcat.tistory.com/105)<br>

# Make requirements.txt
```
pip install pipreqs
```

# pipreqs 참고 문서
[PyPI pipreqs](https://pypi.org/project/pipreqs/)<br>

# Gemini 참고 문서
[위키독스](https://ai.google.dev/gemini-api/docs/music-generation)<br>


