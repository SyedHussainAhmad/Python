import streamlit as st
from transformers import BertTokenizer, BertForMaskedLM

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

def summarize_paragraph(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=40, num_beams=4, early_stopping=True)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

def main():
    st.title("Paragraph Summarizer with BERT")
    st.markdown("---")
    st.write("Welcome to the Paragraph Summarizer app! Enter a paragraph in the text area below and click the button to generate a summary.")
    st.markdown("---")

    input_text = st.text_area("Enter your paragraph here", height=200)
    if st.button("Summarize", key="summarize_button"):
        if input_text.strip() != "":
            summary_text = summarize_paragraph(input_text)
            st.markdown("---")
            st.subheader("Summary:")
            st.write(summary_text)
        else:
            st.error("Please enter a paragraph to summarize.")

if __name__ == '__main__':
    main()
