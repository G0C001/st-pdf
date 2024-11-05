import streamlit as st
import ctypes, json, io, os
from body import styleresume, personal, summary, education, experience_certfy, skills, project_lang

# gtk3_path = "GTK3/"
# for file_name in os.listdir(gtk3_path):
#     if file_name.endswith(".dll"):
#         dll_path = os.path.join(gtk3_path, file_name)
#         try:
#             my_dll = ctypes.CDLL(dll_path)
#             print(f"Successfully loaded {dll_path}")
#         except Exception as e:
#             print(f"Failed to load {dll_path}: {e}")

from weasyprint import HTML
from body import gemini

st.title('ATS_RESUME')
role = st.text_input('Enter your role:')
job_input = st.text_area('Enter your job descripition:', height=200)

if st.button('Submit'):
    try:
        skills_dict = json.loads(gemini(job_input))
        html_content = f"""
        {styleresume.style()}
        <body>
            <div class="container">
                {personal.personal(role)}
                {summary.summary(role)}
                {education.education()}
                {experience_certfy.experience_certfy()}
                {skills.skill(skills_dict)}
                {project_lang.project_lan()}
            </div>
        </body>
        </html>
        """
        pdf = HTML(string=html_content).write_pdf()
        pdf_buffer = io.BytesIO(pdf)
        st.download_button(
            label=f'Download Resume for {role}',
            data=pdf_buffer,
            file_name=f'GokulVasanth_{role}_Resume.pdf',
            mime='application/pdf'
        )

    except json.JSONDecodeError:
        st.error('Invalid JSON format. Please check your input.')
    except Exception as e:
        st.error(f"An error occurred: {e}")