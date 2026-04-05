from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

# Load environment variables from .env file
load_dotenv()
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

# Define the sales agent with specific instructions
instructions = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

# Initialize the OpenAI client and model for the sales agent
deepseek_client = AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek-chat", openai_client=deepseek_client)

# Create the sales agent with the defined instructions and model
sales_agent1 = Agent(name="DeepSeek Sales Agent", instructions=instructions, model=deepseek_model)

