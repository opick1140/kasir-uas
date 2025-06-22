from flask import Flask, render_template, request, redirect, url_for
import os

# Tentukan path ke folder templates yang sejajar dengan api/
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
app = Flask(__name__, template_folder=template_dir)
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
