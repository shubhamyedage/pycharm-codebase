from flask import Flask, render_template, redirect, url_for, Response, make_response
import base64

app = Flask(__name__)


# @app.route('/app')
# def show_entries():
#     with open('Report.pdf', 'rb') as static_file:
#         return send_file(
#             static_file,
#             'application/pdf',
#             as_attachment=True,
#             attachment_filename='file.pdf'
#         )
#     # return render_template('main.html')
#
#
# @app.route('/app', methods=['POST'])
# def add_entry():
#     return redirect(url_for('main'))


@app.route("/")
def index():
    return render_template("hello.html")


@app.route("/app=<name>", methods=["GET"])
def generate_report(name):
    print(name)
    return "/static/Report.pdf"
