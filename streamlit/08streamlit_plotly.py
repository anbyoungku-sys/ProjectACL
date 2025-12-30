import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터프레임 생성
df = pd.DataFrame(data={
    'Exam': ['Exam 1', 'Exam 2', 'Exam 3'],
    'Jessica': [77, 76, 87],
    'John': [56, 97, 95]
})

# 선 플롯으로 플로틀리 피규어 생성
fig = go.Figure(data=[
    go.Scatter(name='Jessica', x=df['Exam'], y=df['Jessica'], mode='lines+markers'),
    go.Scatter(name='John', x=df['Exam'], y=df['John'], mode='lines+markers')
])

# 레이아웃 업데이트
fig.update_layout(
    xaxis_title='Exam',
    yaxis_title='Score',
    legend_title='Name',
)

# 선택 기능이 활성화된 상태로 스트림릿을 사용하여 플롯 표시
event = st.plotly_chart(fig, on_select='rerun')

# 선택된 포인트 접근
if event and event.selection:
    selected_data = []
    for point in event.selection.points:
        selected_data.append({
            'Exam': point['x'],
            'Student': point['curve_number'],
            'Score': point['y']
        })
    # curveNumber를 학생 이름으로 매핑
    for item in selected_data:
        item['Student'] = fig.data[item['Student']].name
    st.write('Selected Exam Scores:')
    st.dataframe(selected_data)

st.divider()

# 대학 위치 데이터
df = pd.DataFrame(data={'university': ['Harvard University', 'Yale University', 'Princeton University',
                                       'Columbia University', 'Brown University', 'Dartmouth University',
                                       'University of Pennsylvania', 'Cornell University'],
                        'latitude': [42.3770, 41.3163, 40.3573, 40.8075, 41.8268, 43.7044, 39.9522, 42.4534],
                        'longitude': [-71.1167, -72.9223, -74.6672, -73.9626, -71.4025, -72.2887, -75.1932, -76.4735]
                        })

# scattergeo 플롯 생성
fig = go.Figure(data=go.Scattergeo(
    lon=df['longitude'],
    lat=df['latitude'],
    text=df['university'],
    mode='markers',
    marker=dict(size=10, color='red', opacity=0.7)
))

# 미국에 초점을 맞추도록 레이아웃 업데이트 및 추가 지도 속성 설정
fig.update_layout(
    geo_scope='usa',
    geo=dict(
        projection_type='albers usa',
        showland=True,
        landcolor='lightgray',
        subunitwidth=1,
    ))

# 스트림릿을 사용하여 지도 표시
st.plotly_chart(fig)