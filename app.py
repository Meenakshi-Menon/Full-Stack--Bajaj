from flask import Flask, request, jsonify
from collections import OrderedDict


app = Flask(__name__)

# Update with your info
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def process_input(data):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    num_sum = 0
    concat_alpha = []

    for item in data:
        item_str = str(item)
        if item_str.isdigit():
            num = int(item_str)
            if num % 2 == 0:
                even_numbers.append(item_str)
            else:
                odd_numbers.append(item_str)
            num_sum += num
        elif item_str.isalpha():
            alphabets.append(item_str.upper())
            concat_alpha.append(item_str)
        elif not item_str.isalnum():
            special_characters.append(item_str)

    # Concatenation, reverse, alternating caps
    concat_string_raw = ''.join(concat_alpha)[::-1]
    concat_string = ''.join([
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(concat_string_raw)
    ])

    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(num_sum),
        "concat_string": concat_string
    }

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        result = process_input(data)
        response = OrderedDict([
            ("is_success", True),
            ("user_id", f"{FULL_NAME}_{DOB}"),
            ("email", EMAIL),
            ("roll_number", ROLL_NUMBER),
            ("odd_numbers", result["odd_numbers"]),
            ("even_numbers", result["even_numbers"]),
            ("alphabets", result["alphabets"]),
            ("special_characters", result["special_characters"]),
            ("sum", result["sum"]),
            ("concat_string", result["concat_string"])])
        return jsonify(response), 200

        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "error": str(e)
        }), 400
    


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


