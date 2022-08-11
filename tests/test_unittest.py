import unittest
from unittest.mock import patch
from parameterized import parameterized
from app import add_new_doc, delete_doc, get_doc_shelf, get_doc_owner_name, documents, directories


FIXTURE_ADD_DOC = [
    ('test_number_1', 'test_type_1', 'test_name_1', 'test_shelf_number_1'),
    ('test_number_2', 'test_type_2', 'test_name_2', '1')
]

FIXTURE_SHELF_NUM_DOC = [
    ('2207 876234', '1'),
    ('10006', '2'),
    ('notexistnumber', '1')
]

FIXTURE_OWNER_NAME_DOC = [
    ('2207 876234', 'Василий Гупкин'),
    ('10006', 'Аристарх Павлов'),
    ('notexistnumber', 'noowner')
]

FIXTURE_DEL_DOC = [
    'test_number_1',
    'test_number_2',
    'notexistnumber'
]


class TestApp(unittest.TestCase):
    
    @parameterized.expand(FIXTURE_ADD_DOC)
    def test_add_doc(self, doc_number, doc_type, owner_name, shelf_number):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [doc_number, doc_type, owner_name, shelf_number]
            result = add_new_doc()
        test_document = {"type": doc_type, "number": doc_number, "name": owner_name}
        self.assertEqual(result, shelf_number)
        self.assertIn(test_document, documents)
        self.assertIn(doc_number, directories[shelf_number])

    @parameterized.expand(FIXTURE_SHELF_NUM_DOC)
    def test_get_doc_shelf(self, doc_number, shelf_number):
        with patch('builtins.input') as mock_input:
            mock_input.return_value = doc_number
            if doc_number == 'notexistnumber':
                result = get_doc_shelf()
                self.assertEqual(result, None)
            else:
                result = get_doc_shelf()
                self.assertEqual(result, shelf_number)

    @parameterized.expand(FIXTURE_OWNER_NAME_DOC)
    def test_get_doc_owner_name(self, doc_number, owner_name):
        with patch('builtins.input') as mock_input:
            mock_input.return_value = doc_number
            if doc_number == 'notexistnumber':
                result = get_doc_owner_name()
                self.assertEqual(result, None)
            else:
                result = get_doc_owner_name()
                self.assertEqual(result, owner_name)

    @parameterized.expand(FIXTURE_DEL_DOC)
    def test_delete_doc(self, doc_number):
        with patch('builtins.input') as mock_input:
            mock_input.return_value = doc_number
            if doc_number == 'notexistnumber':
                result = delete_doc()
                self.assertEqual(result, None)
            else:
                result, status = delete_doc()
                self.assertEqual(result, doc_number)
                self.assertEqual(status, True)
