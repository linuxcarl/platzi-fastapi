from pydantic import BaseModel , EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    description: Optional[str] = None
    email: EmailStr
    age: int

class CustomerCreate(CustomerBase):
   pass

class Customer(CustomerBase):
    id: Optional[int] = None

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