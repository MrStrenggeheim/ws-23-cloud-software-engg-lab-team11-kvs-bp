from flask import Flask, g
from api import api
from ff import FileFolder


app = Flask(__name__)
app.register_blueprint(api)
ff = FileFolder()


@app.before_request
def request_inject():
  g.ff = ff


if __name__ == "__main__":
  try:
    app.run(debug=True, port=8080)
  except Exception as error:
    print(error)
  finally:
    ff.close()