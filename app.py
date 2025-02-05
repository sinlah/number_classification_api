import json
from flask import Flask, request, jsonify, Response
import requests
import math
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


def extract_indv_digits(n):
    digits = [int(d) for d in n if d.isdigit()]  #extract only digits
    if n.startswith('-'):  #if the number was originally negative, restore the negative sign for the first digit
        digits[0] *= -1
    return digits


def is_prime(n):
    if n < 2 or type(n) == float:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n < 2 or type(n) == float:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n


def is_armstrong(n):
    digits = extract_indv_digits(n)
    if digits[-1] == 0:
        digits.pop()
    num_digits = len(digits)
    return int(float(n)) == sum(d ** num_digits for d in digits)


def digit_sum(n):
    return sum(extract_indv_digits(n))


def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get('text', f'No fun fact about {n} available.')
    return f'No fun fact about {n} available.'


#default route for Render health check
@app.route('/')
def home():
    return "Number Classification API is running!"


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')
    #validate input: ensure number is a valid float or integer
    try:
        number_float = float(number_str)  #convert to float
    except (ValueError, TypeError):
        #return jsonify({"number": number_str, "error": "Invalid input. Please provide a valid number."}), 400
        return Response(json.dumps({"number": number_str, "error": "Invalid input. Please provide a valid number."}), mimetype="application/json"), 400
    #if the number is an integer, convert it to int (to remove decimals like .0)
    number = int(number_float) if number_float.is_integer() else number_float

    properties = []
    if is_armstrong(number_str):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number_str),
        "fun_fact": get_fun_fact(number)
    }
    return Response(json.dumps(response, ensure_ascii=False), mimetype="application/json"), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)