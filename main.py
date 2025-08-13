import streamlit as st

# =========================
# MBTI 데이터
# =========================
mbti_data = {
    "INTJ": {
        "stress": "논리적으로 상황을 분석하려 하지만, 완벽주의로 인해 자기 비판이 심해지고 혼자 고립되려 함.",
        "rest": "혼자만의 독서, 미래 계획 세우기, 전략 게임 등으로 에너지 회복."
    },
    "INTP": {
        "stress": "과도한 분석으로 생각이 꼬이고, 현실적 행동이 늦어짐.",
        "rest": "철학적 사색, 혼자만의 취미, 지적 호기심을 충족하는 영상 시청."
    },
    "ENTJ": {
        "stress": "통제력을 잃는 상황에 예민하게 반응, 주변에 명령조로 대함.",
        "rest": "목표 재정비, 운동, 생산적인 프로젝트 계획."
    },
    "ENTP": {
        "stress": "쉽게 지루해하며, 불필요한 논쟁이나 자극을 찾아 헤맴.",
        "rest": "새로운 아이디어 실험, 친구와의 유쾌한 대화, 즉흥 여행."
    },
    "INFJ": {
        "stress": "사람들의 감정과 갈등에 지나치게 몰입하여 소모됨.",
        "rest": "명상, 글쓰기, 조용한 공간에서의 창작 활동."
    },
    "INFP": {
        "stress": "감정적으로 예민해지고, 혼자만의 상상 속에 빠져 현실 회피.",
        "rest": "좋아하는 음악 감상, 일기 쓰기, 의미 있는 콘텐츠 소비."
    },
    "ENFJ": {
        "stress": "모두를 만족시키려다 자신을 소홀히 함.",
        "rest": "가족·친구와 깊은 대화, 사람들과 함께하는 봉사 활동."
    },
    "ENFP": {
        "stress": "흥미가 급격히 떨어지고, 한 가지에 집중하기 어려움.",
        "rest": "창의적인 취미, 여행 계획, 새로운 사람 만나기."
    },
    "ISTJ": {
        "stress": "예상치 못한 변화에 불안해하며 계획에 집착.",
        "rest": "정리·청소, 규칙적인 일과, 익숙한 환경에서의 휴식."
    },
    "ISFJ": {
        "stress": "타인의 기대에 부응하지 못하면 죄책감을 느낌.",
        "rest": "소중한 사람과 조용히 시간 보내기, 홈카페."
    },
    "ESTJ": {
        "stress": "통제 불가능한 상황에 화가 나며, 다른 사람을 재촉.",
        "rest": "생산적인 취미, 규칙적인 운동, 목표 재설정."
    },
    "ESFJ": {
        "stress": "주변 평가에 지나치게 신경 쓰고 감정적으로 소모됨.",
        "rest": "따뜻한 대화, 소소한 파티, 가족과의 시간."
    },
    "ISTP": {
        "stress": "계속되는 간섭과 제한에 답답함을 느낌.",
        "rest": "혼자서 드라이브, 손으로 만드는 활동, 스포츠."
    },
    "ISFP": {
        "stress": "타인의 부정적 평가에 상처받고 의욕 저하.",
        "rest": "예술 활동, 자연 속 산책, 감각적인 취미."
    },
    "ESTP": {
        "stress": "지루하고 답답한 상황에 불안, 충동적으로 행동.",
        "rest": "즉흥 여행, 친구들과 액티비티, 게임."
    },
    "ESFP": {
        "stress": "주목받지 못하거나 자유가 제한될 때 힘들어함.",
        "rest": "음악과 춤, 사람들과의 즐거운 모임."
    }
}

# =========================
# Streamlit 앱
# =========================
st.set_page_config(page_title="MBTI 반응 분석기", page_icon="🧠", layout="centered")

# 헤더
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🧠 MBTI별 스트레스 & 휴식 반응</h1>", unsafe_allow_html=True)
st.write("---")

st.write("### MBTI를 선택하면 스트레스 받을 때와 쉴 때의 반응을 확인할 수 있습니다.")

# 선택 박스
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list, index=0)

# 결과 표시
if selected_mbti:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 😖 {selected_mbti} 스트레스 받을 때")
        st.markdown(f"<div style='background-color:#FFD6D6; padding:10px; border-radius:10px;'>{mbti_data[selected_mbti]['stress']}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"### 🌿 {selected_mbti} 쉴 때")
        st.markdown(f"<div style='background-color:#D6FFD9; padding:10px; border-radius:10px;'>{mbti_data[selected_mbti]['rest']}</div>", unsafe_allow_html=True)

# 하단 푸터
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 MBTI Reaction App | Made with ❤️ by Streamlit</p>", unsafe_allow_html=True)
