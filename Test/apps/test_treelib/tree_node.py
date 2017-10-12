from treelib import Node


class TreeNode(Node):
    # Initialize attributes.
    def __init__(self, key_list=None, node_type=None, tag_flag=False):
        self.key_list = key_list
        self.values = []
        self.tag_flag = tag_flag
        self.node_type = node_type
        self.current_year_value = 0
        self.change_value = 0
        self.per_change = 0
        self.slope = 0
        self.constant = 0
        self.average_change = 0
        self.average_per_change = 0
        # self.long_term_trend_indicator = con.GROWING_SLOWLY
        # self.short_term_trend_indicator = con.INCREASE
        self.quarterly_values = []
        self.annual_values = []
        self.annual_per_holdings = []
        self.quarterly_per_holdings = []

    # # Validate values list.
    # def _validate_values(self):
    #     return False if len(self.values) == 0 else True
    #
    # # Gives values with formatting i.e. replacing special character with 0 or empty.
    # def get_values(self, index):
    #     if not self._validate_values() or index > len(self.values):
    #         return []
    #     else:
    #         self.values = self.values[0] if len(self.values) == 1 else self.values[index]
    #         return self.values
    #
    # # This function is supposed to use by node analysis.
    # def get_change_value(self, index1=None, index2=None):
    #     if index1 is None:
    #         index1 = 1
    #     if index2 is None:
    #         index2 = 2
    #     if not self._validate_values():
    #         return 0
    #     else:
    #         value = round(self.get_value(index1) - self.get_value(index2), 2)
    #         self.change_value = (value * -1) if self.node_type is con.SUB else value
    #         return self.change_value
    #
    # # This give percentage change between two values.
    # def get_per_change(self, index1=None, index2=None):
    #     v = self.get_value(2) if index2 is None else self.get_value(index2)
    #     v1 = self.get_value(1 if index1 is None else index1)
    #     self.per_change = v1 if v == 0 else round(self.get_change_value(index1, index2) * 100 / v, 2)
    #     return self.per_change
    #
    # # Return slope.
    # def get_slope(self, index=None, is_root=False):
    #     if not self._validate_values():
    #         return 0
    #     else:
    #         if index is None:
    #             index = len(self.values) - 1
    #         else:
    #             index += len(self.values) - index
    #         values = self.values[:index]
    #         if is_root:
    #             values = [(a - b) * 100 / b for a, b in zip(values[1:], values[:-1])]
    #         self.slope, self.constant = MathUtils().get_linear_function_properties(values)
    #         return self.slope
    #
    # # Give particular value from list.
    # def get_value(self, len_val):
    #     size = len(self.values)
    #     return 0 if not self._validate_values() else self.values[size - len_val]
    #
    # # Gives average change over time period.
    # def get_average_change(self):
    #     self.average_change = 0 if not self._validate_values() else MathUtils().average_change(self.values)
    #     return self.average_change
    #
    # # Give average percentage change rate.
    # def get_avg_per_change(self):
    #     if not self._validate_values():
    #         self.average_per_change = 0
    #     else:
    #         l_val = len(self.values)
    #         v1 = self.get_value(l_val)
    #         v2 = self.get_value(1)
    #         self.average_per_change = MathUtils().percentage_change(v1, v2)
    #     return round(self.average_per_change / l_val, 2)
    #
    # # Return node dict with data.
    # def get_node_dict(self, nid):
    #     l = len(self.values)
    #     if l is 0:
    #         return
    #     v = self.per_holdings[l - 1] - self.per_holdings[l - 2]
    #     v1 = self.get_value(1)
    #     return {con.KEY: nid, con.YEAR_1: self.get_value(2), con.YEAR_2: v1,
    #             con.CALCULATED_YEAR_2: self.current_year_value,
    #             con.CHANGE: (v1 - self.current_year_value), con.YEAR_1_HOLDINGS: self.per_holdings[l - 1],
    #             con.YEAR_2_HOLDINGS: self.per_holdings[l - 2], con.COMPARISION: 0 if v < 5 else v}
    #
    # # Get long term trend.
    # def get_long_term_trend_indicator(self):
    #     self.get_slope()
    #     if self.slope > 2:
    #         self.long_term_trend_indicator = con.GROWTH
    #     if self.slope < -2:
    #         self.long_term_trend_indicator = con.DECLINE
    #     return self.long_term_trend_indicator
    #
    # # Get short term trend
    # def get_short_term_trend(self):
    #     indicator_2 = con.EXPANDED
    #     self.get_change_value()
    #     if self.change_value < 0:
    #         self.short_term_trend_indicator = con.DECREASED
    #         indicator_2 = con.NARROWED
    #     return self.short_term_trend_indicator, indicator_2
    #
    # # Set values either annual or quarterly.
    # def set_abs_values(self, use_annual=False):
    #     self.values = self.annual_values if use_annual else self.quarterly_values
    #
    # # Set per_holdings either annual or quarterly.
    # def set_per_values(self, use_annual=False):
    #     self.values = self.annual_per_holdings if use_annual else self.quarterly_per_holdings
