import streamlit as st
import google.generativeai as genai
import os

# Set the Gemini API Key (Replace with your actual API key)
os.environ["GEMINI_API_KEY"] = "AIzaSyBxOmfzVxl8XxloiShveE_2cJD6wVze7pM"  # Replace with your API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# System Prompt for AI to guide the review process
sys_prompt = """
As an AI Code Reviewer, your role is to analyze submitted Python code with precision. Your review should include:

🔹Bug Detection: Spot and explain any bugs, errors, or logical flaws in the code, providing clear insights into potential issues.
🔹Code Fixes: Suggest practical fixes or optimizations, with clear explanations on how they address the identified problems or improve the code.
🔹Guidance & Tips: Provide concise, easy-to-understand recommendations for developers of all experience levels, with an emphasis on best practices and enhancing code quality.
"""

def review_code_with_ai(code_snippet):
    """Requests the Gemini AI model to review and suggest improvements on the provided code."""
    prompt = sys_prompt + f"\n\nReview the following code and provide suggestions:\n\n{code_snippet}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text if response else "No suggestions returned by AI."

    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

# Streamlit UI Configuration
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

# Page title and description with emojis
st.title("🔍✨ AI Code Reviewer")
st.markdown("<h2 style='font-size: 22px; font-weight: bold;'>A code review is a chance to teach and learn, every time.</h2>", unsafe_allow_html=True)
st.markdown("Paste your code below and let the 🧠 AI provide a detailed review with suggestions for improvements 💡.")

# Code input area with icon style and emoji help
code_input = st.text_area("Paste your code here 📝:", height=300, help="Your code is about to get a smart review 🔎")

# Button for submitting code review with emoji
if st.button("Review Code 🔍💻"):
    if code_input.strip():  # Check if code input is not empty
        with st.spinner("Analyzing your code... ⏳"):
            review_result = review_code_with_ai(code_input)
        st.subheader("AI Review & Suggestions 🤖💡:")
        st.write(review_result)
    else:
        st.warning("⚠️ Please paste some code before requesting a review.")
# Footer
st.markdown("""
    <div class='footer'style='text-align: center;'>
        Developed by <b>Susmitha Reddy</b> | Built with ✨ using Streamlit
    </div>
    """, unsafe_allow_html=True)