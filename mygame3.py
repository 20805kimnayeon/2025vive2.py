import streamlit as st
import random

# 캐릭터 시나리오 포함
characters = {
    "루비": {
        "emoji": "💖",
        "image": "assets/ruby.gif",
        "personality": "활발하고 엉뚱함",
        "location_scenarios": {
            "카페": [
                {
                    "question": "☕ 어떤 음료를 마실까?",
                    "options": {
                        "딸기 라떼! 달콤한 게 최고야!": [
                            ("꺄~ 딸기 완전 좋아해! 🍓", +2),
                            ("나도 딸기 좋아해~ 찰떡궁합이네? 💕", +1),
                            ("음... 너무 달지 않을까? 🙄", -1)
                        ],
                        "아이스 아메리카노!": [
                            ("헉... 루비는 쓴 거 못 마셔 😵", -1),
                            ("멋지다~ 어른 같은 느낌이야! 😳", +1)
                        ]
                    }
                }
            ]
        }
    },
    "제로": {
        "emoji": "🧊",
        "image": "assets/zero.gif",
        "personality": "차가운 츤데레, 무뚝뚝하지만 가끔 귀여움",
        "location_scenarios": {
            "카페": [
                {
                    "question": "☕ 어떤 음료를 마실까?",
                    "options": {
                        "딸기 라떼!": [
                            ("...달달하군. 너랑 어울려. 🙄", +1),
                            ("그런 유치한 음료를 고르다니. ...그래도 귀엽다. 😒", +2)
                        ],
                        "아이스 아메리카노": [
                            ("흠. 나랑 취향이 비슷하군. ☕", +2),
                            ("그거 쓰지 않나...? 너 좀 의외다. 😐", +1)
                        ]
                    }
                }
            ]
        }
    }
}

# 페이지 설정
st.set_page_config(page_title="AI 친구와 데이트하기 💘", page_icon="💘", layout="wide")

# 스타일
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .title {
        font-size: 40px;
        text-align: center;
        color: #ff69b4;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💘 AI 친구와 데이트하기 💘</div>", unsafe_allow_html=True)

# 사용자 입력
username = st.text_input("닉네임을 입력해주세요 💬")
place = st.selectbox("데이트 장소를 골라주세요 🎡", ["카페"])
st.image("assets/background.jpg", use_column_width=True)

if st.button("✨ AI 캐릭터 선택하기!"):
    character_name = random.choice(list(characters.keys()))
    character = characters[character_name]

    st.subheader(f"💘 오늘 데이트 상대는: {character_name} {character['emoji']}")
    st.image(character["image"], width=300)
    st.markdown(f"**성격:** {character['personality']}")

    score = 0
    for scene in character["location_scenarios"][place]:
        st.write("---")
        st.write(scene["question"])
        choice = st.radio("선택지를 골라보세요:", list(scene["options"].keys()), key=scene["question"])
        reaction, delta = random.choice(scene["options"][choice])
        st.write(f"🗣️ {character_name}: {reaction}")
        score += delta

    st.write("---")
    st.markdown("<div class='title'>🎉 게임 종료! 결과 발표 💌</div>", unsafe_allow_html=True)
    if score >= 6:
        st.success(f"{character_name}이(가) 고백했어요! 💍 ")
    elif score >= 3:
        st.info("우리 친구로 지내요~ 🤝")
    else:
        st.error("앗... 다음에 다시 시도해봐요 💔")
