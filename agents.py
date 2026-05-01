from crewai import Agent, Task, Crew, LLM
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools import yt_tool
load_dotenv()
import streamlit as st

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
print(os.getenv('GROQ_API_KEY'))
llm = LLM(
    model="groq/mixtral-8x7b-32768",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=0.9,
    stop=None,
    stream=False,
)
## Create a senior blog content researcher

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Analyze the provided transcript provided by tools and extract relevant insights from the url {YT_URL}',
    verbose=True,
    backstory=(
        'Expert in understanding YouTube video transcripts in AI, Data Science, Machine Learning and GenAI, and providing structured insights'
    ),
   
    allow_delegation=True,
    llm=llm,
    tools = [yt_tool]
)

# creating a Senior blog writer agent

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the analysis of yt video  using provided research insights',
    verbose=True,
    backstory=(
        '''
        With a flair for simplifying complex topics, you craft engaging narratives
        that captivate and educate, bringing new discoveries to light in an accessible manner
        '''
    ),
    
    allow_delegation=False,
    llm=llm,
   # tools = [yt_tool]
  
)