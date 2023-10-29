from sqlitedict import SqliteDict


class FileFolder:
  def __init__(self, source="filefolder.sqlite", cap=10) -> None:
    self.__db = SqliteDict(source)
    self.__cap = cap
  
  def __enter__(self):
    return self
  
  def __exit__(self, type, value, traceback) -> None:
    self.close()
  
  def put(self, mark: str, content: str) -> bool:
    if mark not in self.__db and len(self.__db) == self.__cap:
      return False
    self.__db[mark] = content
    self.__db.commit()
    return True

  def get(self, mark: str) -> str | None:
    if mark in self.__db:
      return self.__db[mark]
    else:
      return None
  
  def remove(self, mark: str) -> str | None:
    if mark in self.__db:
      content = self.__db[mark]
      del self.__db[mark]
      self.__db.commit()
      return content
    else:
      return None
  
  def items(self) -> list[tuple[str, str]]:
    return [(mark, content) for mark, content in self.__db.items()]

  def close(self) -> None:
    self.__db.close()


