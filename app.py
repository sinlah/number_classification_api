import json
from flask import Flask, request, jsonify, Response
import requests
import math
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return n == sum(d ** num_digits for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get('text', f'No fun fact about {n} available.')
    return 'No fun fact available.'

#default route for Render health check
@app.route('/')
def home():
    return "Number Classification API is running!"


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"number": request.args.get('number'), "error": True}), 400

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # #use OrderedDict to preserve the exact key order
    # response = OrderedDict([
    #     ("number", number),
    #     ("is_prime", is_prime(number)),
    #     ("is_perfect", is_perfect(number)),
    #     ("properties", properties),
    #     ("digit_sum", digit_sum(number)),
    #     ("fun_fact", get_fun_fact(number))
    # ])

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return Response(json.dumps(response, ensure_ascii=False), mimetype="application/json"), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)