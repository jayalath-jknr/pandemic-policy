
# simulations/simulation.py

import pandas as pd
import random
from agents.agent_manager import create_agents
from agents.policies import get_policy
from models.llama31_integration import agent_decision
from config.settings import (
    DEFAULT_INITIAL_INFECTED,
    DEFAULT_SIMULATION_DAYS,
    DEFAULT_INFECTION_RATE,
    DEFAULT_RECOVERY_RATE,
)

def run_simulation(policy_name, population_size, simulation_days):
    policy = get_policy(policy_name)
    results = []

    # Initialize agents
    agents = create_agents(population_size)

    # Infect initial agents
    for agent in agents[:DEFAULT_INITIAL_INFECTED]:
        agent.status = 'Infected'

    # Run simulation
    for day in range(simulation_days):
        day_data = {'Day': day + 1, 'Susceptible': 0, 'Infected': 0, 'Recovered': 0}

        for agent in agents:
            context = {
                'policy_name': policy_name,
                'policy': policy,
                'day': day + 1
            }

            if agent.status == 'Infected':
                # Determine if agent recovers
                if should_recover():
                    agent.status = 'Recovered'
            elif agent.status == 'Susceptible':
                # Determine if agent gets infected based on interactions
                if should_be_infected(agent, agents, policy):
                    agent.status = 'Infected'

            # Agent makes a decision (not fully implemented)
            agent.make_decision(context, agent_decision)

            # Collect data
            if agent.status == 'Susceptible':
                day_data['Susceptible'] += 1
            elif agent.status == 'Infected':
                day_data['Infected'] += 1
            elif agent.status == 'Recovered':
                day_data['Recovered'] += 1

        results.append(day_data)

    return pd.DataFrame(results)

def should_recover():
    return random.random() < DEFAULT_RECOVERY_RATE

def should_be_infected(agent, agents, policy):
    contact_rate = policy.get('contact_rate', 1.0)
    infection_chance = DEFAULT_INFECTION_RATE * contact_rate
    return random.random() < infection_chance
