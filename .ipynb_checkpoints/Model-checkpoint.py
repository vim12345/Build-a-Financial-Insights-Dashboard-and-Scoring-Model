from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input data model
class FamilyData(BaseModel):
    Family_ID: str
    Income: float
    Savings: float
    Monthly_Expenses: float
    Loan_Payments: float
    Credit_Card_Spending: float
    Financial_Goals_Met: float
    Category: str
    Amount: float

# Scoring logic as a function
@app.post("/score")
def score_family(data: FamilyData):
    score = calculate_score(data)
    insights = {
        "Score": score,
        "Insights": [
            "Improve savings-to-income ratio." if data.Savings / data.Income < 0.2 else "",
            "Reduce monthly expenses to below 60% of income." if data.Monthly_Expenses / data.Income > 0.6 else "",
        ]
    }
    return insights

# Run the app
# Save this file as `app.py` and run: `uvicorn app:app --reload`
