# This code is going to generate a API with flask to show the Meny of an Argentinian Bakery
# By Ignacio Riboldi

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to the Argentinian Bakery</h1>
    <p>Food menu: /food</p>
    <p>Drinks menu: /drinks</p>
    <p>Promotions: /promotions</p>
    """

@app.route('/food')
def food_menu():
    return '''
    <h1>Argentinian Bakery Food Menu</h1>
    <ul>
        <li>Medialunas - $2.00</li>
        <li>Facturas - $3.00</li>
        <li>Empanadas - $4.00</li>
        <li>Churros - $2.50</li>
        <li>Chocotorta Portion - $5.00</li>
    </ul>
    '''

@app.route('/drinks')
def drinks_menu():
    return '''
    <h1>Argentinian Bakery Drinks Menu</h1>
    <ul>
        <li>Espresso - $3.00</li>
        <li>Americano - $4.50</li>
        <li>Latte - $4.50</li>
        <li>Capuccino - $5.00</li>
        <li>Matcha - $5.50</li>
        <li>Mate - $3.00</li>
    </ul>
    '''
@app.route('/promotions')
def promotions_menu():
    return '''
    <h1>Argentinian Bakery Promotions</h1>
    <ul>
        <li>Any Coffee + Medialuna - $5.50</li>
        <li>6 Medialunas - $10.00</li>
        <li>6 Churros - $13.00</li>
        <li>6 Facturas - $16.00</li>
        <li>6 Empanadas - $20.00</li>
        <li>Chocotorta - $30.00</li>
    </ul>
    '''


if __name__ == '__main__':    
    app.run(debug=True)