import json


class ReadTextFile():
    def __init__(self):
        self.j = self._text_to_json()

    def _text_to_json(self):
        f = open("Company_Node.txt")
        j = json.loads(f.read())
        print(type(j))
        return j

    def process_json(self):
        print(type(self.j))
        print(self.j.get("company_name"))
        self.j["company_name"] = "h"
        print(self.j.get("company_name"))
        annual_table = self.j.get("annual_table")
        self._attach_data(annual_table)
        print(self.j)

    def _attach_data(self, annual_table):
        annual_table["index"] = [1, 2, 3, 400000000000000000000000000000000]
        annual_table["absolute_values"] = [1, 2, 3, 4, 5, 6]
        annual_table["percentage_values"] = [9, 8, 7, 6, 5, 4, 3]


ReadTextFile()
