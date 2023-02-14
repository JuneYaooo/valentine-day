import os
from PIL import Image
import streamlit as st


def create_album(folder_path):
    # 判断文件夹是否存在
    if not os.path.isdir(folder_path):
        st.error("The folder does not exist.")
        return

    # 读取文件夹中的图片
    images = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        abs_file_path = os.path.abspath(file_path)
        print('file_path',abs_file_path)
        if os.path.isfile(abs_file_path):
            try:
                with Image.open(file_path) as img:
                    images.append(img)
            except:
                st.error(f"Failed to load image: {filename}")

    # 展示图片
    for i, img in enumerate(images):
        print('img',img)
        st.image(img, use_column_width=True)
        st.write(f"Displaying image {i + 1}")
        st.write("Press the button to continue...")
        st.button("Next")


# 创建相册
st.title("Electronic Album")
create_album("./photos")
