import unittest
from datetime import datetime
import os
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from filefolder import FileFolder
import tempfile


class TestFileFolder2(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.source = os.path.join(self.test_dir, 'test_filefolder_2.sqlite')
        self.size = 10
        self.file_folder = FileFolder(source=self.source, size=self.size)

    def tearDown(self):
        # Close the FileFolder and remove the temporary directory
        self.file_folder.close()
        os.remove(self.source)
        os.rmdir(self.test_dir)

    def test_put_big_file(self):
        # Add a big file content
        file_name = 'overflow_file.txt'
        file_content = 'test test test test'
        self.assertFalse(self.file_folder.put(file_name, file_content))
        file = self.file_folder.get(file_name)
        self.assertIsNone(file)
        self.assertEqual(self.size, self.file_folder.get_free_space())

    def test_put_built_in_keyword_filename(self):
        # Add a file with name = buill-in keyword `size`
        file_name = 'size'
        file_content = 'fit now'
        self.assertFalse(self.file_folder.put(file_name, file_content))

    def test_fill_then_update(self):
        # Fill the folder free space
        file_name = 'fit_file_1.txt'
        file_content = 'fit 1'
        self.assertTrue(self.file_folder.put(file_name, file_content))
        self.assertEqual(5, self.file_folder.get_free_space())
        file_name = 'fit_file_2.txt'
        file_content = 'fit 2'
        self.assertTrue(self.file_folder.put(file_name, file_content))
        self.assertEqual(0, self.file_folder.get_free_space())
        # Update the bigger file content
        file_content = 'fit 2+'
        self.assertFalse(self.file_folder.put(file_name, file_content))
        # Update the smaller file content
        file_content = 'fit2'
        self.assertTrue(self.file_folder.put(file_name, file_content))
        self.assertEqual(1, self.file_folder.get_free_space())
        # Update the bigger content
        file_name = 'fit_file_1.txt'
        file_content = 'fit 1+'
        self.assertTrue(self.file_folder.put(file_name, file_content))

    def test_create_filefolder_from_existing_source(self):
        # Add new file to current folder
        file_name = 'file.txt'
        file_content = 'content'
        self.file_folder.put(file_name, file_content)
        # Clone a new folder from same datasource
        # Check the cloned folder having the same free space
        # Arg `size` should be ignored
        cloned_file_folder = FileFolder(source=self.source, size=1000)
        self.assertEqual(3, cloned_file_folder.get_free_space())
        # Delete file and check the cloned folder
        self.assertIsNotNone(self.file_folder.remove(file_name))
        cloned_file_folder = FileFolder(source=self.source, size=1000)
        self.assertEqual(10, cloned_file_folder.get_free_space())

    def test_file_last_modified_timestamp(self):
        # Add new file
        file_name = 'file.txt'
        file_content = 'test'
        before = datetime.now()
        self.assertTrue(self.file_folder.put(file_name, file_content))
        after = datetime.now()
        file = self.file_folder.get(file_name)
        self.assertIsNotNone(file)
        self.assertTrue(before <= file.last_modified <= after)
        # Update the file
        file_content = 'updated'
        before = datetime.now()
        self.assertTrue(self.file_folder.put(file_name, file_content))
        after = datetime.now()
        file = self.file_folder.get(file_name)
        self.assertTrue(before <= file.last_modified <= after)


if __name__ == '__main__':
    unittest.main()
