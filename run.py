import streamlit as st

st.title("Happy Valentine's Day")


video_file = open('fullheart.mp4', 'rb') #enter the filename with filepath

video_bytes = video_file.read() #reading the file

st.video(video_bytes) #displaying the video

