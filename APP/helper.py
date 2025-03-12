import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import PyPDF2
from io import BytesIO

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Helper Functions
def load_pdf_resume(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text(file):
    resume_text = load_pdf_resume(file)
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_text(resume_text)

def ats_evaluate(resume_text, job_description):
    prompt = f"""
    You act as an Application Tracking System (ATS).
    Compare the given job description with the provided resume and provide:
    - A match score (0-100%)
    - Missing keywords
    - A profile summary
    
    **Job Description:** 
    {job_description}
    
    **Resume:** 
    {resume_text}
    
    Provide results in the following format:
    - Match Score: XX%
    - Missing Keywords: [keyword1, keyword2, ...]
    - Summary: Brief summary of the candidate's profile
    """
    
    llm = ChatGroq(api_key=GROQ_API_KEY, model='llama-3.3-70b-versatile', temperature=0.5)
    response = llm.invoke(prompt)
    

    result = response.content.strip().split('\n')
    ats_result = {}
    
    for line in result:
        if "Match Score" in line:
            ats_result["Match Score"] = line.split(":")[1].strip()
        elif "Missing Keywords" in line:
            ats_result["Missing Keywords"] = line.split(":")[1].strip().split(",")
        elif "Summary" in line:
            ats_result["Summary"] = line.split(":")[1].strip()

    return ats_result


