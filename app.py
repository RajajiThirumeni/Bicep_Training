from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ACA Demo Calculator Upadted one</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 500px;
                margin: 60px auto;
                text-align: center;
            }

            input, select, button {
                padding: 10px;
                margin: 8px;
                font-size: 16px;
            }

            .result {
                margin-top: 25px;
                font-size: 24px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <h1>Upadted V5 Now</h1>

        <form action="/calculate" method="get">
            <input type="number" name="num1" placeholder="Number 1" required>

            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">×</option>
                <option value="divide">÷</option>
            </select>

            <input type="number" name="num2" placeholder="Number 2" required>

            <br>

            <button type="submit">Calculate</button>
        </form>

        <p>Version: v3</p>
    </body>
    </html>
    """

@app.route("/calculate")
def calculate():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    operation = request.args.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2

    return f"""
    <html>
    <body style="font-family: Arial; text-align: center; margin-top: 60px;">
        <h1>ACA Demo Calculator</h1>
        <div style="font-size: 28px; margin: 30px;">
            Result: {result}
        </div>
        <a href="/">Back to Calculator</a>
        <p>Version: v1</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "Healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)