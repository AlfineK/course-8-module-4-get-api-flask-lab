from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"Message":"Welcome to a list of products"}) # TODO: Return a welcome message

# TODO: Implement GET /products route that returns all products or filters by category
@app.route('/products',methods=['GET'])
def get_products():
    category=request.args.get("category")
    if category:
        filtered=[item for item in products if item['category']==category]
        return jsonify(filtered),200
    return jsonify(products),200


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for item in products:# TODO: Return product by ID or 404
        if  item['id']==id:
            return jsonify(item),200
    return jsonify({"Message":"product not found"}) ,404

if __name__ == "__main__":
    app.run(debug=True)
