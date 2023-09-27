from flask import Blueprint, render_template, request, redirect
from website import mysql
from datetime import datetime

views = Blueprint("views", __name__)


@views.route("/")
def index():
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM notes")
    allNotes = cursor.fetchall()
    for note in allNotes:
        print(note)
    cursor.close()
    return render_template("home.html", allNotes=allNotes)


@views.route("/newNote", methods=["POST", "GET"])
def newNote():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        created_on = datetime.now()

        cursor = mysql.cursor()
        cursor.execute(
            "INSERT INTO notes(title,content,created_on) VALUES(%s,%s,%s)",
            (title, content, created_on),
        )
        mysql.commit()
        cursor.close()
        return redirect("/")

    return render_template("create.html")


# render note or update note
@views.route("/note/<noteId>", methods=["POST", "GET"])
def renderNote(noteId):
    cursor = mysql.cursor()
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        created_on = datetime.now()
        cursor.execute(
            "update notes set title=%s,content=%s,created_on=%s where _id=%s  ",
            (title, content, created_on, noteId),
        )
        mysql.commit()
        return redirect("/")

    cursor.execute(f"select * from notes where _id={noteId}")
    note = cursor.fetchone()
    cursor.close()
    return render_template("note.html", note=note)


@views.route("/delete/<noteId>")
def deleteNote(noteId):
    cursor = mysql.cursor()
    cursor.execute(f"delete from notes where _id={noteId}")
    mysql.commit()
    cursor.close()
    return redirect("/")
