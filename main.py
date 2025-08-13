import streamlit as st

# MBTI별 반응 데이터
mbti_data = {
    "INTJ": {
        "stress": "논리적으로 상황을 분석하려 하지만, 혼자 고립되려는 경향이 강해짐.",
        "rest": "혼자만의 시간과 책, 전략적인 계획 세우기를 즐김."
    },
    "INFP": {
        "stress": "감정이 쉽게 소모되고, 주변의 부정적인 분위기에 민감하게 반응함.",
        "rest": "좋아하는 음악이나 글쓰기, 혼자만의 사색 시간으로 회복."
    },
    "ENTP": {
        "stress": "쉽게 지루해하고, 불필요한 논쟁이나 새로운 자극을 찾아 헤맴.",
        "rest": "친구들과 아이디어 브레인스토밍, 새로운 프로젝트 시작."
    },
    "ESFJ": {
        "stress": "사람들의 기대에 부응하지 못할까 봐 불안해하고, 과도하게 배려하려 함.",
        "rest": "가족·친구와의 따뜻한 대화와 소소한 취미 활동."
    },
    # 필요한 만큼 MBTI 유형 추가
}

# 앱 제목
st.title("MBTI별 스트레스 & 휴식 반응 보기")

# 설명
st.write("MBTI를 선택하면 스트레스 받을 때와 쉴 때의 특징을 보여줍니다.")

# MBTI 선택
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 선택 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 스트레스 받을 때")
    st.write(mbti_data[selected_mbti]["stress"])

    st.subheader(f"🌿 {selected_mbti} 쉴 때")
    st.write(mbti_data[selected_mbti]["rest"])

