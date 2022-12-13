from flask import Flask, request, abort 
import json
import random 
from config import me 
from mock_data import catalog

app = Flask("server")

@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is another endpoint"


@app.get("/about")
def about():
    return "David Lively"


    #################################################
    ##############  Catalog API  ####################
    #################################################

@app.get("/api/version")
def version():
        version= {
            "v": "v1.0.4",
            "name": "zombie rabbit"
        }
        return json.dumps(version)


    #get /api/about
    # return me as json

@app.get("/api/about")
def api_about():
        return json.dumps(me)


# get /api/catalog
# returns the catalog as json
# try it in browser

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

# POST /api/catalog
@app.post("/api/catalog")
def save_product():
    product = request.get_json()

    # validations

    if "title" not in product:
        return abort(400, "Title is required")

    # the title should have at least characters
    if len(product["title"]) <5:
        return abort(400, "Title should contain 5 characters or more")

    # must have a category
    if "category" not in product:
        return abort(400, "Category is required")

    # must have a price

    if "price" not in product:
        return abort(400, "Price is required")

    if not isinstance(product["price"], (float, int) ):
        return abort(400, "Price is invalid" )

    # the price should be greater than 0
    if product["price"] < 0:
        return abort(400, "Price must be greater than 0")



    #assign a unique _id to product
    product["_id"] = random.randint(1000, 10000)

    catalog.append(product)

    return json.dumps(product)

#get /api/test/count
#return the number of products in the list

@app.get("/api/test/count")
def num_of_products():
    return len(catalog)


# GET /api/catalog/<category>
# return all of the products that belong to spefific category

@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            results.append(product)

    return json.dumps(results)


#GET /api/catalog/search/<text>
# return products whose title contains the text

@app.get("/api/catalog/search/<text>")
def search_by_text(text):
    text = text.lower()
    results = []

    for product in catalog:
        if text in product["title"].lower() or text in product["category"].lower():
            results.append(product)

    return json.dumps(results)



@app.get("/api/categories")
def get_categories():
    results = []
    for product in catalog:
        cat = product["category"]
        if cat not in results:
           results.append(cat)

    return json.dumps(results)


@app.get("/api/test/value")
def total_value():
    total = 0
    for product in catalog:
        total = total + product["price"]


    return json.dumps(total)


@app.get("/api/product/cheapest")
def search_cheapest():
    cheapest = catalog[0]
    for product in catalog:
        if product ["price"] < cheapest["price"]:
            cheapest = product


    return json.dumps(cheapest)



@app.get("/api/product/<id>")
def search_by_id (id):
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "Error: Product not found"


  

  



app.run(debug=True)



