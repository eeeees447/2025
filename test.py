import streamlit as st

# 앱 제목
st.title("👕👖 상의 색상 & 형태에 따른 바지 스타일 추천")

st.write("원하는 상의 스타일을 선택하면 어울리는 바지를 추천해드립니다!")

# 상의 색상 선택
color = st.selectbox(
    "상의 색상을 선택하세요",
    ["화이트", "블랙", "네이비", "그레이", "레드", "옐로우", "그린", "베이지"]
)

# 상의 형태 선택
shape = st.selectbox(
    "상의 형태를 선택하세요",
    ["티셔츠", "셔츠", "후드", "니트", "자켓"]
)

# 추천 로직
def recommend_pants(color, shape):
    if color in ["화이트", "베이지"]:
        if shape == "셔츠":
            return "슬림핏 슬랙스"
        elif shape == "티셔츠":
            return "청바지"
        else:
            return "와이드 팬츠"
    elif color in ["블랙", "네이비", "그레이"]:
        if shape == "후드":
            return "조거 팬츠"
        elif shape == "니트":
            return "체크 슬랙스"
        else:
            return "데님 팬츠"
    elif color in ["레드", "옐로우", "그린"]:
        if shape == "티셔츠":
            return "블랙 진"
        else:
            return "화이트 팬츠"
    else:
        return "기본 청바지"

# 결과 출력
if st.button("스타일 추천 받기"):
    pants = recommend_pants(color, shape)
    st.success(f"{color} {shape}에는 👉 {pants}가 잘 어울립니다!")

