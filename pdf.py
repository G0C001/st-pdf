import streamlit as st
import subprocess

st.title("Install Streamlit and WeasyPrint")

if st.button("Install"):
    # Execute the shell script
    result = subprocess.run(["./install_streamlit_weasyprint.sh"], capture_output=True, text=True, shell=True)
    
    # Display the output and error (if any)
    st.text("Output:")
    st.text(result.stdout)
    st.text("Error:")
    st.text(result.stderr)
