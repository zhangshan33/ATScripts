# -*- coding: utf-8 -*-
# __author__ = "maple"


'''
pip install xlrd
pip install xlwt
'''
import xlrd

# file_path = r'D:\MT\ATScripts\demo\接口测试示例.xlsx'
#
# # 获取到book对象
# book = xlrd.open_workbook(file_path)
# # print(book)
# # 获取sheet对象
# sheet = book.sheet_by_index(0)
# # sheet = book.sheet_by_name('接口自动化用例')
# # sheets = book.sheets()  # 获取所有的sheet对象
#
# rows, cols = sheet.nrows, sheet.ncols
# print(rows, cols)

# 获取所有行
# for row in range(rows):
#     print(sheet.row_values(row))
#     break

# 获取所有列
# for col in range(cols):
#     print(sheet.col_values(col))

# 获取，第3行
# print(sheet.row_values(2))

# 获取指定列
# print(sheet.col_values(0))

# 获取指定的单元格内容
# print(sheet.cell(0, 0))

# 将首行与其他行组成字典 [{} {}]

# # 大wei的思路
# l = []
# # 阿虎的思路，先取一行
# # print(sheet.row_values(0))
# title = sheet.row_values(0)
# print(title)
# # 获取其他行
# for i in range(1, rows):
#     # print(sheet.row_values(i))
#     l.append(dict(zip(title, sheet.row_values(i))))
#
# print(l)


import pytest

def get_excel_data():
    file_path = r'接口测试示例.xlsx'

    # 获取到book对象
    book = xlrd.open_workbook(file_path)
    # print(book)
    # 获取sheet对象
    sheet = book.sheet_by_index(0)
    # sheet = book.sheet_by_name('接口自动化用例')
    # sheets = book.sheets()  # 获取所有的sheet对象

    rows, cols = sheet.nrows, sheet.ncols
    l = []
    # print(sheet.row_values(0))
    title = sheet.row_values(0)
    # print(title)
    # 获取其他行
    for i in range(1, rows):
        # print(sheet.row_values(i))
        l.append(dict(zip(title, sheet.row_values(i))))

    return l

# @pytest.mark.parametrize('case', get_excel_data())
# def test_case(case):
#     print(case)

# if __name__ == '__main__':
    # pytest.main(['-s' ,'test_demo1.py'])
import json
# res = get_excel_data()['case_expect']
# print(res, type(res))
# print(json.loads(res))
# for value in get_excel_data():
#     print(value['case_expect'], json.loads(value['case_expect']))

import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.cnblogs.com/Neeo/articles/11667962.html')
s = BeautifulSoup(r.text, 'html.parser')
print(s.find('title').text)





