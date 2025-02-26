#streamlit
import streamlit as st


st.set_page_config(page_title= "growth mindset project", project_icon="✨")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embracr challenges, learn from mistakes,and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection,challenges, and achievements!🌟")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st. write("“Succes is not final, failure is not fatal:it is the courage to continue that counts”.-Winston churchill")

st.header("🔧 What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing;")


#condition
if user_input:
    st.success(f"💪you're facing: {user_input}. Keep pushing forward towords your goal!🚀")
else:
    st.warning("Tell us your challenge to get started!")

    #refiexing
    st.header("Reflect on your Learning")
    reflection =st.text_area("Write your reflection here:")
if reflection:
    st.success(f"🌟 Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header("🏆 Celebrate Your Wins!")
acheivement = st.text_input("Share something you've recently accomplished:")

if acheivement:
    st.success(f"💥 Amazing! you achieved:{acheivement}")
else:
    st.info("Big or small , every acheivement counts! Share one now 😍")

    #footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination!🤩")
st.write("**⭕Created by Asmara Faisal**")