
# models/llama31_integration.py

from llama3 import Llama31Model
from config.settings import LLAMA31_API_KEY

# Initialize Llama 3.1 model
llama_model = Llama31Model(api_key=LLAMA31_API_KEY)

def agent_decision(agent, context):
    # Create a prompt for the LLM
    prompt = create_prompt(agent, context)
    response = llama_model.generate_response(prompt)
    decision = parse_response(response)
    return decision

def create_prompt(agent, context):
    # Build a prompt based on agent's role and context
    prompt = f"Agent Role: {agent.role}\n"
    prompt += f"Agent Status: {agent.status}\n"
    prompt += f"Policy: {context['policy_name']}\n"
    prompt += "What should the agent do next?"
    return prompt

def parse_response(response):
    # Parse the LLM's response into actionable decisions
    return response.strip()
