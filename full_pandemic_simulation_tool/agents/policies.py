
# agents/policies.py

policies = {
    'No Intervention': {
        'contact_rate': 1.0  # Full contact
    },
    'Social Distancing': {
        'contact_rate': 0.5  # Reduced contact
    },
    'Lockdown': {
        'contact_rate': 0.1  # Minimal contact
    },
}

def get_policy(policy_name):
    return policies.get(policy_name, {})
