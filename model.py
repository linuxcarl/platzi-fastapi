from pydantic import BaseModel , EmailStr
from typing import Optional
from sqlmodel import SQLModel, Field  

class CustomerBase(SQLModel):
    name: str = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    email: EmailStr = Field(default=None, max_length=100)
    age: int = Field(default=None, ge=0, le=120)

class CustomerCreate(CustomerBase):
   pass

class Customer( CustomerBase, table=True):
    id: int = Field(default=None, primary_key=True)

class Transaction(BaseModel):
    id: int
    amount: float
    description: Optional[str] = None

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction] = []
    total: int

    @property
    def amount_total(self):
        return sum(transaction.amount for transaction in self.transactions)