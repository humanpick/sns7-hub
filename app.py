import streamlit as st

# 1. 페이지 설정 (제로스크롤 & 와이드 레이아웃 최적화)
st.set_page_config(
    page_title="후미남 | sns7.kr 통합 허브",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Humanpick 디자인 시스템 CSS 적용 (다크모드, 글래스모피즘, Pretendard)
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    * {
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 전체 배경 네이비 고정 및 스크롤 방지 */
    .stApp {
        background-color: #0B1120;
        color: #FFFFFF;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* 상하단 불필요한 공백 및 메뉴 숨기기 */
    header, footer {visibility: hidden;}
    
    /* 글래스모피즘 카드 스타일 */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        text-align: center;
    }
    
    /* 타이포그래피 강조 */
    .brand-title {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #8B5CF6, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    .brand-subtitle {
        font-size: 0.95rem;
        color: #94A3B8;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    
    /* 커스텀 버튼 스타일 */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #8B5CF6, #6366F1);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 20px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. 메인 콘텐츠 영역 (제로스크롤 원페이지 뷰)
st.markdown("<br>", unsafe_allow_html=True)

# 헤더 & 브랜드 철학 카드
st.markdown("""
<div class="glass-card">
    <div class="brand-title">후미남 : 후회 없는 미소를 짓는 남자</div>
    <div class="brand-subtitle">
        "후각과 미각은 잃었지만, 삶을 향한 감각은 선명합니다.<br>
        요란한 말 대신, 꺾이지 않는 진정성과 행동으로 증명합니다."
    </div>
</div>
""", unsafe_allow_html=True)

# 핵심 서비스 및 정보 연결 게이트웨이 (배너형 카드들)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <h3 style="color: #38BDF8; font-size: 1.2rem; margin-bottom: 8px;">🚗 프리미엄 로드탁송</h3>
        <p style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 12px;">비흡연·장거리 전문, 철저한 차량 검수 및 안심 브리핑 서비스</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("탁송 신청 및 가이드 바로가기"):
        # 외부/서브 사이트 연결 (quote 적용 및 새창 열기 표준)
        st.markdown('<script>window.open("https://car.sns7.kr", "_blank");</script>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="min-height: 180px; display: flex; flex-direction: column; justify-content: center;">
        <h3 style="color: #EC4899; font-size: 1.2rem; margin-bottom: 8px;">💼 CEO포털 & 비즈니스</h3>
        <p style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 12px;">소상공인 운영 지원 솔루션 및 맞춤 리스크 관리(보험) 허브</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("비즈니스 파트너십 보기"):
        st.markdown('<script>window.open("https://ceo.sns7.kr", "_blank");</script>', unsafe_allow_html=True)

# 하단 푸터 노트
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.8rem; margin-top: 20px;">
    © 2026 후미남(HUMINAM). All Rights Reserved. | sns7.kr
</div>
""", unsafe_allow_html=True)
