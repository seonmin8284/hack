import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# 페이지 설정
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="🤖",
    layout="wide"
)

# 사이드바 설정
with st.sidebar:
    st.title("🤖 Gemini 챗봇")
    st.markdown("---")
    st.markdown("""
    ### 사용 방법
    1. API 키를 입력하세요
    2. 메시지를 입력하세요
    3. 대화를 시작하세요!
    """)
    
    # API 키 입력
    api_key = st.text_input("API 키를 입력하세요:", type="password")
    st.markdown("---")

# 메인 화면 설정
st.title("💬 채팅")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

if "gemini_history" not in st.session_state:
    st.session_state.gemini_history = []

# Gemini 모델 설정
def initialize_gemini():
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=st.session_state.gemini_history)
    return chat

# 채팅 히스토리 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요"):
    if not api_key:
        st.error("API 키를 입력해주세요!")
        st.stop()
    
    # 사용자 메시지 표시
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Gemini 응답 생성
        chat = initialize_gemini()
        with st.chat_message("assistant"):
            with st.spinner("생각 중..."):
                response = chat.send_message(prompt)
                st.markdown(response.text)
                
        # 대화 히스토리 업데이트
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.session_state.gemini_history.append({"role": "user", "parts": [prompt]})
        st.session_state.gemini_history.append({"role": "model", "parts": [response.text]})
        
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")

# 채팅 초기화 버튼
if st.button("대화 초기화"):
    st.session_state.messages = []
    st.session_state.gemini_history = []
    st.experimental_rerun() 