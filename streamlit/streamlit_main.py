import subprocess
import sys
import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import requests

def run_streamlit(appName):  # 1개의 사용 위치 신규 *
    subprocess.run([
        sys.executable,
        "-m", "streamlit", "run",
        str(appName)
    ])

# 실행 진입점
# 위치는 파일 맨 아래
if __name__ == "__main__":
    # run_streamlit("12streamlit_multi_pages.py")
    # run_streamlit("13streamlit_multi_pages.py")
    # run_streamlit("14streamlit_multi_pages.py")
    run_streamlit("15streamlit_query_params.py")
