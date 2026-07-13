import streamlit as st

# પ્રશ્નો અને જવાબોની યાદી (તારો જ ડેટા)
Questions = [
    ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1],
    ["What is the largest planet in our solar system?", "Jupiter", "Saturn", "Neptune", "Uranus", 1],
    ["duniya ni sauthi moti city kai che?", "jay", "ahmedabad", "sydney", "mvr", 1],
    ["What is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the currency of Japan?", "Yen", "Dollar", "Euro", "Pound", 1],
    ["What is the highest mountain in the world?", "Mount Everest", "K2", "Kangchenjunga", "Lhotse", 1],
    ["What is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert", 1],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3],
    ["What is the largest country in the world by land area?", "Russia", "Canada", "China", "United States", 1],
    ["What is the smallest country in the world by land area?", "Vatican City", "Monaco", "Nauru", "San Marino", 1],
    ["What is the largest mammal in the world?", "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", 1],
    ["What is the largest bird in the world?", "Ostrich", "Eagle", "Albatross", "Penguin", 1],
    ["duniya ma sauthi saaru ghar kone banav ta aavde che?", "labour", "civil engineer", "mahavir", "null", 3],
    ["What is the largest fish in the world?", "Whale Shark", "Great White Shark", "Manta Ray", "Tiger Shark", 1],
    ["What is the largest amphibian in the world?", "Chinese Giant Salamander", "Axolotl", "Hellbender", "Cane Toad", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

# ગેમની સ્ટેટ મેનેજ કરવા માટે Streamlit Session State
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "money" not in st.session_state:
    st.session_state.money = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title(" Kaun banega crorepati (KBC) ")
st.write("---")

# જો ગેમ પૂરી થઈ ગઈ હોય તો
if st.session_state.game_over:
    st.error(f"game puri thay gayi bhai! tu che ne total ₹{st.session_state.money} jeetyo che to chalo william jones.")
    if st.button("phir se khel 🔄"):
        st.session_state.current_question = 0
        st.session_state.money = 0
        st.session_state.game_over = False
        st.rerun()
else:
    q_idx = st.session_state.current_question
    
    # બધા પ્રશ્નો પતી ગયા હોય તો
    if q_idx >= len(Questions):
        st.balloons()
        st.success(f"🥳 congratulations !! te che ne badha answer bhul thi sacha aapi didha. tu total ₹{st.session_state.money} jeetyo che have to barbie que jau pade!")
        if st.button("farithi ram bhai tu 🔄"):
            st.session_state.current_question = 0
            st.session_state.money = 0
            st.session_state.game_over = False
            st.rerun()
    else:
        # કરન્ટ પ્રશ્ન અને લેવલ બતાવો
        q_data = Questions[q_idx]
        st.subheader(f"question {q_idx + 1}: {q_data[0]}")
        st.info(f"to yeh raha aapka saval ₹{levels[q_idx]} tamara maate! (haal ni jeeteli rakam: ₹{st.session_state.money})")
        
        # ઓપ્શન્સ માટે બટનો
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(f"1️⃣ {q_data[1]}", use_container_width=True):
                check_answer(1, q_data[5], levels[q_idx])
            if st.button(f"2️⃣ {q_data[2]}", use_container_width=True):
                check_answer(2, q_data[5], levels[q_idx])
                
        with col2:
            if st.button(f"3️⃣ {q_data[3]}", use_container_width=True):
                check_answer(3, q_data[5], levels[q_idx])
            if st.button(f"4️⃣ {q_data[4]}", use_container_width=True):
                check_answer(4, q_data[5], levels[q_idx])

# જવાબ ચેક કરવાનું ફંક્શન
def check_answer(user_ans, correct_ans, current_level_money):
    if user_ans == correct_ans:
        st.session_state.money = current_level_money
        st.session_state.current_question += 1
        st.toast("correct !", icon="🎉")
        st.rerun()
    else:
        st.session_state.game_over = True
        st.rerun()
