import math
from fractions import Fraction
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "to_radians/number"

@app.route('/to_radians/<int:x>')
def toRadians(x):
    integer = math.radians(x)
    return f"{Fraction.from_float(integer).limit_denominator(10)} იგივე რაც {integer} რადიანი"

if __name__ == '__main__':
    app.run(port=8080, debug=True)