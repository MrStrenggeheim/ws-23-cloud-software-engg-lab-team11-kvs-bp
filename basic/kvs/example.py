from sqlitedict import SqliteDict
from contextlib import contextmanager

source = "example.sqlite"


@contextmanager
def openKVS():
    db = SqliteDict(source)
    yield db
    db.close()


def display():
    with openKVS() as db:
        print("-------- display starts ------")
        for key, item in db.items():
            print("%s=%s" % (key, item))
        print("-------- display ends --------\n")


def create_storage():
    with openKVS() as _:
        pass
    # Display a newly created storage
    display()


def add_items():
    with openKVS() as db:
        # Add few items
        db["1"] = {"name": "first item"}
        db["2"] = {"name": "second item"}
        db["3"] = {"name": "yet another item"}
        # Commit to save the objects.
        db.commit()
    # Now, display the current storage
    display()


def add_nocommit_item():
    with openKVS() as db:
        # Oops, forgot to commit here, that object will never be saved.
        # Always remember to commit, or enable autocommit with SqliteDict("example.sqlite", autocommit=True)
        # Autocommit is off by default for performance.
        db["4"] = {"name": "yet another item"}
    # Now, display the current storage
    display()


def update_item():
    with openKVS() as db:
        # Update an item in storage
        db["1"] = {"name": "updated first item"}
        db.commit()
    # how the storage looks like rn?
    display()


def delete_item():
    with openKVS() as db:
        # Delete an item
        del db["2"]
        db.commit()
    # item associated with key `2` should no longer be in the storage
    display()


def clear_storage():
    with openKVS() as db:
        # Clear the storage
        db.clear()
    # The storage should be empty now
    display()


if __name__ == "__main__":
    create_storage()
    add_items()
    add_nocommit_item()
    update_item()
    delete_item()
    clear_storage()
