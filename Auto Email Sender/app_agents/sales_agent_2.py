from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

# Load environment variables from .env file
load_dotenv()
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Define the sales agent with specific instructions
instructions = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

# Initialize the OpenAI client and model for the sales agent
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)

# Create the sales agent with the defined instructions and model
sales_agent2 =  Agent(name="Gemini Sales Agent", instructions=instructions, model=gemini_model)
