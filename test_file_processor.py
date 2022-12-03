import unittest

import src.file_processor as module


class Testing(unittest.TestCase):
    def test_read_list(self):
        file, file_type = ('./src/data/lista-1.csv', 'lista')
        file_content = module.read(file, file_type)
        self.assertEqual(len(file_content), 4)

    def test_read_matrix(self):
        file, file_type = ('./src/data/matriz-1.csv', 'matriz')
        file_content = module.read(file, file_type)
        self.assertEqual(len(file_content), 4)

    def test_read_unknown(self):
        file, file_type = ('./src/data/matriz-1.csv', 'unknown')
        module.read(file, file_type)

    def test_read_file_list(self):
        file = './src/data/lista-1.csv'
        file_content = module.read_file_list(file)
        self.assertEqual(len(file_content), 4)

    def test_read_file_matrix(self):
        file = './src/data/matriz-1.csv'
        file_content = module.read_file_matrix(file)
        self.assertEqual(len(file_content), 4)


if __name__ == '__main__':
    unittest.main()
