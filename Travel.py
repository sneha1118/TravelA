import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template="""Welcome to the {city} travel guide!
    If you're visiting in {month}, here is what you can do:
    1. Must visit attractions.
    2. Local cuisines you can try.
    3. Useful phrases in {language} to help you get around.
    4. Budget-friendly tips for travelers on a budget of {budget}.
    Enjoy your trip. """
)

st.title("Travel Guide Generator")

city = st.text_input("Enter the city you want to visit: ")
month = st.text_input("Enter the month of your visit: ")
language = st.text_input("Enter the language spoken in the city: ")
budget = st.text_input("Enter your budget for the trip: ")

chain = prompt_template | llm
if city and month and language and budget:
    response = chain.invoke({
        "city": city,
        "month": month,
        "language": language,
        "budget": budget
    })
    st.write(response.content)

