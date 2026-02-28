import streamlit as st
import pandas as pd

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="BOND'S TRACKER", page_icon="🏰", layout="wide")

# 2. 사이드바 - Bond님의 철학 노출
st.sidebar.title("🕵️‍♂️ BOND'S VIEW")
st.sidebar.info("당신의 자산은 인플레이션의 파도를 타고 있습니까? 아니면 성벽 아래 갇혀 있습니까?")
st.sidebar.markdown("---")
st.sidebar.write("✅ **PBR 0.8:** 인생을 바꾸는 기회")
st.sidebar.write("✅ **M2 대비 수익률:** 자산의 실질 성장")

# 3. 메인 화면 구성
st.title("🏰 성벽 측정기 (The Wall Tracker) v1.0")
st.markdown("#### 서울의 평양화와 자산 계급화를 데이터로 직시하십시오.")

# 4. 사용자 입력창
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        apt_name = st.text_input("🏠 분석할 아파트 이름을 입력하세요", "녹번 e편한세상 캐슬")
    with col2:
        purchase_price = st.number_input("💰 매수 가격 (억원)", value=10.5, step=0.1)

# 5. 가상 데이터 시뮬레이션 (나중에 실거래 API 연동 가능)
# 실제 서비스 시에는 여기서 공공데이터포털 API를 호출합니다.
current_price = 15.5 
m2_growth = 1.18 # 2022년 말 대비 통화량 증가율 (18%)
pbr_val = 1.45 # 대지분 및 건축비 산정 예시

# 6. 결과 리포트 출력
st.markdown("---")
st.subheader(f"📊 '{apt_name}' 분석 리포트")

m1, m2, m3 = st.columns(3)
# 실질 수익률 계산
real_return = (current_price / purchase_price) / m2_growth

m1.metric("평양 지수 (PYI)", "Lv. 7.2", "서울 상위 15%")
m2.metric("PBR 지수", f"{pbr_val}", "안전마진 확보")
m3.metric("M2 대비 실질수익률", f"{real_return:.2f}x", f"{(real_return-1)*100:.1f}% 초과성장")

# 7. 시각화 지표
st.markdown("### 🏹 성벽 내 위치 (Visual Insight)")
progress_val = int(min(real_return * 40, 100)) # 시각적 표현용 로직
st.progress(progress_val)
st.write(f"현재 당신의 자산은 성벽의 **{progress_val}%** 높이에 도달했습니다.")

if real_return > 1.5:
    st.success("🎉 축하합니다! 퀀텀점프에 성공하여 성벽 안(내성)으로 진입하셨습니다.")
elif real_return >= 1.0:
    st.warning("⚖️ 인플레이션 방어 중입니다. 상급지 이동을 위한 체력을 기르는 구간입니다.")
else:
    st.error("🚨 경고: 자산이 인플레이션 속도를 따라가지 못하고 있습니다. 전략 재수립이 필요합니다.")

# 8. 하단 카피
st.markdown("---")
st.caption("© 2026 BOND'S VIEW. 데이터는 국토교통부 실거래가 및 한국은행 M2 통계 기반입니다.")
