import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import requests

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5'])

with tab1:
    st.subheader('_Tab 1_')

    # 본문의 익스팬더
    st.subheader('Expander')
    with st.expander('Time'):
        time = datetime.now().strftime('%H:%M:%S')
        st.write(f'**{time}**')

    # 본문의 컬럼
    st.subheader('Columns')
    col1, col2 = st.columns(2)
    with col1:
        option_4 = st.selectbox('Please select option 4', ['A', 'B'])
    with col2:
        option_5 = st.radio('Please select option 5', ['A', 'B'])

    # 본문의 컨테이너
    container = st.container()
    container.subheader('Container')
    option_6 = container.slider('Please select option 6')
    st.warning('Elements outside of container will be displayed externally')
    container.info(f'**Option 6:** {option_6}')

with tab2:
    # 본문의 팝오버
    st.subheader('Popover')
    with st.popover('Popover'):
        option_7 = st.radio('Please select option 7', ['A', 'B'])
    st.write(f'**Option 7:** {option_7}')

    # 본문의 대화 상자
    # 다른 말로는 모달 대화상자라고도 함
    # 모달 대화상자 : 대화상자가 열려있는 동안 사용자는 다른 작업을 할 수 없음
    # 모달 대화상자 : 대화상자가 열려있는 동안 사용자는 다른 화면 조작 불가
    # 예) 메모장에서 '파일-열기' 대화상자를 띄운 경우
    # 모달리스 대화상자 : 대화상자가 열려있는 동안 사용자는 다른 화면 조작 가능
    # 예) 메모장에서 '편집-찾기' 대화상자를 띄운 경우
    # 스트림릿의 세션 관리
    # 스트림릿은 스크립트를 매번 위에서 다시 실행하는 구도임 - 기존값은 없어짐
    # 따라서, 값 우지를 위해 st.session_state를 사용함
    # 사용자가 고른 option_8의 값을 세션에 저장

    st.subheader('Dialog box')
    @st.dialog('Option 8')
    def dialog_box():
        option_8 = st.selectbox('Please select option 8', ['A', 'B'])
        if st.button('Submit'):
            st.session_state['option_8'] = option_8
            # st.rerun() 이벤트 발생시 UI를 새로 그리게 함

    if 'option_8' not in st.session_state:
        if st.button('Dialog box'):
            dialog_box()
    else:
        st.write(f'**Option 8:** {st.session_state["option_8"]}')

with tab3:
    show_sidebar = st.checkbox('사이드바 보여주기')

    if show_sidebar:
        # 사이드바의 익스팬더
        st.sidebar.subheader('Expander')
        with st.sidebar.expander('Time'):
            time = datetime.now().strftime('%H:%M:%S')
            st.write(f'**{time}**')

        # 사이드바의 컬럼
        st.sidebar.subheader('Columns')
        col1, col2 = st.sidebar.columns(2)
        with col1:
            option_1 = st.selectbox('Please select option 1', ['A', 'B'])
        with col2:
            option_2 = st.radio('Please select option 2', ['A', 'B'])

        # 사이드바의 컨테이너
        container = st.sidebar.container()
        container.subheader('Container')
        option_3 = container.slider('Please select option 3')
        st.sidebar.warning('Elements outside of container will be displayed externally')
        container.info(f'**Option 3:** {option_3}')

with tab4:
    st.title('Clock')

    clock = st.empty()

    show_clock = st.checkbox('시간 보여주기')

    if show_clock:
        # 자동으로 페이지를 일정 간격으로 새로고침하게 해주는 함수
        # 실시간 데이터 표시, 시계, 알람, 센서 값등 주기적 업데이트가 필요한 경우 유용
        st_autorefresh(interval=500, key='clock_refresh')

        time = datetime.now().strftime('%H:%M:%S')

        # 플레이스홀더에 현재 시간 표시
        clock.info(f'**Current time:** {time}')

        if time > '11:55:15':
            # 알람 조건이 충족되면 시간 표시를 지우고 알람 표시
            clock.empty()
            st.warning('Alarm!!')

with tab5:
    go_download = st.checkbox('파일다운로드')

    if go_download:

        progress_text = st.empty()

        # 진행 표시줄 위젯 생성, 초기값은 0%
        progress_bar = st.progress(0)

        def download_file(url, filename):
            # 파이썬용 Http 요청 라이브러리
            # 웹 사이트의 있는 정보를 요청(get)하거나, 정보를 보내거나(post)
            # 쿠키, 헤더, 인증등 웹과 관련된 복잡한 작업을 수행함
            # 사용시 브라우져 헤더를 반드시 설정
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}

            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            with open(filename, "wb") as f:
                downloaded = 0
                # chunk : 데이터 덩어리, 조각을 의미
                # 보통 파일이나 데이터를 한번에 통채로 처리하지 않고 나눠 처리할때 사용
                # 특히 큰 파일이나 스티리밍시 유용하게 사용
                # chunk_size=8192 -> 다운 로드할 파일을 8kb chunk 단위로 나눠 응답으로 받음
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = int(downloaded * 100 / total_size) if total_size else 0

                        # 진행 텍스트와 진행 표시줄 업데이트
                        progress_text.subheader(f'Progress: {percent}%')
                        progress_bar.progress(percent)
            return filename

        # 사용자 정의 진행 표시줄을 사용하여 requests로 파일 다운로드
        download_file('https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/pt/2024/05/31/202405311915778523_6659a350aad3b.jpg', 'suji.jpg')


