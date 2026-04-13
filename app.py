from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def reverse():
    result = ""

    if request.method == "POST":
        text = request.form.get("text")
        result = text[::-1]

    return render_template("reverse.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
