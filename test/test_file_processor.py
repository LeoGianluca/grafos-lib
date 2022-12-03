import unittest

import src.file_processor as module

TEST_INPUT_LISTA = '../src/data/in/teste-lista-1.csv'
TEST_INPUT_MATRIZ = '../src/data/in/teste-matriz-1.csv'


class Testing(unittest.TestCase):
    def test_read_list(self):
        file, file_type = (TEST_INPUT_LISTA, 'lista')
        file_content = module.read(file, file_type)
        self.assertEqual(len(file_content), 4)

    def test_read_matrix(self):
        file, file_type = (TEST_INPUT_MATRIZ, 'matriz')
        file_content = module.read(file, file_type)
        self.assertEqual(len(file_content), 4)

    def test_read_unknown(self):
        file, file_type = (TEST_INPUT_MATRIZ, 'unknown')
        module.read(file, file_type)

    def test_read_file_list(self):
        file_content = module.read_file_list(TEST_INPUT_LISTA)
        self.assertEqual(len(file_content), 4)

    def test_read_file_matrix(self):
        file_content = module.read_file_matrix(TEST_INPUT_MATRIZ)
        self.assertEqual(len(file_content), 4)


if __name__ == '__main__':
    unittest.main()
