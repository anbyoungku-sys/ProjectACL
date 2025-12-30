import streamlit as st
from PIL import Image
from pathlib import Path


# favicon설정
# 웹사이트를 대표하는 작은 아이콘 - 브랜드 인식을 위해 사용
BASE_DIR = Path(__file__).parent
icofile = BASE_DIR / 'favicon.ico'
icon = Image.open(icofile)

# 페이지 구성
st.set_page_config(
    page_title='Hello World',
    page_icon=icon,
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello World**'
    }
)

# 제목 설정
title = 'Hello World'
st.sidebar.title(title)
st.title(title)


# # 헤더와 푸터를 숨기기 위한 사용자 정의 CSS
# hide_streamlit_style = """
#     <style>
#     /* 스트림릿 헤더 숨기기 */
#     header {
#         visibility: hidden;
#     }
#     /* 스트림릿 푸터 숨기기 */
#     footer {
#         visibility: hidden;
#     }
#     </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# # 사이드바에 사용자 정의 푸터 추가
# custom_footer_style = """
#     <div class="markdown-text-container stText" style="width: 698px;">
#         <footer>
#             <p></p>
#         </footer>
#         <div style="font-size: 12px;">Hello world v 0.1</div>
#         <div style="font-size: 12px;">Hello world LLC.</div>
#     </div>
#     """
# st.sidebar.markdown(custom_footer_style, unsafe_allow_html=True)


import streamlit as st

# 사이드바에 사용자 정의 푸터 추가
custom_footer_style = """
    <style>
    /* 사이드바 푸터를 하단에 고정하는 스타일 */
    [data-testid="stSidebarNav"] + div {
        position: relative;
        height: 100%;
    }
    .custom-footer {
        position: fixed;
        bottom: 20px;
        left: 20px;
        width: 250px; /* 사이드바 너비에 맞춰 조절 */
        font-size: 12px;
        color: #808495; /* 부드러운 회색조 */
        background-color: transparent;
    }
    </style>
    
    <div class="custom-footer">
        <hr style="border: 0.5px solid #e6e9ef;">
        <div>Hello world v 0.1</div>
        <div>Hello world LLC.</div>
    </div>
    """

# 사이드바에 적용
st.sidebar.markdown(custom_footer_style, unsafe_allow_html=True)

# 테스트용 사이드바 내용
st.sidebar.title("메뉴")
st.sidebar.write("내용이 많아져도 푸터는 하단에 유지됩니다.")