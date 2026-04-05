from app_agents import sales_agent1, sales_agent2, sales_agent3, subject_writer, html_converter

# Convert the sales agents to tools with descriptions
description = "Write a cold sales email"
sales_tool_1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)
sales_tool_2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description=description)
sales_tool_3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description=description)

# Convert the subject writer agent to tools with descriptions
subject_writer_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")

# Convert the HTML converter agent to a tool with description
html_converter_tool = html_converter.as_tool(tool_name="html_converter", tool_description="Convert a text email body to an HTML email body")