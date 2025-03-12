from APP.helper import extract_text,ats_evaluate
import streamlit as st 

st.set_page_config(page_title="Smart ATS Resume Evaluator", page_icon="🚀")

st.title("🚀 Smart ATS Resume Evaluator")

job_description = st.text_area("Enter the Job Description:", height=200)
uploaded_file = st.file_uploader("Upload Your Resume (PDF only)", type=["pdf"])

 
if st.button("Analyze Resume"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing... ⏳"):
            resume_text = extract_text(uploaded_file)
            ats_result = ats_evaluate(resume_text, job_description)

        st.subheader("📊 Evaluate")

        
        match_score = ats_result.get("Match Score", "0%")
        try:
            match_percentage = int(match_score.replace('%', ''))
        except:
            match_percentage = 0

            
        st.progress(match_percentage)

        st.metric("Match Score", f"{match_percentage}%", delta=None)

           
        missing_keywords = ats_result.get("Missing Keywords", [])
        st.subheader("🔎 Missing Keywords")
        if missing_keywords:
            st.write(", ".join(missing_keywords))
        else:
            st.success("No missing keywords 🎉")

           
        st.subheader("📝 Profile Summary")
        st.write(ats_result.get("Summary", "No summary available"))

    else:
        st.warning("Please upload a resume and enter a job description.")
        
        
with st.sidebar:
    st.markdown("### About")
    st.markdown("This app evaluates your resume against a job description using an advanced ATS powered by Groq's LLM.")
    st.markdown("---")
    st.markdown("**How to use:**")
    st.markdown("1. Paste the job description in the text area.")
    st.markdown("2. Upload your resume in PDF format.")
    st.markdown("3. Click 'Evaluate' to get insights.")
    st.markdown("---")
    st.markdown("Made with ❤️ by ldotmithu")
