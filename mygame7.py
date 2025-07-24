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
                },
                {
                    "question": "🐶 갑자기 강아지가 다가왔다! 어떻게 할까?",
                    "options": {
                        "귀엽다고 쓰다듬기": [("나도 강아지 진짜 좋아해! 🐾", +2)],
                        "도망가기": [("으앗... 강아지가 무서운가봐...? 😥", -1)],
                        "주인에게 돌려주기": [("착하다~ 배려심 최고야! 😍", +1)],
                        "강아지와 셀카 찍기": [("헐ㅋㅋ 귀여워~ 같이 찍자! 🤳", +2)]
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
                },
                {
                    "question": "🍰 디저트는 뭘로 할까?",
                    "options": {
                        "딸기 케이크": [("딸기 또 나왔어~ 🍓 좋아!", +2)],
                        "빙수": [("시원하고 달콤~ 여름엔 최고지! 🍧", +2)],
                        "아이스크림": [("헉 맛있겠다~ 무슨 맛이야? 🍦", +1)],
                        "안 먹을래": [("어...? 아쉬워 😢", -1)]
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

proceed = st.button("✨ AI 캐릭터 만나기!")

if proceed:
    character_name = random.choice(list(characters.keys()))
    character = characters[character_name]
    st.subheader(f"오늘 데이트 상대는 {character_name} {character['emoji']}")
    st.markdown(f"**성격:** {character['personality']}")

    score = 0
    all_answered = True  # 모든 질문에 답했는지 여부 확인

    for idx, scene in enumerate(character["location_scenarios"][place]):
        st.write("---")
        st.write(scene["question"])
        choice = st.radio(
            "선택지를 골라보세요:", 
            list(scene["options"].keys()), 
            key=f"{place}_{idx}"
        )
        if choice:
            reaction, delta = random.choice(scene["options"][choice])
            st.write(f"🗣️ {character_name}: {reaction}")
            score += delta
        else:
            all_answered = False

    st.write("---")
    if all_answered:
        st.subheader("🎀 데이트 결과 💌")
        if score >= 5:
            st.success(f"{character_name}이(가) 당신에게 반했어요! 💍")
        elif score >= 3:
            st.info(f"{character_name}과(와) 좋은 친구가 되었어요! 🤝")
        else:
            st.error(f"{character_name}은(는) 아직 어색한가봐요... 다음 기회에! 💔")
    else:
        st.warning("❗ 모든 질문에 답해주세요. 선택을 완료해야 결과가 나와요!")
