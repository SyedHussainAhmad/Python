import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Helper function to get GPT-3.5 completion
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # Degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def main():
    st.title("Text Summarizer")
    st.markdown("---")
    st.write("Welcome to the Text Summarizer app! Enter a paragraph in the text area below and click the button to generate a summary.")
    st.markdown("---")
    input_text = st.text_area("Enter your paragraph here", height=200)
    if st.button("Summarize", key="summarize_button"):
        if input_text.strip() != "":
            prompt = f"""
            Summarize the text delimited by triple backticks 
            into a single sentence.
            ```
            {input_text}
            ```
            """
            summary_text = get_completion(prompt)
            st.markdown("---")
            st.subheader("Summary:")
            st.write(summary_text)
        else:
            st.error("Please enter a paragraph to summarize.")

if __name__ == '__main__':
    main()
