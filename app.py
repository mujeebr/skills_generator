import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
# Function to generate skills and companies based on the job role
def generate_skills_and_companies(job_role):
    # Initialize Google's Palm LLM
    llm = GooglePalm(google_api_key='AIzaSyAA28rGYJnOsGasVGEQ-dJRHXqLNTVEQz4', temperature=0)  # Replace with your Google API Key

    # Chain 1: This chain is for Job role
    prompt_template_name = PromptTemplate(
        input_variables=['job_role'],
        template="""I want to apply for a {job_role} role. Please help me with the desired skills and ensure you are 
        giving correct skills as it is critical."""
    )

    skills_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="skills")

    # Chain 2: This is for companies
    prompt_template_items = PromptTemplate(
        input_variables=['companies'],
        template="""Suggest some companies to apply for {job_role}. Return it as a comma separated string"""
    )

    companies_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="companies")

    chain = SequentialChain(
        chains=[skills_chain, companies_chain],
        input_variables=['job_role'],
        output_variables=['skills', "companies"]
    )

    response = chain({'job_role': job_role})

    return response

# Streamlit app
st.title("Skills and Companies Recommendation App")
job_role = st.text_input("Enter a job role:")

if st.button("Generate"):
    output = generate_skills_and_companies(job_role)

    if output:
        st.subheader("Skills:")
        skills = output['skills'].split('\n')
        for skill in skills:
            skill = skill.strip('* ').strip()
            st.write(skill)

        st.subheader("Companies:")
        companies = output['companies'].split('\n')
        for company in companies:
            company = company.strip('* ').strip()
            st.write(company)

# Adding an image to the app
st.sidebar.image("/Users/shaikmujeeburrahman/Downloads/odinschool1.jpg", use_column_width=True)

# "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"

