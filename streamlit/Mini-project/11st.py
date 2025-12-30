import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import base64
import time
from datetime import datetime, timedelta
from supabase import create_client  # pip install supabase

# =====================================================
# 1. 페이지 설정
# =====================================================
st.set_page_config(
    layout="wide",
    page_title="🛰️ Attack 상세 모니터링",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. 배경 이미지 + 공통 CSS
# =====================================================
def set_bg(image_file):
    if not os.path.exists(image_file):
        st.markdown("""<style>.stApp { background-color: #0e1117; }</style>""", unsafe_allow_html=True)
        return

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(5,15,25,0.45), rgba(5,15,25,0.45)), url("data:image/jpg;base64,{encoded}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .title-card {{
        background: rgba(10,20,35,0.55); backdrop-filter: blur(10px); border-radius: 18px;
        padding: 22px 30px; margin: 10px auto 25px auto; width: fit-content;
        box-shadow: 0 0 30px rgba(0,229,255,0.25);
    }}
    .attack-title {{
        text-align: center; font-size: 42px; font-weight: 800; color: #00e5ff; margin: 0;
    }}
    div[data-testid="stPlotlyChart"], div[data-testid="stDataFrame"] {{
        background: rgba(10,20,35,0.55); backdrop-filter: blur(8px); border-radius: 14px; padding: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("background.jpg")

# =====================================================
# 3. 데이터 로드 (Supabase 연동)
# =====================================================
# Supabase 연결 초기화 (캐시 사용으로 리소스 절약)
@st.cache_resource
def init_connection():
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Supabase 연결 실패: secrets.toml을 확인하세요. ({e})")
        return None

supabase = init_connection()

def load_data():
    if not supabase:
        return pd.DataFrame()

    try:
        # DB에서 최신 500개 데이터 가져오기 (created_at 기준 내림차순)
        response = supabase.table("attack_logs").select("*").order("created_at", desc=True).limit(500).execute()
        df = pd.DataFrame(response.data)

        if not df.empty:
            # 컬럼 매핑 (DB 컬럼명 -> 대시보드 컬럼명)
            df = df.rename(columns={
                "created_at": "발생시간",
                "ip_address": "출발지IP",
                "country": "출발지국가",
                "organization": "목적지기관",
                "attack_type": "공격유형",
                "count": "건수"
            })

            # 시간 변환 (UTC -> 한국 시간 KST)
            df["발생시간"] = pd.to_datetime(df["발생시간"]) + pd.Timedelta(hours=9)

        return df
    except Exception as e:
        st.error(f"데이터 불러오기 오류: {e}")
        return pd.DataFrame()

df = load_data()

# =====================================================
# 4. 헤더
# =====================================================
st.markdown("""
<div class="title-card">
    <div class="attack-title">
        🛰️ ATTACK 실시간 관제 대시보드
    </div>
</div>
""", unsafe_allow_html=True)

# 데이터가 없을 경우 처리
if df.empty:
    st.warning("📡 DB에 데이터가 없습니다. GitHub Actions가 실행 중인지 확인하세요.")
    st.stop()

# =====================================================
# 5. 상단 영역
# =====================================================
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📊 시간대별 공격 탐지량")
    df_hour = df.set_index("발생시간").resample("H").size().reset_index(name="count")

    fig = go.Figure()
    fig.add_bar(x=df_hour["발생시간"], y=df_hour["count"], name="건수")
    fig.add_scatter(x=df_hour["발생시간"], y=df_hour["count"], mode="lines+markers", name="추세")

    fig.update_layout(
        template="plotly_dark", height=320,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📈 시스템 상태")
    st.metric("TOTAL EVENTS", f"{len(df):,}")
    st.metric("TOTAL HITS", f"{df['건수'].sum():,}")

    # 1분 카운트다운 및 상태 표시
    st.info(f"🔄 **실시간 연동 중**\n\n마지막 갱신: {datetime.now().strftime('%H:%M:%S')}")

st.divider()

# =====================================================
# 6. 중단 그래프
# =====================================================
mid1, mid2, mid3 = st.columns(3)

def transparent_layout(fig, h=280):
    fig.update_layout(
        template="plotly_dark", height=h,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

with mid1:
    st.subheader("🌐 국가별 분포")
    fig = px.pie(df, names="출발지국가", hole=0.4)
    st.plotly_chart(transparent_layout(fig), use_container_width=True)

with mid2:
    st.subheader("🏢 기관별 공격건수")
    df_org = df.groupby("목적지기관")["건수"].sum().reset_index()
    fig = px.bar(df_org, x="건수", y="목적지기관", orientation="h", color="목적지기관")
    st.plotly_chart(transparent_layout(fig), use_container_width=True)

with mid3:
    st.subheader("🛡️ 공격 유형별 비중")
    df_type = df.groupby("공격유형").size().reset_index(name="count")
    fig = px.funnel(df_type, x="count", y="공격유형")
    st.plotly_chart(transparent_layout(fig), use_container_width=True)

st.divider()

# =====================================================
# 7. 하단 테이블
# =====================================================
st.subheader("📝 실시간 경보 발생 현황 (DB)")

def highlight_attack(row):
    if row["공격유형"] == "02.악성코드 유포":
        return ["background-color: #4a0000; color: white"] * len(row)
    if row["공격유형"] == "01.침입 시도":
        return ["background-color: #3e3e00; color: #ffd700"] * len(row)
    return [""] * len(row)

styled_df = (
    df.sort_values("발생시간", ascending=False)
    .head(100)
    .style.apply(highlight_attack, axis=1)
)

st.dataframe(styled_df, use_container_width=True, height=400)

# =====================================================
# 8. 자동 새로고침 로직 (1분)
# =====================================================
time.sleep(60) # 60초 대기
st.rerun()     # 페이지 전체 다시 실행