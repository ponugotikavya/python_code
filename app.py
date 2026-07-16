from flask import Flask, render_template

app = Flask(__name__)

sarees = [
    {
        "name":"Royal Blue Silk Saree",
        "price":"₹1499"
    },
    {
        "name":"Pink Banarasi Saree",
        "price":"₹1899"
    },
    {
        "name":"Green Cotton Saree",
        "price":"₹999"
    },
    {
        "name":"Yellow Soft Silk Saree",
        "price":"₹1599"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/collection")
def collection():
    return render_template("collection.html", sarees=sarees)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
