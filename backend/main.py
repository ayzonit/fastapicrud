from fastapi import FastAPI
from models import Product
from database import session
import database_model

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to app"

products = [Product(id=1, name="board", description="a plastic board", price=57.85, quantity=5),
            Product(id=2, name="mouse", description="a computer mouse", price=65.50, quantity=8)]

@app.get("/products")
def getAllProducts():
    db = session()
    
    return products


@app.get("/product/{id}")
def getProductById(id: int):
    for product in products:
        if product.id == id:
            return product
            
    return "product not found"


@app.put("/product")
def updateProduct(id: int, product: Product):
    for i in range(lens(products)) :
        if(product[i].id) == id:
            products[i] = product
            return "Product added successfully"
        
    return "product not found"