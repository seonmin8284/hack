# Gemini 챗봇

Gemini API를 활용한 기본적인 챗봇 프레임워크입니다.

## 기능

- Gemini API를 통한 대화형 챗봇
- 대화 컨텍스트 유지
- 채팅 히스토리 관리
- 반응형 UI

## 설치 방법

1. 저장소를 클론합니다

```bash
git clone [repository-url]
cd gemini_chatbot
```

2. 필요한 패키지를 설치합니다

```bash
pip install -r requirements.txt
```

3. `.env` 파일을 생성하고 API 키를 설정합니다

```
GOOGLE_API_KEY=your_api_key_here
```

## 실행 방법

```bash
streamlit run app.py
```

## 환경 설정

- Python 3.8 이상
- Streamlit 1.32.0
- Google Generative AI 0.3.2

## 주의사항

- API 키는 반드시 안전하게 관리해야 합니다
- `.env` 파일을 절대 공개 저장소에 업로드하지 마세요
