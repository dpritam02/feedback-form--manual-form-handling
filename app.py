from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/feedback", methods=["GEt","POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("Message")
        return render_template("thankyou.html", name=name, message=message)
    
    return render_template("feedback.html")
    
if __name__ == "__main__":
    app.run(debug = True, port = 5555, host = '0.0.0.0')