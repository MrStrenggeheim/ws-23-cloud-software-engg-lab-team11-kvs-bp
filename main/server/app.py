from flask import Flask, current_app
from api import api
from ff import FileFolder


if __name__ == "__main__":
  try:
    app = Flask(__name__)
    with app.app_context():
      if not hasattr(current_app, "ff"):
        current_app.ff = FileFolder()
    app.register_blueprint(api)
    app.run(host="127.0.0.1", port=8080)
  except Exception as error:
    print(error)
  finally:
    with app.app_context():
      if hasattr(current_app, "ff"):
        current_app.ff.close()