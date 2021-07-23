import os
import unittest
import csv
import csv_utils, test_utils

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "data.csv")



class TestCSVUtils(unittest.TestCase):
    def test_get_column_names(self):
        actual_result_A = csv_utils.CSVUtils(csv_A_path).get_column_names()
        expected_result_B = test_utils.parse_csv_file(column_names_B_path)[0]
        self.assertListEqual(actual_result_B, expected_result_B)  
        self.assertListEqual(actual_result_A, expected_result_A)

   

if __name__ == '__main__':
    unittest.main()