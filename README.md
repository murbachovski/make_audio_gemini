# 프로젝트 제목
```
NASA와 함께하는 우주 대탐험
```

# 프로젝트 설명
```
1. NASA에서 선정한 오늘의 우주 구경
2. 지구 셀카 관찰
3. 뜨거운 태양 관찰
4. 자외선 태양 4종 관찰
```

# 가상환경 설정
```
conda create -n nasa_gem python=3.9
```

# API_KEY 설정
```
export NASA_KEY=""
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
[위키독스](https://wikidocs.net/254713)<br>

# NASA OpenAPI 참고 문서
[NASA](https://api.nasa.gov/)<br>
[NASA OpenAPI 안내](https://ssd-api.jpl.nasa.gov/doc/index.php)<br>
