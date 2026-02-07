from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define the state of the  agent
class AgentState(TypedDict):
    customer_data: dict
    churn_probability: float
    review_status: str

# Node 1: Analyze behavior (for Simulating 92% accuracy model)
def analyze_behavior(state: AgentState):
    state['churn_probability'] = 0.85 
    return state

# Node 2: Reviewer node to prevent hallucinations
def review_analysis(state: AgentState):
    state['review_status'] = "High Risk - Approved" if state['churn_probability'] > 0.8 else "Low Risk"
    return state

workflow = StateGraph(AgentState)
workflow.add_node("analyze", analyze_behavior)
workflow.add_node("review", review_analysis)
workflow.set_entry_point("analyze")
workflow.add_edge("analyze", "review")
workflow.add_edge("review", END)

app = workflow.compile()
