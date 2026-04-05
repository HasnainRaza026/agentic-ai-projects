from dotenv import load_dotenv
from agents import function_tool
from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

# Load environment variables from .env file
load_dotenv()
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

# Define the function tool for sending HTML emails
@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("sender@example.com")  # Change to your verified sender
    to_email = To("recipient@example.com")  # Change to your recipient
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}