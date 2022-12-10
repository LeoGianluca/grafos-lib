import unittest

from src.file_processor import FileProcessor

TEST_INPUT_LISTA = './data/in/teste-lista-1.csv'
TEST_INPUT_MATRIZ = './data/in/teste-matriz-1.csv'


class Testing(unittest.TestCase):
    FILE_INPUT_SIZE_LISTA = 4
    FILE_INPUT_SIZE_MATRIZ = 5

    file_processor = FileProcessor()

    def test_read_list(self):
        file, file_type = (TEST_INPUT_LISTA, 'lista')
        file_content = self.file_processor.read(file, file_type)
        self.assertEqual(self.FILE_INPUT_SIZE_LISTA, len(file_content))

    def test_read_matrix(self):
        file, file_type = (TEST_INPUT_MATRIZ, 'matriz')
        file_content = self.file_processor.read(file, file_type)
        self.assertEqual(self.FILE_INPUT_SIZE_MATRIZ, len(file_content))

    def test_read_unknown(self):
        file, file_type = (TEST_INPUT_MATRIZ, 'unknown')
        self.file_processor.read(file, file_type)

    def test_read_file_list(self):
        file_content = self.file_processor.read_file_list(TEST_INPUT_LISTA)
        self.assertEqual(self.FILE_INPUT_SIZE_LISTA, len(file_content))

    def test_read_file_matrix(self):
        file_content = self.file_processor.read_file_matrix(TEST_INPUT_MATRIZ)
        self.assertEqual(self.FILE_INPUT_SIZE_MATRIZ, len(file_content))

    def test_write_file_graph_as_matrix(self):
        file_path = './data/out/teste-matriz-out.csv'
        file_content = [['A', 'B', 12], ['A', 'C', 4], ['A', 'D', 1], ['A', 'E', 5], ['C', 'E', 2]]

        self.file_processor.write_file_graph_as_matrix(file_path, file_content)
        file_content_readed = self.file_processor.read_file_matrix(file_path)

        self.assertEqual(file_content, file_content_readed)


if __name__ == '__main__':
    unittest.main()
