from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"

# Data
food_menu = [
    {"id": 1, "name": "Medialunas", "price": 2.00},
    {"id": 2, "name": "Facturas", "price": 3.00},
    {"id": 3, "name": "Empanadas", "price": 4.00},
    {"id": 4, "name": "Plain Churros", "price": 2.50},
    {"id": 5, "name": "Churros with Dulce de Leche or Chocolate", "price": 3.50},
    {"id": 6, "name": "Chocotorta Portion", "price": 7.00}
]

drinks_menu = [
    {"id": 7, "name": "Espresso", "price": 3.00},
    {"id": 8, "name": "Americano", "price": 4.50},
    {"id": 9, "name": "Latte", "price": 4.50},
    {"id": 10, "name": "Capuccino", "price": 5.00},
    {"id": 11, "name": "Matcha", "price": 5.50},
    {"id": 12, "name": "Mate", "price": 3.00}
]

promotions = [
    {"id": 13, "name": "Any Coffee + Medialuna", "price": 5.50},
    {"id": 14, "name": "6 Medialunas", "price": 10.00},
    {"id": 15, "name": "6 Churros", "price": 13.00},
    {"id": 16, "name": "6 Facturas", "price": 16.00},
    {"id": 17, "name": "6 Empanadas", "price": 20.00},
    {"id": 18, "name": "Whole Chocotorta", "price": 30.00}
]

daily_speciality = {
    "Monday": {"name": "Chipa (cheese bread)", "price": 4.00},
    "Tuesday": {"name": "Crusty sandwich", "price": 5.00},
    "Wednesday": {"name": "Pulled pork sandwich (slow cooked with Malbec)", "price": 10.00},
    "Thursday": {"name": "Focaccia", "price": 8.00},
    "Friday": {"name": "Choripan (Chorizo Sandwich with Chimichurri)", "price": 9.00},
    "Saturday": {"name": "Milanesa Sandwich (beef or chicken)", "price": 12.00},
    "Sunday": {"name": "Asado (Argentinian BBQ) - EXTRAS: Chimichurri/Salsa Criolla", "price": 20.00}
}


# Links
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/food")
def food():
    return render_template("food.html", food_menu=food_menu)

@app.route("/drinks")
def drinks():
    return render_template("drinks.html", drinks_menu=drinks_menu)

@app.route("/promotions")
def promo():
    return render_template("promotions.html", promotions=promotions)

@app.route("/special")
def special():
    today = datetime.now().strftime("%A")
    special_food = daily_speciality.get(today)
    return render_template("special.html", today=today, special=special_food)

@app.route("/order", methods=["GET", "POST"])
def place_order():
    if request.method == "POST":

        ...

    today = datetime.now().strftime("%A")
    return render_template(
        "order.html",
        food_menu=food_menu,
        drinks_menu=drinks_menu,
        promotions=promotions,
        daily_special=daily_speciality.get(today)
    )

if __name__ == "__main__":
    app.run(debug=True)