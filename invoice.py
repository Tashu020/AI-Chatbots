from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pytesseract
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Function to perform OCR (extract text from image)
def extract_text_from_image(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)  # Open the uploaded image
        text = pytesseract.image_to_string(image)  # Extract text using Tesseract OCR
        return text.strip()  # Remove extra spaces or new lines
    else:
        return "No image uploaded."

# Function to get response from Gemini AI
def get_gemini_response(text, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([text, prompt])
    return response.text

# Streamlit UI
st.set_page_config(page_title="Invoice Reader with OCR")

st.header("Invoice Reader (OCR + AI)")
uploaded_file = st.file_uploader("Upload an Invoice (JPG, PNG, JPEG)", type=["jpg", "jpeg", "png"])
input_query = st.text_input("Ask a question about the invoice:", key="input")

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

    # Perform OCR
    extracted_text = extract_text_from_image(uploaded_file)
    st.subheader("Extracted Invoice Text:")
    st.text(extracted_text)  # Display extracted text

submit = st.button("Analyze Invoice")

# Prompt for AI Analysis
input_prompt = """
You are an expert in reading invoices.
You will receive extracted text from invoices & must answer queries based on it.
"""

# If button is clicked
if submit and extracted_text:
    response = get_gemini_response(extracted_text, input_query)
    st.subheader("AI Response:")
    st.write(response)
