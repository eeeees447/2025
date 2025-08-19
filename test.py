import streamlit as st
from PIL import Image

# 앱 제목
st.markdown("""
    <h1 style='text-align: center; color: #2C3E50;'>👕👖 상의 색상 & 형태에 따른 바지 스타일 추천</h1>
    <p style='text-align: center; color: #7F8C8D;'>나만의 스타일을 찾아보세요 ✨</p>
""", unsafe_allow_html=True)

# 상의 색상 선택 (더 구체화)
color = st.selectbox(
    "상의 색상을 선택하세요",
    ["화이트", "아이보리", "베이지", "라이트 그레이", "차콜", "블랙", "네이비", "스카이블루", "카키", "올리브", "머스타드 옐로우", "버건디 레드", "라이트 핑크", "민트", "라벤더"]
)

# 상의 형태 선택
shape = st.radio(
    "상의 형태를 선택하세요",
    ["티셔츠", "셔츠", "후드", "니트", "자켓", "블레이저", "폴로 셔츠"],
    horizontal=True
)

# 추천 로직
def recommend_pants(color, shape):
    if color in ["화이트", "아이보리", "베이지"]:
        if shape in ["셔츠", "블레이저"]:
            return "슬림핏 네이비 슬랙스"
        elif shape == "티셔츠":
            return "라이트 블루 청바지"
        else:
            return "베이지 와이드 팬츠"
    elif color in ["블랙", "차콜", "네이비"]:
        if shape == "후드":
            return "그레이 조거 팬츠"
        elif shape == "니트":
            return "체크 패턴 슬랙스"
        else:
            return "다크 블루 데님 팬츠"
    elif color in ["버건디 레드", "머스타드 옐로우", "라이트 핑크", "라벤더", "민트"]:
        if shape == "티셔츠":
            return "블랙 스키니 진"
        else:
            return "화이트 크롭 팬츠"
    elif color in ["카키", "올리브"]:
        if shape == "자켓":
            return "브라운 치노 팬츠"
        else:
            return "아이보리 와이드 팬츠"
    else:
        return "기본 데님 팬츠"

# 버튼 및 결과 출력
if st.button("✨ 스타일 추천 받기 ✨"):
    pants = recommend_pants(color, shape)
    st.markdown(f"""
        <div style='text-align: center; padding: 20px; background-color: #ECF0F1; border-radius: 15px;'>
            <h3 style='color:#2C3E50;'>💡 추천 결과</h3>
            <p style='font-size:18px;'> <b>{color}</b> <b>{shape}</b> 에는 👉 <b style='color:#27AE60;'>{pants}</b> 가 잘 어울립니다!</p>
        </div>
    """, unsafe_allow_html=True)

