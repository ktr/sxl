============
sxl Overview
============

This library is intended to help you deal with big Excel files from within
Python. After trying pandas_, openpyxl_, xlwings_, and even win32com_ it seems
that none have the ability to iterate over large Excel files without loading
them completely into memory. So when you are dealing with files that are
extremely large, this can be burdensome (especially if you only want to examine
a bit of the file - the first 10 rows say). This library solves that by parsing
the SpreadsheetML / XML xlsx files using a streaming parser. So you can see the
first ten rows of any tab within any Excel file extremely quickly.

Getting Started
===============

There are no dependancies to install. You just need to::

    pip install sxl

Once installed, you can iterate through the entire file without using much
memory by doing the following::

    from sxl import Workbook
    wb = Workbook("filepath")
    ws = wb.sheets['sheet name'] # or, for example, wb.sheets[1]
    for row in ws.rows:
        print(row)

Note that by default we assume the workbook is encoded with UTF-8. If you need
to specifiy a different encoding, you can do so when opening the workbook::

    wb = Workbook("filepath", encoding='cp1252')

If you are only interested in a few rows::

    head = ws.head(5)
    print(head)


Running Tests
=============

To run tests::

    python -m tests.test_sxl

License
=======

The project is licensed under the MIT License - see the LICENSE.md_ file for
details

.. _openpyxl: https://openpyxl.readthedocs.io/en/stable/
.. _xlwings: http://docs.xlwings.org/en/stable/quickstart.html
.. _win32com: http://docs.activestate.com/activepython/2.4/pywin32/html/com/win32com/HTML/docindex.html
.. _pandas: https://pandas.pydata.org/
.. _license.md: /LICENSE.txt
.. _lax: http://www.dictionary.com/browse/lax?s=t
