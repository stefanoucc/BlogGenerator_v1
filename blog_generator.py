# Import necessary modules
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

# Hugging Face token
huggingface_token = #replace with your tokem

# Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "meta-llama/Meta-Llama-3-8B"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=huggingface_token)
    model = AutoModelForCausalLM.from_pretrained(model_name, token=huggingface_token, torch_dtype=torch.float16)
    
    # Set the pad token
    tokenizer.pad_token = tokenizer.eos_token
    return model, tokenizer

model, tokenizer = load_model()

# Define the function to get response from the LLama model
def getLLamaresponse(input_text, no_words, blog_style):
    try:
        # Prepare the prompt
        prompt = f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."
        
        # Tokenize the input
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512).to("cuda" if torch.cuda.is_available() else "cpu")
        
        # Generate the response
        outputs = model.generate(inputs.input_ids, attention_mask=inputs.attention_mask, max_length=int(no_words), pad_token_id=tokenizer.eos_token_id)
        
        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    except Exception as e:
        return f"Error: {str(e)}"

st.header("Generate Blogs 🤖")

# User inputs
input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    with st.spinner('Generating blog...'):
        response = getLLamaresponse(input_text, no_words, blog_style)
    st.write(response)
