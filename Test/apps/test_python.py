# y1 = 11
# y2 = -18
# y3 = -10
#
# indicators = {
#             (0 < y1 and 0 < y3 and 0 < y2): ["MIXED_GROWTH", ''],
#             (0 < y1 and y3 < 0 < y2): ["MIXED_GROWTH", ''],
#             (y2 < 0 < y1 and 0 < y3): ["MIXED_GROWTH", ''],
#             (5 > y1 and 5 > y2 and 7 < y3): [
#                 "FLAT_FOLLOWED_BY_GROWTH_THIS_YEAR", ''
#             ],
#             (5 > y1 and 5 > y2 and 5 > y3): ["GROWTH", "FLAT"],
#             (5 > y1 and 5 > y2 and 0 > y3): [
#                 "FLAT_FOLLOWED_BY_DECLINE_THIS_YEAR", ''
#             ],
#             (5 < y1 and 5 < y2 and 5 < y3): ["GROWTH", "STEADY"],
#             (10 < y1 and 10 < y2 and 10 < y3): [
#                 "GROWTH", "OUBLE_DIGIT"
#             ],
#             (y1 > y2 > y3): ["DECLINE", "ACCELERATING"],
#             (y1 < y2 < y3): ["GROWTH", "ACCELERATING"],
#             (0 > y1 and 0 > y2 and 0 > y2): ["DECLINE", "STEADY"],
#             (-5 > y1 and -5 > y2 and -5 > y3): ["DECLINE", "FLAT"],
#         # }[True]
#         }.get(True, ['', ''])
# print(indicators)
# print((0 > y1 and 0 > y2 and 0 > y2))
# value = 0.79
# e = [
#         0,
#         0.6
#       ]
# g =  [
#         0.6,
#         1.25
#       ]
# p = [
#         1.25,
#         1.8
#       ]
# c = [
#         1.8,
#         0
#       ]
# state = {
#     e[0] < value < e[1]: "EXCELLENT",
#     g[0] < value < g[1]: "con.GOOD",
#     p[0] < value < p[1]: "con.POOR",
#     c[0] < value < c[1]: "con.CRITICAL"
# }.get(True)
# print(state)
# print(
#     g[0] < value < g[1]
# )


# final_fps = 5.8
# i = {
#             2.0 <= final_fps < 1.6: ["AAA", "Excellent", 1, 4],
#             1.6 <= final_fps < 1.2: ["AA", "Very good", 2, 5],
#             1.2 <= final_fps < 0.8: ['A', "Good", 3, 6],
#             0.8 <= final_fps < 0.4: ["BBB", "Positive", 4, 7],
#             0.4 <= final_fps < 0: ["BB", "Normal", 5, 8],
#             0 <= final_fps < -0.4: ['B', "Satisfactory", 6, 9],
#             -0.4 <= final_fps < -0.8: ["CCC", "Unsatisfactory", 7, 10],
#             -0.8 <= final_fps < -1.2: ["CC", "Adverse", 8, 11],
#             -1.2 <= final_fps < -1.6: ["C", "Bad", 9, 12],
#             -1.6 <= final_fps < -2: ["D", "Critical", 10, 13]
#         }.get(True)
# print(i)
#
# from treelib.tree import Tree
# t = Tree()
# t.create_node('a', 'a')
# t.create_node('b', 'b', parent='a')
# print(t.get_node('c'))
# if t.su('b'):
#     print("yes")
# i = [1,2,3,4]
# s = "fkm"
# print(s + str(i))

# import pandas as pd
#
# df = pd.DataFrame()
# if df.isnull:
#     print("yes")
p = None
i = float(p)