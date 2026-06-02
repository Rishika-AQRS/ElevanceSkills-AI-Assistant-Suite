import google.generativeai as genai
from PIL import Image
import os
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model=genai.GenerativeModel('gemini-flash-latest')

st.set_page_config(page_title="Multi Modal ChatBot")
st.header("Multi Modal Gemini Bot")

upload_file=st.file_uploader("Upload an Image: ", type=["png", "jpeg", "jpg"])
image=None

if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image, caption="Your Uploaded Image: ", use_container_width=True)

user_input=st.text_input("Ask a question about image or about any other topic: ", key="input")

if st.button("Generate!"):
    if user_input or image:
        prompt=[]
        if user_input:
            prompt.append(user_input)
        if image:
            prompt.append(image)
        
        with st.spinner("Gemini Model is Thinking...."):
            response=model.generate_content(prompt)
            st.write("### Response: ")
            st.write(response.text)
    else:
        st.warning("Please provide a question prompt or an image!")


