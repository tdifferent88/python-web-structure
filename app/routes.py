print(" ROUTES IMPORTADO ")

from flask import Blueprint, render_template, request, redirect
from app.database import SessionLocal
from app.models import Projeto

main = Blueprint("main", __name__)

@main.route("/projetos")
def listar():
    db = SessionLocal()
    projetos = db.query(Projeto).all()
    db.close()
    return render_template("projetos.html", projetos=projetos)


@main.route("/projetos/novo", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        db = SessionLocal()

        novo = Projeto(
            nome=request.form.get("nome"),
            descricao=request.form.get("descricao")
        )

        db.add(novo)
        db.commit()
        db.close()

        return redirect("/projetos")

    return render_template("novo.html")