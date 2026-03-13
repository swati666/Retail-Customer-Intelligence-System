from pydantic import BaseModel

class CustomerFeatures(BaseModel):
    frequency: float
    monetary: float
    total_quantity: float
    avg_spend: float