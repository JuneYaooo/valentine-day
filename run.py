import streamlit as st

st.title("Happy Valentine's Day")

# video_file = st.file_uploader("Upload a video", type=["mp4"])
# if video_file:
#     video_player = st.video(video_file)
video_file = open('fullheart.mp4', 'rb') #enter the filename with filepath

video_bytes = video_file.read() #reading the file

st.video(video_bytes) #displaying the video

