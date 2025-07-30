from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Template load failed: {e}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)