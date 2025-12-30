import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import base64
from datetime import datetime, timedelta

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
        st.warning(f"⚠ 배경 이미지 없음: {image_file}")
        return

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    /* ===== 전체 배경 ===== */
    .stApp {{
        background:
            linear-gradient(rgba(5,15,25,0.45), rgba(5,15,25,0.45)),
            url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* ===== 타이틀 카드 (그래프와 동일 컨셉) ===== */
    .title-card {{
        background: rgba(10,20,35,0.55);
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 22px 30px;
        margin: 10px auto 25px auto;
        width: fit-content;
        box-shadow: 0 0 30px rgba(0,229,255,0.25);
    }}

    .attack-title {{
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #00e5ff;
        margin: 0;
    }}

    /* ===== 그래프 카드 ===== */
    div[data-testid="stPlotlyChart"] {{
        background: rgba(10,20,35,0.55);
        backdrop-filter: blur(8px);
        border-radius: 14px;
        padding: 10px;
    }}

    /* ===== 테이블 카드 ===== */
    div[data-testid="stDataFrame"] {{
        background: rgba(10,20,35,0.55);
        backdrop-filter: blur(8px);
        border-radius: 14px;
        padding: 8px;
    }}

    div[data-testid="stDataFrame"] th {{
        background: rgba(0,0,0,0.6);
        color: #00e5ff;
    }}

    div[data-testid="stDataFrame"] td {{
        background: rgba(0,0,0,0.35);
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("background.jpg")

# =====================================================
# 3. 데이터 생성 / 로드
# =====================================================
FILE_PATH = "attack_log.csv"

def generate_rows(n=100):
    attack_types = ["05.CTI 공격", "00.평판 탐지", "01.침입 시도", "02.악성코드 유포"]
    orgs = ["A기관", "B기관", "C기관", "D기관"]
    countries = ["South Korea", "United States", "China", "Russia"]

    return pd.DataFrame({
        "발생시간": [(datetime.now() - timedelta(minutes=np.random.randint(0, 300))) for _ in range(n)],
        "출발지IP": [
            f"{np.random.randint(1,255)}.{np.random.randint(0,255)}."
            f"{np.random.randint(0,255)}.{np.random.randint(1,255)}"
            for _ in range(n)
        ],
        "출발지국가": np.random.choice(countries, n),
        "목적지기관": np.random.choice(orgs, n),
        "공격유형": np.random.choice(attack_types, n),
        "건수": np.random.randint(1, 10, n)
    })

def load_data():
    if not os.path.exists(FILE_PATH):
        df = generate_rows(1000)
        df.to_csv(FILE_PATH, index=False, encoding="utf-8-sig")
    df = pd.read_csv(FILE_PATH)
    df["발생시간"] = pd.to_datetime(df["발생시간"])
    return df

df = load_data()

# =====================================================
# 4. 헤더 (🔥 그래프 카드 스타일 적용)
# =====================================================
st.markdown("""
<div class="title-card">
    <div class="attack-title">
        🛰️ ATTACK 실시간 관제 대시보드
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# 5. 상단 영역
# =====================================================
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📊 시간대별 공격 탐지량")

    df_hour = df.set_index("발생시간").resample("H").size().reset_index(name="count")

    fig = go.Figure()
    fig.add_bar(x=df_hour["발생시간"], y=df_hour["count"])
    fig.add_scatter(x=df_hour["발생시간"], y=df_hour["count"], mode="lines+markers")

    fig.update_layout(
        template="plotly_dark",
        height=320,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📈 상태")
    st.metric("TOTAL EVENTS", f"{len(df):,}")
    st.metric("TOTAL HITS", f"{df['건수'].sum():,}")

    if st.button("🔄 데이터 새로고침 (+100)"):
        df = pd.concat([df, generate_rows(100)], ignore_index=True)
        df.to_csv(FILE_PATH, index=False, encoding="utf-8-sig")
        st.rerun()

st.divider()

# =====================================================
# 6. 중단 그래프
# =====================================================
mid1, mid2, mid3 = st.columns(3)

def transparent(fig, h=280):
    fig.update_layout(
        template="plotly_dark",
        height=h,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

with mid1:
    st.subheader("🌐 국가별")
    fig = px.pie(df, names="출발지국가", hole=0.4)
    st.plotly_chart(transparent(fig), use_container_width=True)

with mid2:
    st.subheader("🏢 기관별")
    fig = px.bar(
        df.groupby("목적지기관")["건수"].sum().reset_index(),
        x="건수", y="목적지기관", orientation="h"
    )
    st.plotly_chart(transparent(fig), use_container_width=True)

with mid3:
    st.subheader("🛡️ 공격 유형")
    fig = px.funnel(
        df.groupby("공격유형").size().reset_index(name="count"),
        x="count", y="공격유형"
    )
    st.plotly_chart(transparent(fig), use_container_width=True)

st.divider()

# =====================================================
# 7. 하단 테이블
# =====================================================
st.subheader("📝 원본 경보 발생 현황")

def highlight_attack(row):
    if row["공격유형"] == "02.악성코드 유포":
        return ["background-color:#8B0000;color:white"] * len(row)
    if row["공격유형"] == "01.침입 시도":
        return ["background-color:#FFD700;color:black"] * len(row)
    return [""] * len(row)

styled_df = (
    df.sort_values("발생시간", ascending=False)
    .style.apply(highlight_attack, axis=1)
)

st.dataframe(styled_df, use_container_width=True, height=420)
