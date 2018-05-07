"""
test_sxl.py - test sxl library
"""

import datetime
import os
import unittest

from .context import sxl


def here():
    "Return filepath to this file"
    return os.path.dirname(__file__)


class TestNoNumberFormats(unittest.TestCase):

    def setUp(self):
        filepath = os.path.join(here(), 'Book2.xlsx')
        self.wb = sxl.Workbook(filepath)
        self.data = list(self.wb.sheets[1].cat())

    def test_leading_zeros(self):
        self.assertEqual(self.data[3][0], "002")

    def test_none(self):
        self.assertIsNone(self.data[3][2])

    def test_all_rows(self):
        row_iter = iter(self.wb.sheets[1].rows)
        last_row = ''
        for row in row_iter:
            last_row = row[0]
        self.asertEqual(last_row, '240')


class TestExcelCat(unittest.TestCase):

    def setUp(self):
        filepath = os.path.join(here(), 'Book1.xlsx')
        self.wb = sxl.Workbook(filepath)
        self.data = list(self.wb.sheets[1].cat())

    def test_first_row_first_col(self):
        self.assertEqual(self.data[0][0], 1)

    def test_first_row_last_col(self):
        self.assertEqual(self.data[0][17], 18)

    def test_date(self):
        self.assertEqual(self.data[5][5], datetime.datetime(2018, 1, 31))

    def test_date_diff_format(self):
        self.assertEqual(self.data[5][9], datetime.datetime(2018, 2, 28))

    def test_row_len(self):
        self.assertEqual(len(self.data[0]), 18)

    def test_col_len(self):
        self.assertEqual(len(self.data), 46)

    def test_old_date(self):
        self.assertEqual(self.data[20][17], datetime.datetime(1900, 1, 1))

    def test_center_across_selection(self):
        self.assertEqual(self.data[26][4], 473)
        self.assertEqual(self.data[26][5], None)

    def test_string(self):
        self.assertEqual(self.data[9][7], 'Test')

    def test_merged_cells(self):
        self.assertEqual(self.data[15][7], 'Merged')
        self.assertEqual(self.data[15][8], None)

    def test_formatted_substring(self):
        self.assertEqual(self.data[22][6], 'Different styles in one cell')

    def test_string_with_line_break(self):
        self.assertEqual(self.data[31][5], 'Test with \nline breaks')


class TestExcelHead(unittest.TestCase):

    def setUp(self):
        here = os.path.dirname(__file__)
        self.filepath = os.path.join(here, 'Book1.xlsx')
        self.data = sxl.Workbook(self.filepath).sheets[1].head()

    def test_head_default_len(self):
        self.assertEqual(len(self.data), 10)

    def test_simple_value(self):
        self.assertEqual(self.data[0][5], 6)

    def test_date_by_formula(self):
        self.assertEqual(self.data[6][9], datetime.datetime(2018, 3, 1))

    def test_small_head(self):
        data = sxl.Workbook(self.filepath).sheets[1].head(3)
        self.assertEqual(len(data), 3)

    def test_big_head(self):
        data = sxl.Workbook(self.filepath).sheets[1].head(1000)
        self.assertEqual(len(data), 46)


if __name__ == '__main__':
    unittest.main()
