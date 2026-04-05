from agents import Agent
from tools import subject_writer_tool, html_converter_tool, send_html_email

# Define the tools to be used by the emailer agent
email_tools = [subject_writer_tool, html_converter_tool, send_html_email]

# Define the emailer agent with specific instructions and tools
instructions ="You are an email formatter and sender. You receive the body of an email to be sent. \
You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. \
Finally, you use the send_html_email tool to send the email with the subject and HTML body."

# Create the emailer agent with the defined instructions, tools, and model
emailer_agent = Agent(
    name="Email Manager",
    instructions=instructions,
    tools=email_tools,
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML and send it")