import tika-python
from tika import parser
import openai
import streamlit as st

st.title('PPTX TO STUDY NOTES CONVERTER')

apikey = st.text_input('Enter your OpenAI API key')
uploadedPresentation = st.file_uploader('Upload a PPTX file', type='pptx')

if uploadedPresentation is not None:
    tika.initVM()

    parsed = parser.from_file(uploadedPresentation)

    text = parsed['content']
    
    openai.api_key = (f"{apikey}")
                               
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="I want you to turn the following text from a powerpoint presentation into concise study notes. Each bullet point should be a new line. There should be three different sections. 1. Key concepts explained briefly 2. Important facts worth noting down 3. Questions for further exploration of the topic" + text,
    temperature=0.7,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.3
)
    st.header('Summarized')
    st.write( str(response['choices'][0]['text']))

else:
    st.write('Please upload a PPTX file')



