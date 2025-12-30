# naviagtion3.py
import streamlit as st
import Home
import Contact

# 현재 페이지 확인
current_page = st.query_params.get('page', ['home'])

# streamlit의 페이지 전환을 py파일이 아닌
# if 조건문을 이용해서 URL 매개변수 기반으로 구현함
# 즉, 특정 페이지를 직접 보여주는 것이 아니고
# 조건에 따라 어떤 페이지를 보여줄지 결정함.
# 예 ?page=home, ?page=contact

# 페이지에 따라 올바른 콘텐츠 표시
if current_page == 'home':
    Home.run()
elif current_page == 'contact':
    Contact.run()


# 하위 URL 간 이동을 위한 링크 추가
# 버튼 클릭시 지정한 페이지를 출력하기 위해 rerun()호출
st.sidebar.title('Pages')
if st.sidebar.button('Home'):
    st.query_params['page'] = 'home'
    st.rerun()
if st.sidebar.button('Contact'):
    st.query_params['page'] = 'contact'
    st.rerun()
