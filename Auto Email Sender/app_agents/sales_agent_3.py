from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

# Load environment variables from .env file
load_dotenv()
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")
groq_api_key = os.getenv("GROQ_API_KEY")

# Define the sales agent with specific instructions
instructions = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

# Initialize the OpenAI client and model for the sales agent
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
llama3_3_model = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=groq_client)

# Create the sales agent with the defined instructions and model
sales_agent3  = Agent(name="Llama3.3 Sales Agent",instructions=instructions,model=llama3_3_model)
