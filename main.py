from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
  <style>
    form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
        }}

        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }}
    </style>
  </head>
  <body>
    <form action="" method="post">
      <label>Rotate by:
        <input type="text" name="rot" value="0" />
      </label>
      <textarea name="text">{0}</textarea>
      <input type="submit" value="Submit Query" />
  </body>
</html>


"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    phrase = request.form['text']
    rotation = int(request.form['rot'])
    encrypt_phrase = rotate_string(phrase, rotation)
    return form.format(encrypt_phrase)


app.run()