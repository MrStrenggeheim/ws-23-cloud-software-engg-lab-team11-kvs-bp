import http.client
import json

# make json request to server
def json_request(method, path, body):
  conn.request(method, path, json.dumps(body), headers={"Content-Type": "application/json"})
  response = conn.getresponse()
  return response.read().decode()

#  Implementing CRUD methods
def create(user_id, key, value):
  request_body = {"uid": user_id, "content": value}
  response = json_request("POST", f"/{key}", request_body)
  return response

def read(user_id, key):
  request_body = {"uid": user_id, "content": ""}
  response = json_request("GET", f"/{key}", request_body)
  return response

def delete(user_id, key):
  request_body = {"uid": user_id, "content": ""}
  response = json_request("DELETE", f"/{key}", request_body)
  return response

def list(user_id):
  request_body = {"uid": user_id, "content": ""}
  response = json_request("GET", "/", request_body)
  return response


if __name__ == "__main__":
  # establish connection
  conn = http.client.HTTPConnection("127.0.0.1", 8080)
  
  # set user for DB
  user_id = 0

  # example usage
  print("Posting elements ...")
  create(user_id, "PGDP", "1.3")
  create(user_id, "DB", "1.0")
  create(user_id, "GBS", "1.7")
  
  print("Listing elements ...")
  print(list(user_id))

  print("Getting an element ...")
  response = read(user_id, "PGDP")
  print(response)

  print("Deleting GBS ...")
  response = delete(user_id, "GBS")
  print(response)

  print("Getting GBS ...")
  response = read(user_id, "GBS")
  print(response)

  # change user
  user_id = 1
  print("Getting PGDP ...")
  response = read(user_id, "PGDP")
  print(response)

  conn.close()
  pass



