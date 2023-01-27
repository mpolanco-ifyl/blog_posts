import streamlit as st
import openai_secret_manager

# Get GPT-3 API key
secrets = openai_secret_manager.get_secret("openai")
api_key = secrets["api_key"]

import openai
openai.api_key = api_key

# Define the prompt for GPT-3
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

st.set_page_config(page_title="Blog Post Generator", page_icon=":guardsman:", layout="wide")

# Create a title for the app
st.title("Blog Post Generator using GPT-3")

# Get user input for the topic of the blog post
topic = st.text_input("Enter the topic of the blog post:")

# Generate the blog post
if st.button("Generate Blog Post"):
    generated_text = generate_text(prompt=f"Write a blog post about {topic}")
    st.write(generated_text)
