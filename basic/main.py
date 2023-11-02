from filefolder import FileFolder


if __name__ == "__main__":
    source = "filefolder.sqlite"
    size = 6

    print("---- PUT ----")
    with FileFolder(source=source, size=size) as ff:
        for i in range(3):
            name, content = "file_%d.txt" % i, "ab"
            print("insert %s" % name, ff.put(name, content))
            print("inserted items", ff.list())
            updated_content = "abc"
            print("update %s" % name, ff.put(name, updated_content))
            print("items", ff.list())

    print("---- GET ----")
    with FileFolder(source=source, size=size) as ff:
        for i in range(3):
            name = "file_%d.txt" % i
            print("get %s" % name, ff.get(name))

    print("---- REMOVE ----")
    with FileFolder(source=source, size=size) as ff:
        for i in range(3):
            name = "file_%d.txt" % i
            print("delete %s" % name, ff.remove(name))
            print("remaining items", ff.list())
