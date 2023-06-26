import streamlit as st
import numpy as np

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


st.title("Multiplying Two Matrices")

# Get the dimension of the matrices
dim1 = st.number_input("Enter the dimension of the first matrix:", min_value=1, step=1)
dim2 = st.number_input("Enter the dimension of the second matrix:", min_value=1, step=1)

# Create form to get input for the matrices
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
submit_button = form.form_submit_button(label='Multiply')

# If the submit button is clicked
if submit_button:
    # Convert the matrices to NumPy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    # Multiply the matrices
    result_matrix = np.dot(matrix1, matrix2)
    # Display the result
    st.write("Result Matrix:")
    st.write(result_matrix)
