# import google.generativeai as genai

import  streamlit as st
import google.generativeai as genai



genai.configure(api_key='A-----------Your Key-----------M')

model = genai.GenerativeModel('gemini-pro')

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
   
] # i got the security error thats why i have included this json code


def generate_content(prompt):
    if prompt in("exit","bye"):# ((prompt!="exit") or (prompt!="bye")):
        return "Thanks for visiting "
    else:
        response = model.generate_content(prompt,safety_settings=safety_settings) # it will generate content
    return response.text

st.title("Generative AI Chat-bot")

prompt=st.text_input(label="Input") # Input

click=st.button("Click to Explain") # once the user click this button it will call the generate content button
if click: # st.button("Click to Explain")
    st.write(generate_content(prompt)) 
    
