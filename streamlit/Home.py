# pages/home.py
import streamlit as st
from datetime import datetime

def run():
    st.title('Home')

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
