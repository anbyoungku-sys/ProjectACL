import streamlit as st
from datetime import date  # 현재 날짜를 사용하기 위해 임포트

# 피드백 폼 생성
with st.form('feedback_form'):
    st.header('Feedback Form')

    # 폼 입력을 컬럼으로 정리
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input('Please enter your name', placeholder='Your full name')
        rating = st.slider('Rate this app (0 = Worst, 10 = Best)', 0, 10, 5)

    with col2:
        dob = st.date_input('Enter your date of birth')
        recommend = st.radio('Would you recommend this app to others?', ('Yes', 'No'))

    # 제출 버튼
    submit_button = st.form_submit_button('Submit')

# 폼 제출 처리
if submit_button:
    # 이름이 비어 있는지 확인
    if not name.strip():
        st.error('Name cannot be empty. Please provide your name.')
    # 생년월일이 유효한지 확인
    elif dob > date.today():
        st.error('Date of birth cannot be in the future.')
    else:
        st.success('Thank you for your feedback!')
        st.write('**Name:**', name)
        st.write('**Date of Birth:**', dob)
        st.write('**Rating:**', rating)
        st.write('**Would Recommend?:**', recommend)
