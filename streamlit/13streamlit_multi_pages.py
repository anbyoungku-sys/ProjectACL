# naviagtion.py
import streamlit as st

# st.navigation : 여러 페이즐ㄹ 탭이나 메뉴처럼 관리할 수 있게 해주는 기능
# 리스트안에 네비게이션 메뉴를 구성할 페이지를 정의
# st.Page : st.navigation에 사용할 페이지를 정의할때 사용하는 객체

pg = st.navigation([st.Page('13streamlit_home.py', title='🏠 Home'),
                    st.Page('13streamlit_contact.py', title='📞 Contact us')])
pg.run()





