

import streamlit as st
import google.generativeai as palm

# Configure the Google Palm API, don't use this api key, use yours.
palm.configure(api_key="AIzaSyAA28rGYJnOsGasVGEQ-dJRHXqLNTVEQz4")

# Define the Streamlit app
def main():
    # Set the title and description
    st.title("Skills and Companies Recommender") # to set the title for the app
    st.subheader("Developed by Mujeeb") # it's a sub heading
    st.sidebar.image("odinschool1.jpg") # to place an image to the left side
    st.write("Enter the job role to get recommendations.") # suggesting an user what needs to be done with this line of code

    # Get user input for job role
    job_role = st.text_input("Enter a job role:") # input space to enter text

    # Define the prompt based on the job role input
    prompt = f'''What are the skills required for a {job_role}? and the top companies to apply to?
skills: name skills without description
companies: name top 10 companies
'''

    # Generate text based on the prompt and user input
    if st.button("Generate"):
        with st.spinner("Generating recommendations..."):
            completion = palm.generate_text(
                model='models/text-bison-001',
                prompt=prompt,
                temperature=0.1
            )
        st.subheader("Generated Recommendations:")
        st.write(completion.result)

# Run the app
if __name__ == "__main__":
    main()
