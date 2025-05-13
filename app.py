from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ecommerce_secret_key'

# Sample Products
products = [
    {'id': 1, 'name': 'T-Shirt', 'price': 500},
    {'id': 2, 'name': 'Shoes', 'price': 1200},
    {'id': 3, 'name': 'Watch', 'price': 900}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
