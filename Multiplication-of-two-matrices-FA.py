import streamlit as st
import numpy as np

# تنظیم تصویر پس زمینه صفحه
page_bg = 'https://www.freecodecamp.org/news/content/images/2022/01/alexander-sinn-KgLtFCgfC28-unsplash.jpg'
page_bg_style = f"""
    <style>
    .stApp {{
        background-image: url({page_bg});
        background-size: cover;
    }}
    </style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

# سبک هدر
header_style = """
    <style>
    *{
        //direction:rtl;
    }

    .css-1629p8f h1, .css-1629p8f h2, .css-1629p8f h3, .css-1629p8f h4, .css-1629p8f h5, .css-1629p8f h6, .css-1629p8f span {
        color: floralwhite;
        scroll-margin-top: 2rem;
        font-size: 50px;
        font-family: B Yekan;
    }

    .row-widget ,.stButton{
        position: relative ; !important
        width: 100% !important;
        text-align: center ; !important
        padding-top: 20px;  !important
    } 

    .css-1a32fsj ,.e19lei0e0{
        text-align: center;
    }


    .header {
        font-size: 40px !important;
        text-align: right !important;
        direction: rtl !important;
        margin-bottom: 50px !important;
    }
    .block-container{
        background-color: rgb(17 61 101 / 75%);
        text-align: right;
    }

    .css-1629p8f h1, .css-1629p8f h2, .css-1629p8f h3, .css-1629p8f h4, .css-1629p8f h5, .css-1629p8f h6, .css-1629p8f span {
        color: floralwhite;

    }

    .css-16idsys p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 17px;
        text-align: right;
        color: darksalmon;
        font-weight: bold;
        direction: rtl;
        padding-left: 400px;
        font-family: B Yekan !important;
    }

    .css-5rimss p {
        word-break: break-word;
        color: #ffffff;
        direction:rtl;
        font-weight: bold;
        font-size: 20px;
        font-family: B Titr;
    }

    [type=button]:not(:disabled), [type=reset]:not(:disabled), [type=submit]:not(:disabled), button:not(:disabled) {
        //cursor: pointer;
        //width: 100%;
        color: #ffffff;
        background: #ff0606;
        font-family: B Titr;
    }

    .css-1vbkxwb p {
        word-break: break-word;
        margin-bottom: 0px;
        font-family: B Yekan;
        font-size: 18px;
    }

    </style>
"""
st.markdown(header_style, unsafe_allow_html=True)

# عنوان صفحه
st.title("ضرب دو ماتریس")

# دریافت ابعاد ماتریس‌ها
dim1 = st.number_input("ابعاد ماتریس اول را وارد کنید:", min_value=1, step=1)
dim2 = st.number_input("ابعاد ماتریس دوم را وارد کنید:", min_value=1, step=1)

# ایجاد فرم برای دریافت ورودی ماتریس‌ها
form = st.form(key='my-form')
matrix1 = []
matrix2 = []
for i in range(dim1):
    matrix1.append([])
    for j in range(dim1):
        matrix1[i].append(form.number_input(label="", key=f"matrix1[{i}][{j}]"))
for i in range(dim2):
    matrix2.append([])
    for j in range(dim2):
        matrix2[i].append(form.number_input(label="", key=f"matrix2[{i}][{j}]"))
submit_button = form.form_submit_button(label='ضرب')

# در صورت فشردن دکمه ارسال
if submit_button:
    # تبدیل ماتریس‌ها به آرایه‌های NumPy
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    # ضرب ماتریس‌ها
    result_matrix = np.dot(matrix1, matrix2)
    # نمایش نتیجه
    st.write("ماتریس نتیجه:")
    st.write(result_matrix)
