import streamlit as st
from PIL import Image
import random

# -------- Page Config --------
st.set_page_config(
    page_title="상의-바지 스타일 추천", page_icon="👖", layout="wide"
)

# --------- Custom CSS (Glow + Gradient + Card) ---------
st.markdown(
    """
    <style>
    @keyframes floaty { 0%{transform: translateY(0px)} 50%{transform: translateY(-6px)} 100%{transform: translateY(0px)} }
    
    .app-gradient {
        background: radial-gradient(1200px 500px at 10% -10%, #fbe9d7 0%, transparent 40%),
                    radial-gradient(1000px 600px at 90% 0%, #e1f3ff 0%, transparent 45%),
                    linear-gradient(180deg, #ffffff 0%, #f6f9fc 100%);
        padding: 12px 0 24px 0;
    }
    .title-wrap {text-align:center;}
    .subtitle {color:#6B7280; margin-top:-10px}
    
    .glass-card {
        backdrop-filter: blur(8px);
        background: rgba(255,255,255,0.6);
        border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-radius: 18px; padding: 18px 22px; margin-bottom: 14px;
        transition: transform .2s ease, box-shadow .2s ease;
    }
    .glass-card:hover { transform: translateY(-2px); box-shadow: 0 14px 40px rgba(0,0,0,0.12) }
    
    .chip { display:inline-flex; align-items:center; gap:8px; padding:6px 12px; border-radius:999px; border:1px solid rgba(0,0,0,.06); background:#fff; box-shadow:0 2px 8px rgba(0,0,0,.05); font-size:13px }
    .chip b { font-weight:600 }
    .swatch { width:16px; height:16px; border-radius:4px; border:1px solid rgba(0,0,0,.1)}
    
    .result-card { text-align:center; padding: 22px; border-radius: 20px; background: linear-gradient(145deg,#ffffff,#f1f5f9); border:1px solid rgba(0,0,0,.06) }
    .result-title { margin:0; color:#111827 }
    .result-sub { color:#4B5563 }
    
    .badge {display:inline-block; padding:6px 10px; border-radius:10px; background:#eef2ff; border:1px solid #e5e7eb; font-size:12px; margin-right:6px}
    
    .hint { color:#6B7280; font-size:13px }
    </style>
    <div class="app-gradient">
        <div class="title-wrap">
            <h1>👕👖 상의 색상 & 형태에 따른 바지 스타일 추천</h1>
            <p class="subtitle">팔레트에서 고르고, 버튼을 누르면 바로 코디 제안이 떠요 ✨</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------- Color Palette (hex for swatches) ---------
COLOR_HEX = {
    "화이트":"#FFFFFF", "아이보리":"#EEE9DD", "베이지":"#D8C7A3", "라이트 그레이":"#D9DDE3", "차콜":"#42464D",
    "블랙":"#111111", "네이비":"#1F3254", "스카이블루":"#A5C8FF", "카키":"#6B7D57", "올리브":"#556B2F",
    "머스타드 옐로우":"#D4A70A", "버건디 레드":"#7A1E2D", "진밤색":"#4B2E2B", "라이트 핑크":"#F7B2C4",
    "분홍색":"#FF6FA0", "민트":"#98E5D0", "라벤더":"#C6B7F2"
}

# --------- Sidebar (Quick info) ---------
with st.sidebar:
    st.markdown("### 🌟 스타일 옵션")
    st.caption("색상은 미리 정의된 팔레트로 추천 정확도가 높아요.")
    st.markdown("""
    <div class="glass-card">
        <div class="chip"><span class="swatch" style="background:#1F3254"></span> <b>네이비</b>는 만능 베이스</div><br>
        <div class="chip"><span class="swatch" style="background:#D8C7A3"></span> <b>베이지</b>는 부드러운 톤온톤</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("#### 🔎 팁")
    st.write("• 상의가 강한 색이면 바지는 뉴트럴 톤으로 밸런스 맞추기")
    st.write("• 실루엣은 한쪽만 와이드: 오버 상의 × 슬림 하의 or 반대로!")

# --------- Layout ---------
left, right = st.columns([1.1, 1.2], gap="large")

with left:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    color = st.selectbox(
        "🎨 상의 색상을 선택하세요",
        list(COLOR_HEX.keys()),
        index=list(COLOR_HEX.keys()).index("화이트")
    )
    shape = st.radio(
        "👔 상의 형태를 선택하세요",
        ["티셔츠", "셔츠", "후드", "니트", "자켓", "블레이저", "맨투맨", "가디건"],
        horizontal=True
    )
    st.markdown(
        f"""
        <div class='chip'>
            <span class='swatch' style='background:{COLOR_HEX[color]}'></span>
            선택한 색상: <b>{color}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("추가 옵션 (선택)")
    fit = st.select_slider("바지 핏 선호", options=["스키니", "슬림", "스트레이트", "와이드"], value="스트레이트")
    vibe = st.multiselect("무드 태그", ["미니멀", "댄디", "스트릿", "캐주얼", "세미포멀"]) 
    st.markdown("</div>", unsafe_allow_html=True)

    go = st.button("✨ 스타일 추천 받기 ✨", use_container_width=True)

# --------- Recommendation Logic ---------

def recommend_pants(color, shape, fit):
    # Base rules from color & shape
    if color in ["화이트", "아이보리", "베이지"]:
        if shape in ["셔츠", "블레이저", "가디건"]:
            base = "네이비 슬림핏 슬랙스"
        elif shape == "티셔츠":
            base = "라이트 블루 스트레이트 데님"
        elif shape == "맨투맨":
            base = "빈티지 워시 데님"
        else:
            base = "샌드 베이지 와이드 치노"
    elif color in ["블랙", "차콜", "네이비", "진밤색"]:
        if shape == "후드":
            base = "라이트 그레이 조거"
        elif shape == "니트":
            base = "헤링본/체크 슬랙스"
        elif shape == "맨투맨":
            base = "블랙 카고 팬츠"
        else:
            base = "다크 인디고 데님"
    elif color in ["버건디 레드", "머스타드 옐로우", "라이트 핑크", "분홍색", "라벤더", "민트"]:
        if shape == "티셔츠":
            base = "블랙 스키니/슬림 진"
        elif shape == "맨투맨":
            base = "오프화이트 와이드 팬츠"
        else:
            base = "화이트 크롭 슬랙스"
    elif color in ["카키", "올리브"]:
        if shape == "자켓":
            base = "초콜릿 브라운 치노"
        elif shape == "가디건":
            base = "아이보리 슬랙스"
        else:
            base = "아이보리 와이드 팬츠"
    else:
        base = "클래식 블루 데님"

    # Adjust by fit slider
    mapping = {
        "스키니": ["스키니", "테이퍼드"],
        "슬림": ["슬림", "테이퍼드"],
        "스트레이트": ["스트레이트"],
        "와이드": ["와이드", "릴랙스드"],
    }
    suffix = random.choice(mapping.get(fit, [""]))
    if suffix not in base:
        rec = f"{base} ({suffix})" if suffix else base
    else:
        rec = base
    return rec


def accessorize(color, shape):
    shoes = {
        "티셔츠": "로우탑 스니커즈",
        "셔츠": "로퍼 / 더비슈즈",
        "블레이저": "로퍼 / 첼시부츠",
        "자켓": "첼시부츠 / 더비",
        "후드": "청키 스니커즈",
        "맨투맨": "캔버스 스니커즈",
        "니트": "클래식 로퍼",
        "가디건": "스웨이드 로퍼",
    }.get(shape, "스니커즈")

    belt = "가죽 벨트 (다크브라운)" if color in ["아이보리", "베이지", "카키", "올리브", "진밤색"] else "블랙 레더 벨트"
    bag = "크로스백" if shape in ["티셔츠", "후드", "맨투맨"] else "토트백"
    return shoes, belt, bag

# --------- Output ---------
with right:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 미리보기")
    st.markdown(
        f"""
        <div class='chip'>
            <span class='swatch' style='background:{COLOR_HEX[color]}'></span>
            상의: <b>{color}</b>
        </div>
        <span class='badge'>{shape}</span>
        <span class='badge'>선호 핏: {fit}</span>
        """, unsafe_allow_html=True,
    )

    if go:
        pants = recommend_pants(color, shape, fit)
        shoes, belt, bag = accessorize(color, shape)
        st.balloons()
        st.markdown(
            f"""
            <div class='result-card'>
                <h3 class='result-title'>💡 추천 결과</h3>
                <p class='result-sub'>
                    <b>{color}</b> <b>{shape}</b>에는<br>
                    <span style='font-size:20px'><b>{pants}</b></span> 가 잘 어울려요.
                </p>
                <div class='hint'>밸런스 팁: 상의가 볼드하면 하의는 뉴트럴/텍스처로 정리</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("##### 🧩 매치 아이템")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<div class='glass-card'><b>신발</b><br>{shoes}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='glass-card'><b>벨트</b><br>{belt}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='glass-card'><b>가방</b><br>{bag}</div>", unsafe_allow_html=True)

        with st.expander("🔧 코디 디테일 팁"):
            st.write("• 상의가 파스텔이면 바지는 화이트/그레이 톤으로 묶기")
            st.write("• 체크 슬랙스는 상의를 솔리드 컬러로 깔끔하게")
            st.write("• 카고/조거는 상의 프린트 크기를 작게 해서 과함 방지")

    else:
        st.markdown("<div class='hint'>왼쪽에서 옵션을 고르고 버튼을 눌러보세요!</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.caption("© 스타일 추천 데모 · Streamlit")
