from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os

app = Flask(__name__)

# Folder jithe QR codes save honge
QR_FOLDER = "static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    qr_img_path = None
    if request.method == "POST":
        user_input = request.form["data"]

        # Awareness URL da demo
        if user_input.strip() == "":
            user_input = "https://your-awareness-demo.com"

        # QR Code generate karna
        qr = qrcode.make(user_input)
        qr_img_path = os.path.join(QR_FOLDER, "qr_demo.png")
        qr.save(qr_img_path)

        qr_img_path = "/" + qr_img_path  # for HTML render

    return render_template("index.html", qr_img_path=qr_img_path)


@app.route("/awareness")
def awareness():
    return "<h2 style='color:red;'>⚠️ Beware! QR codes can be misused for phishing. This is only a demo for educational purposes.</h2>"


if __name__ == "__main__":
    app.run(debug=True)
