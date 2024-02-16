
from github import Github
import streamlit as st
import os

# GitHub details
github_token = "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"
repo_owner = "GeniusMundi10"
repo_name = "streamlit-app-"
repo_path = "input_pdfs"

# Authenticate with GitHub
g = Github(github_token)
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Streamlit app
st.title("PDF File Uploader to LegalGPT")

# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    # Display file details
    st.write("File Details:")
    st.write(f"File Name: {uploaded_file.name}")
    st.write(f"File Size: {uploaded_file.size} bytes")

    # Save uploaded file to a local temporary folder
    temp_folder = "temp_folder"
    os.makedirs(temp_folder, exist_ok=True)
    file_path = os.path.join(temp_folder, uploaded_file.name)
    with open(file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    
    # Upload the file to the GitHub repository
    with open(file_path, "rb") as file_content:
        repo.create_file(os.path.join(repo_path, uploaded_file.name), "Upload new file", file_content.read())

    # Display success message
    st.success("File uploaded successfully!")

# Display list of files in the GitHub repository
#files = [file.name for file in repo.get_contents(repo_path)]
#st.subheader("Files in GitHub Repository:")
#st.write(files)



