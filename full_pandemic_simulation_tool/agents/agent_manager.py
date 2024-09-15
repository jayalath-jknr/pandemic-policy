
# agents/agent_manager.py

from crewai import AgentManager
from agents.agent import Agent
from agentops import AgentMonitor

# Initialize Agent Manager
agent_manager = AgentManager()

# Define agent roles
roles = ['Citizen', 'HealthcareWorker', 'PolicyMaker']

# Register agents
for role in roles:
    agent_manager.register_agent(role_name=role)

# Function to create agents
def create_agents(number):
    agents = []
    for i in range(number):
        agent_role = 'Citizen'  # For simplicity, all are citizens
        agent = Agent(agent_id=i, role=agent_role)
        agents.append(agent)
        agent_manager.add_agent(agent)
    return agents

# Initialize Agent Monitor
def start_agent_monitoring():
    agent_monitor = AgentMonitor(agents=agent_manager.get_all_agents())
    agent_monitor.start_monitoring()

# Start monitoring agents
start_agent_monitoring()
