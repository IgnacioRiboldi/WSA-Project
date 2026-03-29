from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Datos
food_menu = [
    {"id": 1, "name": "Medialunas", "price": 2.00},
    {"id": 2, "name": "Facturas", "price": 3.00},
    {"id": 3, "name": "Empanadas", "price": 4.00},
    {"id": 4, "name": "Churros", "price": 2.50},
    {"id": 5, "name": "Chocotorta Portion", "price": 7.00}
]

drinks_menu = [
    {"id": 6, "name": "Espresso", "price": 3.00},
    {"id": 7, "name": "Americano", "price": 4.50},
    {"id": 8, "name": "Latte", "price": 4.50},
    {"id": 9, "name": "Capuccino", "price": 5.00},
    {"id": 10, "name": "Matcha", "price": 5.50},
    {"id": 11, "name": "Mate", "price": 3.00}
]

promotions = [
    {"id": 12, "name": "Any Coffee + Medialuna", "price": 5.50},
    {"id": 13, "name": "6 Medialunas", "price": 10.00},
    {"id": 14, "name": "6 Churros", "price": 13.00},
    {"id": 15, "name": "6 Facturas", "price": 16.00},
    {"id": 16, "name": "6 Empanadas", "price": 20.00},
    {"id": 17, "name": "Whole Chocotorta", "price": 30.00}
]

daily_speciality = {
    "Monday": "Chipa (cheese bread)",
    "Tuesday": "Crusty sandwich",
    "Wednesday": "Pulled pork sandwich (slow cooked with Malbec)",
    "Thursday": "Focaccia",
    "Friday": "Choripan (Chorizo Sandwich with Chimichurri)",
    "Saturday": "Milanesa Sandwich (beef or chicken)",
    "Sunday": "Asado (Argentinian BBQ)"
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

if __name__ == "__main__":
    app.run(debug=True)