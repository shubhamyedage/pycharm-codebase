from treelib import Node
import apps.constant as con


class TreeNode(Node):
    def __init__(self, key_list, node_type, values = []):
        self.key_list = key_list
        self.values = values
        self.tag_flag = False
        self.node_type = node_type
        self.current_year_value = 0
        self.change_value = 0

    def _validate_values(self):
        return False if len(self.values) == 0 else True

    def get_change(self):
        size = len(self.values)
        if not self._validate_values():
            return 0
        else:
            value = self.values[size - 1] - self.values[size - 2]
            return (value * -1) if self.node_type is con.SUB else value

    def get_value(self, len_val):
        size = len(self.values)
        return 0 if not self._validate_values() else self.values[size - len_val]

    def to_string(self, identifier):
        print(identifier + "\t\t{}\t\t{}\t\t{}\t\t{}".format(self.get_value(2), self.get_value(1), self.get_change(),
                                                             self.current_year_value))
