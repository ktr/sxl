
# Overview

This library is intended to help you deal with big Excel files from within
Python. After trying pandas_, openpyxl_, xlwings_, and even win32com_ it seems
that none have the ability to iterate over large Excel files without loading
them completely into memory. When all you want to do is look at the first few
rows or when the files are massive, loading the entire thing into memory before
doing anything can be overkill.

Getting Started

Tests

Installation


To run tests:

    python -m tests.test_xl

.. _openpyxl: https://openpyxl.readthedocs.io/en/stable/
.. _xlwings: http://docs.xlwings.org/en/stable/quickstart.html
.. _win32com: http://docs.activestate.com/activepython/2.4/pywin32/html/com/win32com/HTML/docindex.html
.. _pandas: https://pandas.pydata.org/
