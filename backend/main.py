from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session 

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


products = [Product(id=1, name="board", description="a plastic board", price=57.85, quantity=5),
            Product(id=2, name="mouse", description="a computer mouse", price=65.50, quantity=8)]


def init_db():
   db = session()
   for product in products:
       db.add(database_model.Product(**product.model_dump()))
   db.commit()
init_db()


@app.get("/")
def greet():
    return "Welcome to app"


@app.get("/products")
def getAllProducts(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products


@app.get("/product/{id}")
def getProductById(id: int, db: Session = Depends(get_db)):
    db_Product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_Product:
        return db_Product
    return "product not found"


@app.put("/product")
def updateProduct(id: int, product: Product):
    for i in range(len(products)) :
        if(product[i].id) == id:
            products[i] = product
            return "Product added successfully"
        
    return "product not found"


        