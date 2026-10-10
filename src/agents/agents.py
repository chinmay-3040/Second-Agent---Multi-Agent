from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

load_dotenv()

# Model Initialization

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=GROQ_API_KEY
)

# 1st Agent : Search Agent -> Searches the topic and returns the relevant urls 
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="""
You are a web research search agent.

Your task:
1. Search for the user's research topic using web_search.
2. Use the tool results as the source of search information.
3. Preserve the exact titles and URLs returned by the tool.
4. Do not invent, modify, or guess URLs.
5. Do not summarize away the URLs.

Return the results in exactly this format for every result:

Title: <title>
URL: <full URL>
Snippet: <snippet>

Separate results with:
---

Return up to 5 results. Do not write an introduction or conclusion.
"""
    )

# 2nd Agent : Reader Agent -> takes the url and scrapes the important content
def build_reader_agent():
    return create_agent(
        model= llm,
        tools=[scrape_url],

    )



#writer chain 
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])


writer_chain = writer_prompt | llm | StrOutputParser()





#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()