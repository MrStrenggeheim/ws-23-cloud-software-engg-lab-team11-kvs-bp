from filefolder import FileFolder


if __name__ == "__main__":
  source = "filefolder.sqlite"
  cap = 4

  print("---- PUT ----")
  with FileFolder(source=source, cap=cap) as ff:
    for i in range(cap + 1):
      mark, content = "mark %d" % i, "content %d" % i
      print("insert %s" % mark, ff.put(mark, content))
      print("inserted items", ff.items())
      updated_content = "%s - updated" % content
      print("update %s" % mark, ff.put(mark, updated_content))
      print("items", ff.items())
  
  print("---- GET ----")
  with FileFolder(source=source, cap=cap) as ff:
    for i in range(cap + 1):
      mark = "mark %d" % i
      print("get %s" % mark, ff.get(mark))
  
  print("---- REMOVE ----")
  with FileFolder(source=source, cap=cap) as ff:
    for i in range(cap + 1):
      mark = "mark %d" % i
      print("delete %s" % mark, ff.remove(mark))
      print("remaining items", ff.items())