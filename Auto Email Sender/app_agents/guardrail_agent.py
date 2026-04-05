from agents import Agent
from pydantic import BaseModel

# Define the output schema for the guardrail agent
class NameCheckOutput(BaseModel):
    is_name_in_message: bool
    name: str

# Define the guardrail agent with specific instructions and output type
guardrail_agent = Agent( 
    name="Name check",
    instructions="Check if the user is including someone's personal name in what they want you to do.",
    output_type=NameCheckOutput,
    model="gpt-4o-mini"
)