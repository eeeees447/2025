import streamlit as st
from PIL import Image

# 앱 기본 설정
st.set_page_config(page_title="AI 패션 스타일링", page_icon="👔", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #FF6F61;'>👕 AI 패션 스타일링 👖</h1>
    <p style='text-align: center; color: gray;'>상의 색상과 형태에 따라 어울리는 바지를 추천해드립니다!</p>
""", unsafe_allow_html=True)

# 상의 색상 옵션
colors = [
    "검은색", "흰색", "회색", "네이비", "아이보리", "베이지",
    "카키", "진밤색", "분홍색", "연청", "다크그린"
]

# 상의 형태 옵션
styles = [
    "라운드 티셔츠", "브이넥 티셔츠", "셔츠", "맨투맨", "후드티", "니트", "가디건", "블레이저"
]

# 유저 입력
col1, col2 = st.columns(2)
with col1:
    top_color = st.selectbox("상의 색상을 선택하세요", colors)
with col2:
    top_style = st.selectbox("상의 형태를 선택하세요", styles)

# 추천 바지 로직
def recommend_pants(color, style):
    if color == "검은색":
        return ["연청 데님", "아이보리 치노", "그레이 슬랙스", "카키 팬츠", "다크 네이비"]
    elif color == "흰색":
        return ["연청 데님", "베이지 치노", "카키 팬츠", "검은 슬랙스"]
    elif color == "회색":
        return ["검은 슬랙스", "네이비 팬츠", "아이보리 치노"]
    elif color == "네이비":
        return ["연청 데님", "흰색 치노", "그레이 슬랙스"]
    elif color == "분홍색":
        return ["흰색 치노", "연청 데님", "회색 팬츠"]
    elif color == "진밤색":
        return ["아이보리 치노", "베이지 팬츠", "카키 팬츠"]
    else:
        return ["검은 슬랙스", "연청 데님", "베이지 치노"]

# 결과 출력
recommended = recommend_pants(top_color, top_style)

st.markdown(f"""
    <div style='text-align: center; padding:20px;'>
        <h2 style='color:#4A90E2;'>추천 스타일</h2>
        <p><b>{top_color}</b> {top_style}에는 아래 바지가 잘 어울려요 👇</p>
        <h3 style='color:#FF6F61;'>{', '.join(recommended)}</h3>
    </div>
""", unsafe_allow_html=True)

# 이미지 예시 (선택적으로 추가)
st.image("https://i.imgur.com/7Vqk7Qv.png", caption="스타일 예시", use_column_width=True)
