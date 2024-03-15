# import google.generativeai as genai

# apikey="AIzaSyADIFAXWJDLjmfC_MicaBPGF4z1AAsejnM"
import  streamlit as st
import google.generativeai as genai



genai.configure(api_key='AIzaSyADIFAXWJDLjmfC_MicaBPGF4z1AAsejnM')

model = genai.GenerativeModel('gemini-pro')

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

st.title("Simple Chat-bot")

prompt=st.text_input(label="Input")
click=st.button("Click Explain")
if click:
    while prompt!="exit" or prompt!="bye":
        response = model.generate_content(prompt,safety_settings=safety_settings)
        st.write(response.text)
else:
    st.write("I can guide you,please write something...")

#print(response.text)