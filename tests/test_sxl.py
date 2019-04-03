"""
test_sxl.py - test sxl library
"""

import datetime
import os
import unittest

from .context import sxl # type: ignore


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
        self.assertEqual(last_row, '240')


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


class TestWorksheets(unittest.TestCase):

    def setUp(self):
        here = os.path.dirname(__file__)
        self.filepath = os.path.join(here, 'Book1.xlsx')
        self.wb = sxl.Workbook(self.filepath)

    def test_row_dimensions_on_empty_sheet(self):
        ws = self.wb.sheets[2]
        self.assertEqual(ws.num_rows, 0)

    def test_col_dimensions_on_empty_sheet(self):
        ws = self.wb.sheets[2]
        self.assertEqual(ws.num_cols, 0)

    def test_row_dimensions_on_sheet_w_one_value(self):
        ws = self.wb.sheets[3]
        self.assertEqual(ws.num_rows, 1)

    def test_col_dimensions_on_sheet_w_one_value(self):
        ws = self.wb.sheets[3]
        self.assertEqual(ws.num_cols, 1)

    def test_get_range_start_w_b(self):
        ws = self.wb.sheets[1]
        data = ws.range('B2:R2')[0]
        exp = list(range(20, 37))
        self.assertEqual(exp, data)

    def test_get_range_start_w_a(self):
        ws = self.wb.sheets[1]
        data = ws.range('A2:R2')[0]
        exp = list(range(19, 37))
        self.assertEqual(exp, data)

    def test_get_range_start_w_a_2rows(self):
        ws = self.wb.sheets[1]
        data = ws.range('A2:R3')
        exp = [list(range(19, 37)), list(range(37, 55)),]
        self.assertEqual(exp, data)

    def test_range_num_rows(self):
        ws = self.wb.sheets[1]
        data = ws.range('A2:R3')
        self.assertEqual(2, len(data))

    def test_time_pm(self):
        expected = datetime.time(hour=18, minute=30)
        ws = self.wb.sheets['Time']
        cell = ws.range('A1')
        self.assertEqual(expected, cell)

    def test_time_am(self):
        expected = datetime.time(hour=6, minute=30)
        ws = self.wb.sheets['Time']
        cell = ws.range('A3')
        self.assertEqual(expected, cell)

    def test_time_military(self):
        expected = datetime.time(hour=14, minute=30)
        ws = self.wb.sheets['Time']
        cell = ws.range('A5')
        self.assertEqual(expected, cell)


if __name__ == '__main__':
    unittest.main()
