import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] =''

email = "hey, your neighbor john here, your house seems to be on fire. this is not a joke."
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

classifier = Agent(
    role = "email classifier",
    goal = "accuratley classify emails based on their importance. give every email one of these ratings: important, casual, spam",
    backstory = "You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad rating if ther are not important. Your job is to help the user manage their inbox.",
    verbose = True,
    allow_delegation = False,
)

responder = Agent(
    role = "email responder",
    goal = "Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal reponse, if the email is rated 'casual' write a casual response, and if the email rated 'spam' ignore the email. no matter what, be very concise.",
    backstory = "You are an AI assistant whose only job is to respond to emails based on their importance. Do not be afraid to ignore emails that are not important. Your job is to help the user manage their inbox.",
    verbose = True,
    allow_delegation = False,
)

classify_email = Task(
    description = f"Classify the following email: '{email}'",
    agent = classifier,
    expected_output = "One of these three options: 'important', 'casual', 'spam'",
)

respond_to_email = Task(
    description = f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
    agent = responder,
    expected_output = "a very concise response to the email based on the importance provided by the 'classifier' agent.",
)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose = 2,
    process = Process.sequential
)

output = crew.kickoff()
print(output)