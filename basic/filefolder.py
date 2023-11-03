from sqlitedict import SqliteDict
from datetime import datetime


class File:
    def __init__(self, content: str, last_modified: datetime) -> None:
        self.content = content
        self.last_modified = last_modified

    def __str__(self) -> str:
        return "[%s]: %s" % (self.last_modified.strftime("%d/%m/%Y, %H:%M:%S"), self.content)


class FileFolder:
    def __init__(self, source="filefolder.sqlite", size=10) -> None:
        """
        Initialize a file folder with limited space
        """
        self.__folder = SqliteDict(source)
        self.__size = size

    def __enter__(self):
        """
        Access the file folder. Override method `__enter__` for context manager
        """
        return self

    def __exit__(self, type, value, traceback) -> None:
        """
        Leave the file folder. Override method `__exit__` for context manager
        """
        self.__folder.close()

    def put(self, name: str, content: str) -> bool:
        """
        Put the file into the folder.

        If file name does not exist in the folder, add a new file with given name and content.
        In case file name already exists, update the exisiting file.

        :param str name: The file name
        :param str content: The file content
        :return: The status of `put` operation. Return `True` if file is added/updated; otherwise, `False` 
        :rtype: bool

        Note that `File.size`, `File.last_modified` and `FileFolder.size` should be considered
        """
        if name not in self.__folder and len(content) > self.__size:
            # print(f" {len(content), self.__size=} --> OVER THE CAPACITY!!")
            return False
        elif name in self.__folder:
            file = self.__folder[name]
            if len(content) - len(file.content) > self.__size:
                # print(f" {len(content), len(file.content)=} --> OVER THE CAPACITY!")
                return False
            self.__size -= len(content) - len(file.content)
            file.content = content
            file.last_modified = datetime.now()
            self.__folder[name] = file
        else:
            self.__size -= len(content)
            self.__folder[name] = File(
                content=content,
                last_modified=datetime.now()
            )
        self.__folder.commit()
        return True

    def get(self, name: str) -> File | None:
        """
        Get the file with specified name in the folder

        :param str name: The file name
        :return: The file with given name in the folder. Return `None` if there is no file with the specified name
        :rtype: File or None
        """
        if name in self.__folder:
            return self.__folder[name]
        else:
            return None

    def remove(self, name: str) -> File | None:
        """
        Remove the file with specified name from the folder

        :param str name: The file name
        :return: The removed file with given name. Return `None` if there is no file with the specified name
        :rtype: File or None

        Note that `FileFolder.size` should be considered
        """
        if name in self.__folder:
            file = self.__folder[name]
            del self.__folder[name]
            self.__size += len(file.content)
            self.__folder.commit()
            return file
        else:
            return None

    def list(self) -> list[tuple[str, File]]:
        """
        List all the files in the folder

        :return: List of files in the folder
        :rtype: tuple of str and File
        """
        return [(name, file) for name, file in self.__folder.items()]
