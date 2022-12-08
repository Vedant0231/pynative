from fastapi import FastAPI ,Path
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
app = FastAPI()

# product_data ={
#     "phones":["samsung","iphone","google pixle"],
#     "laptops":["lenovo","samsung","macbook"],
#     "watches":["apple watch","samsung watch","pixle watch"]
# }
# valid_data = product_data.keys()

# @app.get("/")
# def hello():
#     return "welcome user"

# @app.get("/about")
# def about():
#     return "my name is vedant and this is my first api"

# @app.get("/product/{product}")
# def product(product,):
#     if product not in valid_data:
#         return f"Sorry sir we don't have this product right now but you can check this ones  {valid_data}"
#     return product_data.get(product)    


# @app.get("/html",response_class= HTMLResponse)
# def file():
#     return"""
#     <html>
#     <head>
#     <title>
#     this is html page
#     </title>
#     </head>
#     <body>
#     <h1> this page is render</h1>
#     </body>
#     </html>
#     """

# @app.post("userinfo")
inventory={
    1: {
        "name":"milk",
        "price":210,
        "brand":"amul"

    }
}

class Iteam(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

@app.get("/iteam/{iteam_id}")
def iteam(iteam_id:int=Path(None,description="this id of iteam you like to view",gt=0 )):
    return  inventory[iteam_id]

#quary peramater
@app.get("/get-by-name")
def get_iteam(*,name: Optional[str]= None , iteam:  int):
    for iteam_id in inventory:
        if inventory[iteam_id]["name"] == name:
            return inventory[iteam_id]
    return "data not found"

@app.post("/create-iteam/{iteam_id}")
def create_iteam(iteam_id:int,iteam:Iteam):
    if iteam_id in inventory:
        return "id is already saved"
    inventory[iteam_id]={"name":iteam.name,"price":iteam.price,"brand":iteam.brand}
    return inventory[iteam_id] 

# @app.put("/update-iteam/{iteam_id}")
# def update_iteam(iteam_id:int,iteam:Iteam):
#     if iteam_id not in inventory:
#         return "not in inventory"

#     if iteam.name !=None:
#         inventory[iteam_id]=iteam.name
#     if iteam.price !=None:
#         inventory[iteam_id]=iteam.price 
#     if iteam.brand !=None:
#         inventory[iteam_id]=iteam.brand
#     return inventory[iteam_id]

