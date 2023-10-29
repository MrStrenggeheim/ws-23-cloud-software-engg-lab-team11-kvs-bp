from sqlitedict import SqliteDict


def write(source):
  db = SqliteDict(source)
  db["1"] = {"name": "first item"}
  db["2"] = {"name": "second item"}
  db["3"] = {"name": "yet another item"}
  # Commit to save the objects.
  db.commit()
  # Oops, forgot to commit here, that object will never be saved.
  # Always remember to commit, or enable autocommit with SqliteDict("example.sqlite", autocommit=True)
  # Autocommit is off by default for performance.
  db["4"] = {"name": "yet another item"}
  # Close the connection
  db.close()


def read(source):
  db = SqliteDict(source)
  for key, item in db.items():
    print("%s=%s" % (key, item))


if __name__ == "__main__":
  source = "example.sqlite"
  write(source)
  read(source)