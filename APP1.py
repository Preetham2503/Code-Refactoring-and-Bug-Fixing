from flask import Flask, render_template, request, session

app = Flask(__name__)


app.secret_key = "1a2b3c4d5e6f7g8h9i0j"  

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        
        notes = session.get("notes", [])
    else:
        
        note = request.form.get("note")
        if note:
            notes = session.get("notes", []) 
            notes.append(note)
            session["notes"] = notes 
        return render_template("home.html", notes=notes)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
