import openai
import streamlit as st


#openai 환경변수 설정 및 api를 가지고 오기.
OPENAI_API_KEY = 'eddfc325c01240ea8bb2971b5251be6f'
AZURE_ENDPOINT = 'https://labuser37openai.openai.azure.com/'
OPENAI_API_TYPE ='azure'
OPENAI_API_VERSION ='2023-05-15'


openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = AZURE_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header('Welcome to AdalenAi-Chatgpt', divider='rainbow')

query = st.text_input('궁금한 내용을 물어보세요: ')
button_click = st.button('실행')

if button_click:
    result = openai.chat.completions.create(
        model = 'dev-gpt-35',
        temperature=1,
        messages=[
            {'role':'system', 'content':'you are a helpful assistant.'},
            {'role':'user','content':query}
        ]

    )

    st.write(result.choices[0].message.content)