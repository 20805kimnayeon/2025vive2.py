import streamlit as st
import random

# 캐릭터 대화 시나리오 직접 포함
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
                },
                {
                    "question": "💬 대화 주제를 골라줘!",
                    "options": {
                        "최근에 본 영화 이야기": [
                            ("나는 감동 영화 좋아해~ 울보라서 😢", +1),
                            ("영화관 가는 거 진짜 좋아해! 다음에 같이 가자~ 🎬", +2)
                        ],
                        "게임 얘기!": [
                            ("어머~ 나도 게임 좋아해! 같이 할래? 🎮", +2),
                            ("그건 잘 몰라서... 😅", -1)
                        ]
                    }
                },
                {
                    "question": "🍰 디저트 뭐 먹을래?",
                    "options": {
                        "딸기 케이크!": [
                            ("딸기 또 나왔어!! 완전 내 스타일~ 🍰💘", +2),
                            ("달콤한 거 먹으면 기분 좋아지지~ 😊", +1)
                        ],
                        "치즈케이크!": [
                            ("치즈는... 루비랑 잘 안 맞는 느낌이야 🤢", -1),
                            ("치즈도 괜찮긴 하지! 😋", +1)
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
                },
                {
                    "question": "💬 어떤 얘기를 할까?",
                    "options": {
                        "요즘 힘들었던 이야기": [
                            ("...그런 말은 나한테만 해. 남들한텐 하지 마. 🫢", +2),
                            ("듣는 건 귀찮지만, 뭐... 네 이야기니까. 🙃", +1)
                        ],
                        "가벼운 농담!": [
                            ("...흥. 유치하군. 근데 좀 웃겼다. 😏", +1),
                            ("...흥미 없어. 🙄", -1)
                        ]
                    }
                },
                {
                    "question": "🍰 디저트를 골라줘.",
                    "options": {
                        "초코 케이크": [
                            ("...달달하군. 네가 주면 먹어줄게. 🍫", +2),
                            ("음... 그렇게 달콤한 걸 좋아해?", +1)
                        ],
                        "쿠키": [
                            ("이건 별로야. 다음엔 다른 걸 고르자. 😑", -1),
                            ("괜찮군. 딱히 나쁘진 않네. 🍪", +1)
                        ]
                    }
                }
            ]
        }
    }
}

# Streamlit UI 설정
st.set_page_config(page_title="AI 친구와 데이트하기 💘", page_icon="💘", layout="wide")

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

st.markdown("<div class='title'>💘 AI 친구와 데이트하기! 귀엽고 심쿵한 시간을 즐겨요 💘</div>", unsafe_allow_html=True)

username = st.text_input("닉네임을 입력해주세요 💬")
place = st.selectbox("데이트 장소를 골라주세요 🎡", ["카페"])  # 지금은 '카페'만 있음
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
        choice = st.radio("선택지 중 하나를 골라보세요:", list(scene["options"].keys()), key=scene["question"])
        reaction, delta = random.choice(scene["options"][choice])
        st.write(f"🗣️ {character_name}: {reaction}")
        score += delta

    st.write("---")
    st.subheader("🎀 데이트 결과 💌")
    if score >= 6:
        st.success(f"{character_name}이(가) 고백했어요! 💍 ")
    elif score >= 3:
        st.info("우리 친구로 지내요~ 🤝")
    else:
        st.error("앗... 다음에 다시 시도해봐요 💔")
