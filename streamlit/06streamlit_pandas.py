import streamlit as st
import pandas as pd
import numpy as np

# 재현성을 위해 시드 설정
np.random.seed(0)

# 무작위 데이터로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1', 'Column 2', 'Column 3')
)

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)

# 데이터프레임 필터링 (변형)
# 블리언 인덱싱 (행 필터링)
# 데이터프레임[데이터프레임['컬럼명'] 조건식]
# 첫번째 컬럼의 값이 0보다 큰 것만 선택
df = df[df['Column 2'] > 0]

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame (col2: 0보다 큰 값만 출력)')
st.dataframe(df)

# 첫번째 컬럼의 값이 1보다 큰 것만 선택
df = df[df['Column 1'] > 1]

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame (col1: 1보다 큰 값만 출력)')
st.dataframe(df)

# 첫번째/세번째 컬럼의 값이 0.5보다 큰 것만 선택
df = df[(df['Column 1'] > 0.5) & (df['Column 3'] > 0.5)]
st.subheader('Mutated DataFrame (col1/col3: 0.5보다 큰 값만 출력)')
st.dataframe(df)

# 첫번째/세번째 컬럼의 값이 0.5보다 큰 것만 선택 2
df = df.query('`Column 1` > 0.5 and `Column 3` > 0.5')
# df = df.query('Column1 > 0.5 and Column3 > 0.5')
st.subheader('Mutated DataFrame (col1/col3: 0.5보다 큰 값만 출력)')
st.dataframe(df)

# 첫번째 컬럼의 값이 1.0 ~ 2.0 사이 값만 선택 2
# df = df[(df['Column 1'] >= 1.0) & (df['Column 1'] <= 2.0)]
# df = df.query('`Column 1` >= 1.0 and `Column 1` <= 2.0')
# df = df[df['Column 1'].between(1.0, 2.0)]
df = df.query('`Column 1`.between(1.0, 2.0)')
st.subheader('Mutated DataFrame (col1: 1.0 ~ 2.0사이 값만 출력)')
st.dataframe(df)


# 'Column 1'을 기반으로 새 컬럼 'Column 4' 생성
# 람다함수: 이름 없이(익명) 한 줄로 쓰는 간단한 함수
# 형식: lambda 매개변수: 반환값
# 일반함수 - def add(x, y):
#               return x + y
# 람다식 -  lambda x, y: x + y
# 특히, pandas, map, filter, sorted 등에 자주 사용
df = df.assign(Column_4 = lambda x: x['Column 1'] * 2)

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame (col4: 람다함수로 생성)')
st.dataframe(df)

st.divider()

# 0과 100 사이의 임의의 정수로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randint(0, 101, size=(6, 3)),
    columns=('Exam 1', 'Exam 2', 'Exam 3')
)

# 'Name'과 'Category' 컬럼 직접 할당
df['Name'] = ['John', 'Jessica', 'Jessica', 'John', 'John', 'Jessica']
df['Category'] = ['B', 'A', 'A', 'B', 'A', 'B']

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)

# 'Name'과 'Category'로 그룹화하고 각 그룹의 첫 번째 행 가져오기
df_grouped = df.groupby(['Name', 'Category']).first()

# 그룹화 후 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df_grouped)

st.divider()

# 첫 번째 데이터프레임 생성 (df1)
df1 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 1': [77, 56]})

# 두 번째 데이터프레임 생성 (df2)
df2 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 2': [76, 97]})

# 세 번째 데이터프레임 생성 (df3)
df3 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 3': [87, 95]})

# 원본 데이터프레임 표시
st.subheader('Original DataFrames')
st.dataframe(df1)
st.dataframe(df2)
st.dataframe(df3)

# 'Name' 컬럼을 기준으로 내부 조인(inner join)을 사용하여 데이터프레임 병합
df_merged = df2.merge(df3, how='inner', on='Name')
df_merged = df1.merge(df_merged, how='inner', on='Name')

# 병합 후 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df_merged)

