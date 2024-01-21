from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def homeRoute():
    resData = {
        "name": "David M.",
        "roll": 456,
        "isPassed": False
    }
    return jsonify(resData)

@app.route("/products")
def getProducts():
    productUrl = "https://dummyapi.online/api/products"
    try:
        productResponse = requests.get(productUrl)
        jsonData = productResponse.json()
        return {
            'isError':False,
            'message':"Products retrived successfully",
            "products": jsonData
        }
    except requests.exceptions.RequestException as e:
        return jsonify({'isError':True,'message':"Failed to get poducts"})

if __name__ == '__main__':
    app.run(debug=True)