
# agents/agent.py

class Agent:
    def __init__(self, agent_id, role):
        self.agent_id = agent_id
        self.role = role
        self.status = 'Susceptible'  # Possible statuses: 'Susceptible', 'Infected', 'Recovered'
        self.tools = []

    def assign_tools(self, tools):
        self.tools.extend(tools)

    def make_decision(self, context, agent_decision_function):
        decision = agent_decision_function(self, context)
        return decision
