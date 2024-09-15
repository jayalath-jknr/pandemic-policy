
# agents/composio_tools.py

from composio import ToolKit
from agents.agent_manager import agent_manager

def initialize_composio_tools():
    # Initialize Composio ToolKit
    toolkit = ToolKit()

    # Assign tools to agents
    for agent in agent_manager.get_all_agents():
        tools = toolkit.get_tools_for_role(agent.role)
        agent.assign_tools(tools)
