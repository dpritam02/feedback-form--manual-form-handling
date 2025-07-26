from flask import Flask, render_template, request,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = "my-secret-key"

# @app.route("/feedback", methods=["GEt","POST"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("Message")
#         return render_template("thankyou.html", name=name, message=message)
    
#     return render_template("feedback.html")

@app.route("/", methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("Name can't be empty!")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, your feedback got saved")
        return redirect(url_for("thankyou"))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
    
if __name__ == "__main__":
    app.run(debug = True, port = 5555, host = '0.0.0.0')