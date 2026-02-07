from fastapi import FastAPI
from pydantic import BaseModel
from graph import app as agent_graph

app = FastAPI(title="Agentic Churn Intelligence API")

class CustomerInput(BaseModel):
    name: str
    usage_score: float

@app.post("/predict")
async def predict_churn(data: CustomerInput):
    # This invokes your LangGraph workflow
    initial_state = {
        "customer_data": data.dict(), 
        "churn_probability": 0.0, 
        "review_status": "Pending"
    }
    result = agent_graph.invoke(initial_state)
    return {
        "customer": data.name, 
        "risk": result['churn_probability'], 
        "status": result['review_status']
    }
