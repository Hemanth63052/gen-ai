import streamlit as st
import requests

st.title("AI Text Generator")

prompt = st.text_area("Enter a prompt:", "")

if st.button('Generate Text'):
    response = requests.post(
        'http://localhost:9503/gen_ai/generate_text/',
        json={"prompt": prompt}
    )

    if response.status_code == 200:
        result = response.json()
        if 'response' in result:
            st.write(f"Generated Text: {result['response']}")
        else:
            st.write(f"Error: {result.get('error')}")
    else:
        st.write("Error fetching data from the backend")
