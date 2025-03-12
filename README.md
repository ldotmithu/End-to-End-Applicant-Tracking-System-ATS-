# 📄 Resume ATS Checker

The **Resume ATS Checker** is a web application built using Streamlit that allows users to compare their resumes with job descriptions and get insights on how well their resume matches the job criteria. The application uses a language model to evaluate the resume's compatibility with the provided job description, offering a detailed match score, missing keywords, and a suggestions.

## ✨ Features
- **Job Description and Resume Analysis**: Compare a resume against a provided job description. 📝
- **Match Score**: Display a percentage score showing how closely the resume matches the job description. 📊
- **Missing Keywords**: Display missing keywords from the resume based on the job description. 🔍


## 🛠️ Technologies Used
- **Streamlit**: Framework used for building the web interface. 🌐
- **LangChain & Groq**: Used for handling large language model (LLM) interactions to process and analyze the text. 💡
- **PyPDF2**: Used for parsing and extracting text from PDF resumes. 📄
- **Python**: Programming language used to develop the application. 🐍
- **Dotenv**: For managing environment variables. 🔑

## 🚀 Installation

### 📌 Prerequisites
- Python 3.10
- Streamlit
- Required dependencies (listed in `requirements.txt`)

### 🧑‍💻 Steps to Run the Application Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ldotmithu/End-to-End-Applicant-Tracking-System-ATS-.git
   cd End-to-End-Applicant-Tracking-System-ATS

2. **Create and activate a virtual environment (optional but recommended)::**
   ```bash
   python -n ats python=3.10 -y 
   conda activate ats 

3. **Install the dependencies::**
   ```bash
   pip install -r requirements.txt
 
4. **Install the dependencies::**
- Create a .env file for environment variables: Make sure to create a .env file in the root directory to store your GROQ_API_KEY.
- Example .env file:
   ```bash
   GROQ_API_KEY=your_api_key_here

5. **Run the application::**
   ```bash
   streamlit run app.py
   
6. Open the app in your browser: After running the above command, open the displayed URL (typically http://localhost:8501) in your browser. 🌐




   
