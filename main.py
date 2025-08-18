import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_community.chat_models import ChatOpenAI


# ---------- Streamlit page setup ----------
st.set_page_config(
    page_title="Blog Post Generator"
)

st.title("Blog Post Generator")

# ---------- Sidebar: OpenAI API Key ----------
openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type="password"
)

# ---------- Function to generate blog post ----------
def generate_response(topic):
    # Initialize chat model
    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model="gpt-3.5-turbo",  # chat model
    )

    # Prompt template
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}

    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    # Format prompt
    query = prompt.format(topic=topic)

    # Call chat model
    response = llm.invoke([HumanMessage(content=query)])

    # Display output
    st.markdown("### Generated Blog Post")
    st.write(response.content)

# ---------- Input from user ----------
topic_text = st.text_input("Enter topic:")

# ---------- Validation ----------
if topic_text:
    if not openai_api_key.startswith("sk-"):
        st.warning("Enter a valid OpenAI API Key (starts with 'sk-')")
    else:
        generate_response(topic_text)
