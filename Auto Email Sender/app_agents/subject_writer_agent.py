from agents import Agent

# Define the email subject writer agent with specific instructions
instructions = "You can write a subject for a cold sales email. \
You are given a message and you need to write a subject for an email that is likely to get a response."

# Create the email subject writer agent with the defined instructions and model
subject_writer = Agent(name="Email subject writer", instructions=instructions, model="gpt-4o-mini")

