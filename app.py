import google.generativeai as genai
import streamlit as st
from PIL import Image
import os

os.environ["GENAI_API_KEY"] = ""

genai.configure(api_key=os.getenv('GENAI_API_KEY'))

def get_genai_response(image, input, prompt):
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    
    response = model.generate_content([input,image[0],prompt])

    return response.text

def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()

        image_part = [
            {
                "mime_type":upload_file.type,
                "data": bytes_data
            }
        ]

        return image_part
    else:
        raise FileNotFoundError("No file upload")
    


st.set_page_config(page_title="Invoce Extractor")

st.header("Gemini Application")

input= st.text_input("Input_prompt:", key="input")

upload_file  = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

image=""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image=image,caption="Upload image", use_column_width=True)

submit = st.button("Tell me about invoice")

input_prompt="""
you are an expert in understanding invoices.
You will receive input images as invoice and 
you will have to answer questions based on the input image.
"""


if submit:
    image_data = input_image_setup(upload_file)
    response = get_genai_response(image=image_data,prompt=input_prompt,input=input)

    st.subheader("The Response is ")
    st.write(response)  

