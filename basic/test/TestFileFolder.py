import unittest
from ..filefolder import FileFolder
from datetime import datetime
import os
import tempfile

class TestFileFolder(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.source = os.path.join(self.test_dir, 'test_filefolder.sqlite')
        self.size = 1000
        self.file_folder = FileFolder(source=self.source, size=self.size)

    def tearDown(self):
        # Close the FileFolder and remove the temporary directory
        self.file_folder.__exit__(None, None, None)
        os.remove(self.source)
        os.rmdir(self.test_dir)
    def test_put_and_get_file(self):
        # Test adding a new file
        file_name = 'test_file.txt'
        file_content = 'This is a test file.'
        self.assertTrue(self.file_folder.put(file_name, file_content))

        # Test retrieving the same file
        file = self.file_folder.get(file_name)
        self.assertIsNotNone(file)
        self.assertEqual(file.content, file_content)

    def test_put_file_exceeding_size(self):
        # Test adding a file that exceeds the folder's size
        file_name = 'large_file.txt'
        file_content = 'a' * (self.size + 1)
        self.assertFalse(self.file_folder.put(file_name, file_content))

    def test_update_file(self):
        # Test updating an existing file's content
        file_name = 'update_file.txt'
        initial_content = 'initial'
        updated_content = 'updated'
        self.assertTrue(self.file_folder.put(file_name, initial_content))
        self.assertTrue(self.file_folder.put(file_name, updated_content))

        # Check if the content was updated
        file = self.file_folder.get(file_name)
        self.assertEqual(file.content, updated_content)

    def test_remove_file(self):
        # Test removing a file
        file_name = 'remove_file.txt'
        file_content = 'content'
        self.file_folder.put(file_name, file_content)

        # Remove the file and try to get it
        removed_file = self.file_folder.remove(file_name)
        self.assertIsNotNone(removed_file)
        self.assertIsNone(self.file_folder.get(file_name))

    def test_list_files(self):
        # Test listing files in the folder
        file_names = ['file1.txt', 'file2.txt']
        for name in file_names:
            self.file_folder.put(name, 'content')

        listed_files = self.file_folder.list()
        self.assertEqual(len(listed_files), len(file_names))
        for name, _ in listed_files:
            self.assertIn(name, file_names)
    def test_size_update_on_put_and_remove(self):
        # Check initial size
        initial_size = self.file_folder._FileFolder__size  # Accessing the private variable for testing
        self.assertEqual(initial_size, self.size)

        # Add a new file and check size decrement
        file_name = 'test_size_file.txt'
        file_content = 'Size test'
        self.assertTrue(self.file_folder.put(file_name, file_content))
        self.assertEqual(self.file_folder._FileFolder__size, initial_size - len(file_content))

        # Remove the file and check size increment
        self.file_folder.remove(file_name)
        self.assertEqual(self.file_folder._FileFolder__size, initial_size)
if __name__ == '__main__':
    unittest.main()
