from agents.sql_agent import get_sql_agent
from agents.policy_agent import get_policy_response

sql_agent = get_sql_agent()

def route_query(query: str):
    query_lower = query.lower()

    if any(word in query_lower for word in ["policy", "refund", "terms", "document"]):
        return get_policy_response(query)

    elif any(word in query_lower for word in ["customer", "ticket", "profile", "ema", "daniel", "sarah"]):
        return sql_agent.run(query)

    else:
        return "I'm not sure which data source to use for this question."
