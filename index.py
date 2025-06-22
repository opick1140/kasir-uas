from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
pesanan = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        menu = request.form.get("menu")
        if nama and menu:
            pesanan.append(f"{nama} - {menu}")
        return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/kasir", methods=["GET", "POST"])
def kasir():
    global pesanan
    if request.method == "POST":
        if pesanan:
            pesanan.pop(0)
        return redirect(url_for("kasir"))
    return render_template("kasir.html", pesanan=pesanan)