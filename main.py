from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from zoneinfo import ZoneInfo
from model import CustomerCreate, Transaction, Invoice, Customer
from db import SessionDependency, create_all_tables
from sqlmodel import select



app = FastAPI(lifespan=create_all_tables)

@app.get("/")
async def root():
    return {"message": "Hello, python fast api!"}

country_timezones = {
    "US": "America/New_York",
    "CA": "America/Toronto",
    "GB": "Europe/London",
    "FR": "Europe/Paris",
    "DE": "Europe/Berlin",
    "JP": "Asia/Tokyo",
    "BR": "America/Sao_Paulo",
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "AR": "America/Argentina/Buenos_Aires"
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso_code = iso_code.upper()
    timezone_str = country_timezones.get(iso_code, "UTC")
    tz = ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}

#variable para almacenar los clientes emaulando una base de datos
db_customers: list[Customer] = []
@app.post("/customer", response_model=Customer)
async def createCustomer(customer_data: CustomerCreate, session: SessionDependency):
    #customer_id = len(db_customers) + 1
    #customer = Customer(id=customer_id, **customer_data.model_dump())
    #db_customers.append(customer)
    customer = Customer.model_validate(customer_data)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get("/customers", response_model=list[Customer])
async def getCustomers(session: SessionDependency):
  customers = session.exec(select(Customer)).all()
  return customers

@app.get("/customers/{id}", response_model=Customer)
async def getCustomers(id: int, session: SessionDependency):
  customer_db = session.get(Customer, id)
  if not customer_db:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
  return customer_db

@app.delete("/customers/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteCustomer(id: int, session: SessionDependency):
    customer_db = session.get(Customer, id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    session.delete(customer_db)
    session.commit()
    return None

@app.post("/transactions")
async def createTransaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoices")
async def createInvoices(invoice_data: Invoice):
    return invoice_data