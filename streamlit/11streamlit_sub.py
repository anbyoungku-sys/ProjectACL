import streamlit as st
from datetime import datetime
import subprocess
import sys
from pathlib import Path
import os


# 제목 설정
title = 'Hello World'
st.sidebar.title(title)
st.title(title)


def run_streamlit():  # 신규 *
    # 터미널 : streamlit run 11streamlit_sub.py
    # 파이썬으로 실행 : python -m streamlit run 11streamlit_sub.py
    # subprocess : python으로 외부 프로세스를 실행, 제어하는 도구
    subprocess.run([sys.executable,
        "-m", "streamlit", "run", "11streamlit_sub.py"])


def main():  # 1개의 사용 위치 신규 *
    # streamlit이 중복 실행 되는 것을 방지하기 위해
    # 일단 streamlit이 한번 실행 되면, STREAMLIT_CHILD변수 설정함
    # STREAMLIT_CHILD 존재 여부에 따라 재실행은 금지
    if os.environ.get("STREAMLIT_CHILD_1") != "1":
        os.environ["STREAMLIT_CHILD_1"] = "1"
        run_streamlit()
    else:
        pass

# 실행 진입점
# 위치는 파일 맨 아래
if __name__ == "__main__":
    # run_streamlit() <- 직접 호출시 문제 발생-무한루프
    main()





