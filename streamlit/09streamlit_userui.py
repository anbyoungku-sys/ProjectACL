import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# 프로그램 선택을 위한 사이드바
program = st.sidebar.selectbox('Select program', ['Dataframe Demo', 'Other Demo'])
code = st.sidebar.checkbox('Display code')

# 프로그램 로직
if program == 'Dataframe Demo':
    df = px.data.stocks()
    st.title('DataFrame Demo')

    # 주식 종목 선택을 위한 멀티셀렉트
    stocks = st.multiselect('Select stocks', df.columns[1:], default=df.columns[1:])

    # 주식 데이터를 데이터프레임으로 표시
    st.subheader('📈Stock value')
    st.write(df[['date'] + stocks].set_index('date'))

    # 플로틀리 선 차트 그리기
    fig = px.line(df, x='date', y=stocks, hover_data={'date': '|%Y %b %d'})
    st.write(fig)

    # 체크박스 선택 시 코드 표시
    if code:
        st.code(
            """
import streamlit as st
import pandas as pd
import plotly.express as px
df = px.data.stocks()
st.title('DataFrame Demo')
program = st.sidebar.selectbox('Select program', ['Dataframe Demo', 'Other Demo'])
code = st.sidebar.checkbox('Display code')
if program == 'Dataframe Demo':
    df = px.data.stocks()
    st.title('DataFrame Demo')
    stocks = st.multiselect('Select stocks', df.columns[1:], default=df.columns[1:])
    st.subheader('Stock value')
    st.write(df[['date'] + stocks].set_index('date'))
    fig = px.line(df, x='date', y=stocks, hover_data={'date': '|%Y %b %d'})
    st.write(fig)
"""
        )
elif program == 'Other Demo':
    st.title('Other Demo')

    BASE_DIR = Path(__file__).parent
    csv_path = BASE_DIR / "auto.csv"  # 경로지정

    st.header("Dataframes and Tables")
    df = pd.read_csv(csv_path)

    # 데이터집합을 가변적으로 출력
    st.dataframe(df.head(10))

    # 데이터집합을 정적으로 출력
    st.table(df.head(10))

    # 차트 위젯
    st.area_chart(df[["mpg","cylinders"]])

    st.bar_chart(df[["mpg","cylinders"]].head(20))

    st.line_chart(df[["mpg","cylinders"]].head(20))

    # matplotlib, seaborn 위젯
    fig, ax = plt.subplots()
    corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot= True)
    st.pyplot(fig)

