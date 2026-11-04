import streamlit as st
import datetime

# 1. 페이지 설정 (와이드 레이아웃, 사이드바 숨김)
st.set_page_config(
    page_title="후미남 시그니처 Road Delivery & 대리운전",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Humanpick 디자인 시스템 CSS 적용 (가독성 및 이미지 카드 스타일링)
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
    
    /* 입력창 위의 라벨 글자 색상 및 크기 선명하게 강제 수정 */
    .stTextInput label, .stRadio label, .stSelectbox label, .stTextArea label, .stDateInput label, .stTimeInput label {
        color: #F8FAFC !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }
    
    /* 화이트 폼 입력창 스타일 (순백색 배경, 검은색 볼드체 텍스트) */
    .stTextInput input, .stSelectbox select, .stTextArea textarea, .stDateInput input, .stTimeInput input {
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

# 3. 헤더 및 감성 이미지 배너 섹션
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="glass-card" style="text-align: center;">
    <div class="hero-title">후미남 시그니처 Road Delivery & 대리운전</div>
    <p style="color: #CBD5E1; font-size: 1rem; line-height: 1.5; margin-bottom: 0;">
        "화려한 수식어 대신, 꺾이지 않는 진정성과 행동으로 증명합니다."<br>
        <span style="color: #38BDF8; font-weight: 600; font-size: 0.9rem;">100% 비흡연 · 철저한 안심 브리핑 · 프리미엄 맞춤 운행</span>
    </p>
</div>
""", unsafe_allow_html=True)

# 상업적 이용 가능한 무료 고화질 자동차 주행 감성 이미지
st.image(
    "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80",
    caption="안전과 신뢰를 싣고 목적지까지 완벽하게 이동합니다.",
    use_container_width=True
)

# 4. 로드탁송(Road Delivery)이란? 개념 설명 섹션
st.markdown("""
<div class="glass-card" style="margin-top: 16px;">
    <div class="section-header">📌 로드탁송(Road Delivery)이란?</div>
    <p style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6; margin: 0; font-weight: 400;">
        <b>로드탁송(Road Delivery)</b>은 숙련된 전문 프로 드라이버가 고객님의 차량에 직접 탑승하여 출발지부터 목적지까지 안전하게 운전하여 이동시키는 차량 탁송 서비스입니다. 중고차/신차 거래, 장거리 이동, 법인 차량 탁송 등 캐리어 트럭 진입이 어렵거나 신속·안전한 직접 운행이 필요할 때 가장 확실한 선택입니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. 왜 나에게 맡겨야 하는지 & 서비스 특징
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="min-height: 220px;">
        <div class="section-header">🚗 이런 분께 필요합니다</div>
        <ul style="color: #F1F5F9; font-size: 0.9rem; padding-left: 15px; margin: 0; line-height: 1.7; font-weight: 500;">
            <li>자동차 거래 후 안전하게 탁송이 필요할 때</li>
            <li>술자리나 야간 일정 후 안전한 대리운전이 필요할 때</li>
            <li>장거리 이동 및 지방 출장으로 운행이 부담될 때</li>
            <li>법인 차량 및 중요한 차량을 믿고 맡길 기사가 필요할 때</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="min-height: 220px;">
        <div class="section-header">🛡️ 왜 후미남인가?</div>
        <ul style="color: #F1F5F9; font-size: 0.9rem; padding-left: 15px; margin: 0; line-height: 1.7; font-weight: 500;">
            <li><b>100% 비흡연 운행 원칙</b>으로 쾌적한 실내 유지</li>
            <li>출발부터 도착까지 철저한 사진/문자 안심 브리핑</li>
            <li>시련을 딛고 일어선 프로 드라이버의 책임 안전 의식</li>
            <li>철저한 배상 책임 보험 가입 완비</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 6. 접수 방법 및 배차 안내 (대체 기사 안내 문구 반영)
st.markdown("""
<div class="glass-card">
    <div class="section-header">📋 서비스 접수 절차</div>
    <p style="color: #E2E8F0; font-size: 0.95rem; margin: 0 0 12px 0; line-height: 1.6; font-weight: 500;">
        <b>1단계:</b> 아래 폼에서 서비스 종류(탁송/대리) 및 차량 정보, 희망 일시를 선택해 주세요.<br>
        <b>2단계:</b> 출발지 및 도착지를 입력하고 접수해 주시면 즉시 확인 연락을 드립니다.<br>
        <b>3단계:</b> 목적지까지 흠집 없이 안전하고 완벽하게 모셔다 드립니다.
    </p>
    <div style="background: rgba(56, 189, 248, 0.1); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 6px; margin-top: 10px;">
        <p style="color: #38BDF8; font-size: 0.88rem; margin: 0; line-height: 1.5; font-weight: 600;">
            💡 <b>배차 안심 안내:</b> 예약이 밀려있거나 출발/목적지가 멀고 외진 지역인 경우, 동일하게 엄선된 <b>100% 비흡연 전문 협력 기사님</b>으로 대체 배차될 수 있습니다. 어떠한 경우에도 쾌적함과 안전을 최우선으로 지켜드립니다.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. 실시간 간편 접수 폼 (탁송 & 대리 통합)
st.markdown('<div class="section-header" style="margin-top: 20px;">✍️ 간편 서비스 접수하기</div>', unsafe_allow_html=True)

with st.form("service_form"):
    service_type = st.radio("신청 서비스 종류", ["로드탁송 (Road Delivery)", "대리운전"], horizontal=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        car_model = st.text_input("차종", placeholder="예: 그랜저 / 2024년식")
    with col_b:
        car_number = st.text_input("차량 번호", placeholder="예: 123가 4567")
        
    col_e, col_f = st.columns(2)
    with col_e:
        fuel_type = st.radio("유종 선택", ["휘발유(가솔린)", "경유(디젤)", "LPG", "전기(EV)/하이브리드"], horizontal=True)
    with col_f:
        transmission = st.radio("변속기 선택", ["오토", "스틱(수동)"], horizontal=True)
        
    col_date, col_time = st.columns(2)
    with col_date:
        pickup_date = st.date_input("희망 날짜", value=datetime.date.today())
    with col_time:
        pickup_time = st.time_input("희망 시간", value=datetime.time(20, 0))

    col_c, col_d = st.columns(2)
    with col_c:
        departure = st.text_input("출발지", placeholder="예: 서울 강남구 / 상세 주소")
    with col_d:
        destination = st.text_input("도착지", placeholder="예: 경기도 광주시 / 상세 주소")
        
    phone_number = st.text_input("연락처 (휴대폰 번호)", placeholder="010-0000-0000")
    memo = st.text_area("요청 및 특이사항 (선택)", placeholder="경유지나 특별히 요청하실 사항을 적어주세요.")
    
    submitted = st.form_submit_button("🚀 서비스 신청 및 접수하기")
    
    if submitted:
        if departure and destination and phone_number and car_number:
            st.success(f"🎉 [{service_type}] 접수가 정상적으로 완료되었습니다! ({pickup_date} {pickup_time.strftime('%H:%M')}) 확인 후 빠르게 연락드리겠습니다.")
        else:
            st.error("⚠️ 필수 항목(차량번호, 출발지, 도착지, 연락처)을 모두 입력해 주세요.")

# 푸터
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.85rem; margin-top: 25px; font-weight: 500;">
    © 2026 후미남(HUMINAM). All Rights Reserved. | sns7.kr
</div>
""", unsafe_allow_html=True)
