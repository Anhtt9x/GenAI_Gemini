import google.generativeai as genai
import streamlit
from PIL import Image
import os

os.environ["GENAI_API_KEY"] = "AIzaSyB3m41ogZgvqSZEBbf1r4g6F8AHbVChTFY"

genai.configure(api_key=os.getenv('GENAI_API_KEY'))

