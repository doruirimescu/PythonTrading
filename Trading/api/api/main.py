from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional
import Trading.loan.loan as loan

load_dotenv()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
orchestrators_dict = {}
sid_username_dict = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/loan/history")
def loan_history():
    return loan.loan_history()

@app.get("/loan/total/principal_paid")
def principal_paid():
    return {"total_principal_paid": loan.principal_paid()}

@app.get("/loan/cumulative/principal_paid")
def principal_paid():
    return {"cumulative_principal_paid": loan.cumulative_principal_paid()}

@app.get("/loan/total/interest_paid")
def interest_paid():
    return {"interest_paid": loan.interest_paid()}

@app.get("/loan/total/cost_paid")
def cost_paid():
    return {"cost_paid": loan.cost_paid()}

@app.get("/loan/total/principal")
def total_principal():
    return  {"total": loan.principal_total()}

@app.get("/loan/interest_rate")
def interest_rate():
    return {"value": loan.get_interest_rate()}
