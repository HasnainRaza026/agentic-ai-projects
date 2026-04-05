from agents import Agent

# Define the email HTML converter agent with specific instructions
instructions = "You can convert a text email body to an HTML email body. \
You are given a text email body which might have some markdown \
and you need to convert it to an HTML email body with simple, clear, compelling layout and design."

# Create the email HTML converter agent with the defined instructions and model
html_converter = Agent(name="HTML email body converter", instructions=instructions, model="gpt-4o-mini")

