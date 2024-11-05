import streamlit as st
from weasyprint import HTML

# Set the title of the app
st.title("HTML to PDF Converter")

# Create a text input for the user's name
name = st.text_input("Enter your name:")
message = st.text_area("Enter a message:")

# Create a button to generate PDF
if st.button("Generate PDF"):
    if name and message:
        # Create simple HTML content
        html_content = f"""
        <html>
            <head>
                <title>PDF Document</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    h1 {{ color: #333; }}
                    p {{ font-size: 14px; }}
                </style>
            </head>
            <body>
                <h1>Hello, {name}!</h1>
                <p>{message}</p>
            </body>
        </html>
        """

        # Generate PDF from HTML
        pdf_file = HTML(string=html_content).write_pdf()

        # Download the PDF
        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name="output.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please enter both your name and a message.")
