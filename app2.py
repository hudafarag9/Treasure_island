import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

# Initialize session state for game progress
if "stage" not in st.session_state:
    st.session_state.stage = "start"


def go_to(stage):
    st.session_state.stage = stage


def reset_game():
    st.session_state.stage = "start"


# --- ASCII art banner ---
ASCII_ART = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

st.title("🏝️ Treasure Island")
st.code(ASCII_ART, language=None)

stage = st.session_state.stage

# --- START ---
if stage == "start":
    st.subheader("Welcome to the Treasure Island game!")
    st.write("Your mission is to find the treasure.")
    st.write("**You're at a crossroad. Where do you want to go?**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Left", use_container_width=True):
            go_to("lake")
            st.rerun()
    with col2:
        if st.button("➡️ Right", use_container_width=True):
            go_to("hole")
            st.rerun()

# --- RIGHT PATH ---
elif stage == "hole":
    st.error("You fell into a hole. Game Over.")
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()

# --- LEFT PATH -> LAKE ---
elif stage == "lake":
    st.write("Great! You've come to a lake. There is an island in the middle of the lake.")
    st.write("**What do you want to do?**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⛵ Wait for a boat", use_container_width=True):
            go_to("island")
            st.rerun()
    with col2:
        if st.button("🏊 Swim across", use_container_width=True):
            go_to("trout")
            st.rerun()

elif stage == "trout":
    st.error("You got attacked by an angry trout. Game Over.")
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()

# --- ISLAND -> DOORS ---
elif stage == "island":
    st.write("You arrived at the island unharmed.")
    st.write("**There are 3 doors. Which color do you choose?**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔴 Red", use_container_width=True):
            go_to("red")
            st.rerun()
    with col2:
        if st.button("🟡 Yellow", use_container_width=True):
            go_to("yellow")
            st.rerun()
    with col3:
        if st.button("🔵 Blue", use_container_width=True):
            go_to("blue")
            st.rerun()

elif stage == "red":
    st.error("It's a room full of fire. Game Over.")
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()

elif stage == "yellow":
    st.success("🎉 You found the treasure. You win! 🎉")
    st.balloons()
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()

elif stage == "blue":
    st.error("You entered a room full of snakes. Game Over.")
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()
