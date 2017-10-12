from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route("/")
def hello():
    file_path = "AMAT Financial Condition Analysis Report.pdf"
    file = open(file_path, 'rb')
    # with open(file_path) as f:
    #     file = f.read()
    # return render_template("hello.html", name=file_path)
    return Response(
        file,
        mimetype="text/pdf",
        headers={"Content-disposition":
                     "attachment; filename=myplot.pdf"})