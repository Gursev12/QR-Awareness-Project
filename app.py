from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR code
            qr = qrcode.make(url)
            img_io = io.BytesIO()
            qr.save(img_io, 'PNG')
            img_io.seek(0)

            # Convert image to base64 string for display in HTML
            qr_code = base64.b64encode(img_io.getvalue()).decode('utf-8')

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)