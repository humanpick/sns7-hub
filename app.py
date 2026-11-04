import streamlit as st

# 1. 페이지 설정 (와이드 레이아웃, 사이드바 숨김)
st.set_page_config(
    page_title="후미남 시그니처 로드탁송",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Humanpick 디자인 시스템 CSS 적용 (가독성 및 타이포그래피 대폭 강화)
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
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 16px;
    }
    
    .hero-title {
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #8B5CF6, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .section-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #38BDF8;
        margin-bottom: 10px;
        border-left: 4px solid #8B5CF6;
        padding-left: 10px;
    }
    
    /* 🌟 입력창(텍스트박스 등) 위의 라벨 글자 색상 및 크기 선명하게 강제 수정 */
    .stTextInput label, .stRadio label, .stSelectbox label, .stTextArea label {
        color: #F8FAFC !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }
    
    /* 화이트 폼 입력창 스타일 (순백색 배경, 검은색 볼드체 텍스트) */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
    }

    /* 라디오 버튼 내부 선택 항목 글자색 선명하게 */
    div[data-testid="stRadio"] div[role="radiogroup"] label p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* 폼 제출 버튼 가독성 강제 보정 */
    div[data-testid="stForm"] button {
        width: 100% !important;
        background: linear-gradient(135deg, #8B5CF6, #EC4899) !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.5) !important;
        transition: all 0.3s ease !important;
        margin-top: 10px;
    }
    
    /* 버튼 내부 텍스트 및 아이콘 색상 강제 지정 */
    div[data-testid="stForm"] button p, 
    div[data-testid="stForm"] button span {
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
    }

    div[data-testid="stForm"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(236, 72, 153, 0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 헤더 및 소개 섹션
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <div class="hero-title">후미남 시그니처 로드탁송</div>
    <p style="text-align: center; color: #CBD5E1; font-size: 1rem; line-height: 1.5; margin-bottom: 0;">
        "화려한 수식어 대신, 꺾이지 않는 진정성과 행동으로 증명합니다."<br>
        <span style="color: #38BDF8; font-weight: 600; font-size: 0.9rem;">100% 비흡연 · 철저한 안심 브리핑 · 프리미엄 맞춤 운행</span>
    </p>
</div>
""", unsafe_allow_html=True)

# 4. 왜 나에게 맡겨야 하는지 & 탁송이 필요한 상황
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="min-height: 210px;">
        <div class="section-header">🚗 이런 분께 필요합니다</div>
        <ul style="color: #F1F5F9; font-size: 0.9rem; padding-left: 15px; margin: 0; line-height: 1.7; font-weight: 500;">
            <li>신차 출고 후 안전하게 탁송이 필요할 때</li>
            <li>장거리 이동 및 지방 출장으로 운행이 부담될 때</li>
            <li>법인 차량 및 중요한 차량을 믿고 맡길 기사가 필요할 때</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="min-height: 210px;">
        <div class="section-header">🛡️ 왜 후미남인가?</div>
        <ul style="color: #F1F5F9; font-size: 0.9rem; padding-left: 15px; margin: 0; line-height: 1.7; font-weight: 500;">
            <li><b>100% 비흡연 운행</b>으로 쾌적한 실내 유지</li>
            <li>출발부터 도착까지 철저한 사진/문자 안심 브리핑</li>
            <li>프로 드라이버의 투철한 책임 안전 의식</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 5. 탁송 접수 방법 안내
st.markdown("""
<div class="glass-card">
    <div class="section-header">📋 탁송 접수 절차</div>
    <p style="color: #E2E8F0; font-size: 0.95rem; margin: 0; line-height: 1.6; font-weight: 500;">
        <b>1단계:</b> 아래 폼에 차량 정보(차종, 번호, 유종, 변속기)와 출발·도착지를 입력해 주세요.<br>
        <b>2단계:</b> 접수 내용 확인 즉시 안전 운행 가능 여부와 함께 신속하게 연락을 드립니다.<br>
        <b>3단계:</b> 목적지까지 흠집 없이 안전하고 완벽하게 인도해 드립니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 6. 실시간 탁송 접수 폼
st.markdown('<div class="section-header" style="margin-top: 20px;">✍️ 간편 탁송 접수하기</div>', unsafe_allow_html=True)

with st.form("toksong_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        car_model = st.text_input("차종", placeholder="예: 그랜저 / 2024년식")
    with col_b:
        car_number = st.text_input("차량 번호", placeholder="예: 123가 4567")
        
    # 유종 및 변속기 선택
    col_e, col_f = st.columns(2)
    with col_e:
        fuel_type = st.radio("유종 선택", ["휘발유(가솔린)", "경유(디젤)", "LPG", "전기(EV)/하이브리드"], horizontal=True)
    with col_f:
        transmission = st.radio("변속기 선택", ["오토", "스틱(수동)"], horizontal=True)
        
    col_c, col_d = st.columns(2)
    with col_c:
        departure = st.text_input("출발지", placeholder="예: 서울 강남구 / 상세 주소")
    with col_d:
        destination = st.text_input("도착지", placeholder="예: 부산 해운대구 / 상세 주소")
        
    phone_number = st.text_input("연락처 (휴대폰 번호)", placeholder="010-0000-0000")
    memo = st.text_area("요청 및 특이사항 (선택)", placeholder="경유지나 특별히 요청하실 사항을 적어주세요.")
    
    submitted = st.form_submit_button("🚀 탁송 신청 및 접수하기")
    
    if submitted:
        if departure and destination and phone_number and car_number:
            st.success("🎉 탁송 접수가 정상적으로 완료되었습니다! 확인 후 빠르게 연락드리겠습니다.")
        else:
            st.error("⚠️ 필수 항목(차량번호, 출발지, 도착지, 연락처)을 모두 입력해 주세요.")

# 푸터
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.85rem; margin-top: 25px; font-weight: 500;">
    © 2026 후미남(HUMINAM). All Rights Reserved. | sns7.kr
</div>
""", unsafe_allow_html=True)
