from flask import Flask, render_template, request,redirect,url_for,flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secret-key"

#----- for handling manual form------
# @app.route("/feedback", methods=["GEt","POST"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("Message")
#         return render_template("thankyou.html", name=name, message=message)
#     return render_template("feedback.html")

#--------- for handling flash and flash message--------
# @app.route("/", methods=["GET","POST"])
# def form():
#     if request.method == "POST":
#         name = request.form.get("name")
#         if not name:
#             flash("Name can't be empty!")
#             return redirect(url_for("form"))
#         flash(f"Thanks {name}, your feedback got saved")
#         return redirect(url_for("thankyou"))
#     return render_template("form.html")
# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")

#----------- for handling flask-wtf--------
@app.route("/", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name}!, you have registered successfully","success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

    
if __name__ == "__main__":
    app.run(debug = True, port = 5555, host = '0.0.0.0')