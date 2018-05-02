#############
laxl Overview
#############

This library is intended to help you deal with big Excel files from within
Python. After trying pandas_, openpyxl_, xlwings_, and even win32com_ it seems
that none have the ability to iterate over large Excel files without loading
them completely into memory. So when you are 

***************
Getting Started
***************

There are no dependancies to install. You just need to::

    pip install laxl

Once installed, you can iterate through the entire file without using much
memory by doing the following::

    from laxl import Workbook
    wb = Workbook("filepath")
    ws = wb.sheets['sheet name'] # or, for example, wb.sheets[1]
    for row in ws.rows:
        print(row)

If you are only interested in a few rows::

    head = ws.head(5)
    print(head)


*************
Running Tests
*************

To run tests::

    python -m tests.test_xl

*******
License
*******

The project is licensed under the MIT License - see the LICENSE.md_ file for details

.. _openpyxl: https://openpyxl.readthedocs.io/en/stable/
.. _xlwings: http://docs.xlwings.org/en/stable/quickstart.html
.. _win32com: http://docs.activestate.com/activepython/2.4/pywin32/html/com/win32com/HTML/docindex.html
.. _pandas: https://pandas.pydata.org/
.. _license.md: /LICENSE.md
