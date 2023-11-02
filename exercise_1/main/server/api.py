from flask import Blueprint, request, current_app
from ff import Entry


api = Blueprint("api", __name__, template_folder="templates")


@api.route("/<key>", methods=["GET"])
def get(key):
  value = current_app.ff.get(key)
  if value is None:
    return "Key %s does not exist" % key
  request_body = request.json
  print(request_body)
  if "uid" not in request_body:
    return "No 'uid' in request body. The request must provide user id"
  uid = request_body["uid"]
  if value.uid != uid:
    return "Cannot access the content associated with key %s owned by other user" % key
  return value.content


@api.route("/<key>", methods=["POST"])
def put(key):
  request_body = request.json
  if "uid" not in request_body:
    return "No 'uid' in request body. The request must provide user id"
  if "content" not in request_body:
    return "No 'content' in request body. The request must provide the content"
  uid = request_body["uid"]
  content = request_body["content"]
  value = current_app.ff.get(key)
  if value is None:
    success = current_app.ff.put(key, Entry(uid, content))
    if success:
      return "Successfully added the content"
    else:
      return "Failed to add the content due to full space"
  else:
    if value.uid != uid:
      return "Cannot update the content associated wtih key %s owned by other user" % key
    else:
      current_app.ff.put(key, Entry(uid, content))
      return "Successfully updated the content"


@api.route("/<key>", methods=["DELETE"])
def remove(key):
  request_body = request.json
  if "uid" not in request_body:
    return "No 'uid' in request body. The request must provide user id"
  uid = request_body["uid"]
  if current_app.ff.get(key).uid != uid:
    return "Cannot delete the content associated with key %s owned by other user" % key
  value = current_app.ff.remove(key)
  if value is None:
    return "Key %s does not exist" % key
  return value.content


@api.route("/", methods=["GET"])
def list():
  request_body = request.json
  if "uid" not in request_body:
    return "No 'uid' in request body. The request must provide user id"
  uid = request_body["uid"]
  items = []
  for key, value in current_app.ff.items():
    if value.uid == uid:
      items.append((key, value.content))
  return items
