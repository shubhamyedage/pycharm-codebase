from os.path import join
from apps\
    .file_utils import FileUtils
import apps.constant as con
from fuzzywuzzy import fuzz, process

def test1():
    file_utils = FileUtils()
    files = file_utils.get_files(join('in', 'csv', con.INCOME_STATEMENTS))
    data_list = []
    for f in files:
        data = file_utils.read_csv(join('in', 'csv', con.INCOME_STATEMENTS), f)
        temp_data = data.transpose()
        list_keys = temp_data.columns

        # print(print(fuzz.ratio("Revenue", "Operating Revenue")))
        # v = process.extractOne("Revenue", ["Revenue", "Total Revenue", "Operating Revenue"])
        # print(v[0])
        # print(data.loc[v[0]][0])
# ######################################################################################################################
        print(fuzz.ratio("Operating Expenses", "Total operating expenses"))
        # v = process.extractOne("Operating Expenses", ["Operating Expenses", "Total operating expenses"])
        v = process.extractOne("Operating Expenses", list_keys)
        print(v[0])
        print(data.loc[v[0]])


def test2():
    list_k = ["Total stockholders' equity", "Total non-current assets", "kjgax"]
    i = process.extractOne("Total non-current assets", list_k)
    print(i)

def test3():
    list_i = ["Cash and cash eq", "Cash", "Cash Eq"]
    i = process.extractOne("Cash", list_i)
    print(i)

print("Hello!")
test2()