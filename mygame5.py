import streamlit as st
import random

# 캐릭터 시나리오
characters = {
    "루비": {
        "emoji": "💖",
        "personality": "활발하고 엉뚱함",
        "location_scenarios": {
            "카페": [
                {
                    "question": "☕ 어떤 음료를 마실까?",
                    "options": {
                        "딸기 라떼! 달콤한 게 최고야!": [("꺄~ 딸기 완전 좋아해! 🍓", +2)],
                        "아이스 아메리카노!": [("멋지다~ 어른 같은 느낌이야! 😳", +1)],
                        "바닐라 라떼": [("나도 그거 좋아해~ 💕", +1)],
                        "핫초코": [("달콤한 거 좋아하는구나~ ☕", +2)]
                    }
                },
                {
                    "question": "📚 무슨 대화를 해볼까?",
                    "options": {
                        "요즘 본 영화 이야기": [("재밌겠다~ 다음에 같이 보자! 🎬", +2)],
                        "최근 고민 나누기": [("그랬구나... 루비가 들어줄게 💕", +1)],
                        "좋아하는 음악 얘기": [("헐 나도 그 가수 좋아해! 🎶", +2)],
                        "날씨 얘기": [("오늘 날씨 진짜 좋다~ 산책가자! ☀️", +1)]
                    }
                }
            ],
            "공원": [
                {
                    "question": "🌳 공원에서 뭐할까?",
                    "options": {
                        "산책하자~": [("기분 상쾌해~ 바람 좋아! 🍃", +1)],
                        "벤치에 앉아서 얘기하자": [("편안하다~ 이야기도 잘 통하네 😌", +2)],
                        "뛰어놀자!": [("헉 체력 짱이다! 😆", +1)],
                        "사진 찍자": [("인생샷 각! 📸", +2)]
                    }
                }
            ],
            "식당": [
                {
                    "question": "🍽️ 뭐 먹을까?",
                    "options": {
                        "김치찌개": [("국물 진짜 시원하다~! 😋", +2)],
                        "스파게티": [("이탈리안 무드~ 🍝", +1)],
                        "초밥": [("회 좋아하는구나! 🐟", +2)],
                        "햄버거": [("패스트푸드도 좋지! 🍔", +1)]
                    }
                }
            ]
        }
    }
}

# Streamlit 설정
st.set_page_config(page_title="AI 친구와 데이트하기 💘", page_icon="💘")
st.title("💘 AI 친구와 데이트하기 💘")

username = st.text_input("당신의 이름은?")
place = st.radio("데이트 장소를 골라주세요!", ["카페", "공원", "식당"])

if st.button("✨ AI 캐릭터 만나기!"):
    character_name = random.choice(list(characters.keys()))
    character = characters[character_name]
    st.subheader(f"오늘 데이트 상대는 {character_name} {character['emoji']}")
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
    if score >= 5:
        st.success(f"{character_name}이(가) 당신에게 반했어요! 💍")
    elif score >= 3:
        st.info(f"{character_name}과(와) 좋은 친구가 되었어요! 🤝")
    else:
        st.error(f"{character_name}은(는) 아직 어색한가봐요... 다음 기회에! 💔")
