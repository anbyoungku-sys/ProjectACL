import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임 생성
df = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                        'Exam 1': [77, 56],
                        'Exam 2': [76, 97],
                        'Exam 3': [87, 95]})

# 'Name' 컬럼을 인덱스로 설정하고 막대 차트 그리기
df.set_index('Name').plot(kind='bar', xlabel='Name', ylabel='Exam', rot=0)

# 스트림릿을 사용하여 플롯 표시
st.pyplot(plt)

st.divider()

# 데이터프레임 생성
df = pd.DataFrame(data={'Exam': ['Exam 1', 'Exam 2', 'Exam 3'],
                        'Jessica': [77, 76, 87],
                        'John': [56, 97, 95]})

# 'Exam'을 인덱스로 설정하고 선 차트 그리기
df.set_index('Exam').plot(kind='line', xlabel='Exam', ylabel='Score', subplots=True)

# 스트림릿을 사용하여 플롯 표시
st.pyplot(plt)
