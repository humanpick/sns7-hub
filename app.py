import streamlit as st

# 1. 페이지 설정 (와이드 레이아웃, 사이드바 숨김)
st.set_page_config(
    page_title="후미남 프리미엄 로드탁송",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Humanpick 디자인 시스템 CSS 적용
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    * {
        font-family: 'Pretendard', sans-serif;
    }
    
    .stApp {
        background-color: #0B1120;
        color: #FFFFFF;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    header, footer {visibility: hidden;}
    
    /* 글래스모피즘 카드 스타일 */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .hero-title {
        font-size: 1.6rem;
        font-weight: 700;
        background: linear-gradient(135deg, #8B5CF6, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 8px;
    }
    
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #38BDF8;
        margin-bottom: 8px;
        border-left: 3px solid #8B5CF6;
        padding-left: 8px;
    }
    
    /* 화이트 폼 스타일 (입력창 순백색 배경, 폰트 굵기 600) */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    /* 폼 제출 버튼 가독성 강제 보정 */
    div[data-testid="stForm"] button {
        width: 100% !important;
        background: linear-gradient(135deg, #8B5CF6, #EC4899) !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 20px !important;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    /* 버튼 내부 텍스트 및 아이콘 색상 강제 지정 */
    div[data-testid="stForm"] button p, 
    div[data-testid="stForm"] button span {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }

    div[data-testid="stForm"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 헤더 및 소개 섹션
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <div class="hero-title">후미남 프리미엄 로드탁송</div>
    <p style="text-align: center; color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">
        "후각과 미각은 잃었지만, 안전을 향한 감각은 선명합니다."<br>
        요란한 말 대신, 묵직한 책임감과 행동으로 증명합니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. 왜 나에게 맡겨야 하는지 & 탁송이 필요한 상황
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="min-height: 190px;">
        <div class="section-header">🚗 이런 분께 필요합니다</div>
        <ul style="color: #CBD5E1; font-size: 0.85rem; padding-left: 15px; margin: 0; line-height: 1.6;">
            <li>신차 출고 후 안전하게 탁송이 필요할 때</li>
            <li>장거리 이동 및 지방 출장으로 운행이 부담될 때</li>
            <li>법인 차량 및 중요한 차량을 믿고 맡길 기사가 필요할 때</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="min-height: 190px;">
        <div class="section-header">🛡️ 왜 후미남인가?</div>
        <ul style="color: #CBD5E1; font-size: 0.85rem; padding-left: 15px; margin: 0; line-height: 1.6;">
            <li><b>100% 비흡연 운행</b>으로 쾌적한 실내 유지</li>
            <li>출발부터 도착까지 철저한 사진/문자 안심 브리핑</li>
            <li>시련을 딛고 일어선 프로 드라이버의 투철한 안전 의식</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 5. 탁송 접수 방법 안내
st.markdown("""
<div class="glass-card">
    <div class="section-header">📋 탁송 접수 절차</div>
    <p style="color: #CBD5E1; font-size: 0.85rem; margin: 0;">
        1단계: 아래 폼에 차량 정보(차종, 번호, 변속기)와 출발지, 도착지를 남겨주세요.<br>
        2단계: 확인 즉시 안전 운행 가능 여부와 함께 신속하게 연락을 드립니다.<br>
        3단계: 안심하고 맡겨주시면 목적지까지 안전하게 인도해 드립니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 6. 실시간 탁송 접수 폼 (오토/스틱 선택 항목 추가)
st.markdown('<div class="section-header" style="margin-top: 15px;">✍️ 간편 탁송 접수하기</div>', unsafe_allow_html=True)

with st.form("toksong_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        car_model = st.text_input("차종 (예: 그랜저 / 2024년식)", placeholder="차종을 입력하세요")
    with col_b:
        car_number = st.text_input("차량 번호 (예: 123가 4567)", placeholder="차량 번호를 입력하세요")
        
    col_e, col_f = st.columns(2)
    with col_e:
        transmission = st.selectbox("변속기 종류", ["오토 (Automatic)", "수동 (Manual / 스틱)"])
    with col_f:
        phone_number = st.text_input("연락처 (휴대폰 번호)", placeholder="010-0000-0000")
        
    col_c, col_d = st.columns(2)
    with col_c:
        departure = st.text_input("출발지 (예: 서울 강남구 / 상세 주소)", placeholder="출발지를 입력하세요")
    with col_d:
        destination = st.text_input("도착지 (예: 부산 해운대구 / 상세 주소)", placeholder="도착지를 입력하세요")
        
    memo = st.text_area("요청 및 특이사항 (선택)", placeholder="경유지나 특별히 요청하실 사항을 적어주세요.")
    
    submitted = st.form_submit_button("🚀 탁송 신청 및 접수하기")
    
    if submitted:
        if departure and destination and phone_number and car_number:
            st.success("🎉 탁송 접수가 정상적으로 완료되었습니다! 확인 후 빠르게 연락드리겠습니다.")
        else:
            st.error("⚠️ 필수 항목(차량번호, 출발지, 도착지, 연락처)을 모두 입력해 주세요.")

# 푸터
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.8rem; margin-top: 20px;">
    © 2026 후미남(HUMINAM). All Rights Reserved. | sns7.kr
</div>
""", unsafe_allow_html=True)
