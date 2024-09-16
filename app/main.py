from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from app.services.formula_service import execute_formulas

app = FastAPI()

# Request data schema
class DataEntry(BaseModel):
    id: int
    fieldA: float = None
    fieldB: float = None
    unitPrice: str = None
    quantity: int = None
    discount: str = None
    product: str = None

class Formula(BaseModel):
    outputVar: str
    expression: str
    inputs: list

class FormulaRequest(BaseModel):
    data: list[DataEntry]
    formulas: list[Formula]

@app.post("/api/execute-formula")
def execute_formula(payload: FormulaRequest):
    try:
        result = execute_formulas(payload.data, payload.formulas)
        return {
            "results": result,
            "status": "success",
            "message": "The formulas were executed successfully."
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")
