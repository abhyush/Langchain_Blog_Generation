import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

##Function to get resonse from Llama 2 model
def getLlamaResponse(input_text, num_words, blog_style):
    ###llama model
    llm = CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q6_K.bin',
                        model_type= 'llama',
                        config= {'max_new_tokens':256,
                                 'temperature': 0.01})
    
##PromptTemplate
    template = """
                 Write a blog for {input_text} for the topic {blog_style} within {num_words} words.
                """
    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'num_words'],
                            template = template)
    
###Generate response
    response = llm.invoke(prompt.format(blog_style= blog_style, input_text= input_text, num_words = num_words ))
    print(response)
    return response





st.set_page_config(page_title="Generate Blogs", 
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog topic")

##We will create two more columns for 2 additional fields

col1, col2 = st.columns([5,5])

with col1:
    num_words = st.text_input("No of words:")
with col2:
    blog_style = st.selectbox('Writing the blog for',
                               ('Researchers', 'Data Scientist'),
                               index = 0)

submit =st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, num_words, blog_style))
                              