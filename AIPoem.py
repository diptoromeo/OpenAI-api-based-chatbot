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

st.header('Welcome to AdalenAI Poem', divider='rainbow')

name = st.text_input('작가의 이름은: ')
subject = st.text_input('시의 주제는: ')
content = st.text_area('상세 내용을 알려주세요: ')
button_click = st.button('실행')

if button_click:
    with st.spinner('생성중......'):
        result = openai.chat.completions.create(
            model = 'dev-gpt-35',
            temperature=1,
            messages=[
                {'role':'system', 'content':'you are a helpful assistant.'},
                {'role':'user','content':'작가의 이름은 ' + name},
                {'role':'user','content':'시의 주제는 ' + subject},
                {'role':'user','content':'시의 내용은 ' + content},
                {'role':'user','content':'위 내용으로 시를 지어줘'}
            ]

        )
    st.success('Done!')
    st.write(result.choices[0].message.content)