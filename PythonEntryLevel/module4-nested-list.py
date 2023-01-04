nums = [0, 'One', 3, 'Three', 4, 'Five']
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
# print(nums)
# print(table)
# print(table[0])
# print(table[1])
# print(table[1][1])
# print('---')
#
# for row in table:
#     print('outer loop / row:', row)
#     for cell in row:
#         print('inner loop / cell value:', cell)

# for row in table:
#     print()
#     for cell in row:
#         print(cell, end=' ')

# 1, 2, 3, 4
# 1, 2, 3, 4
# 1, 2, 3, 4
# 1, 2, 3, 4


table = [[i for i in range(1, 5)] for j in range(4)]
for row in table:
    print()
    for cell in row:
        print(cell, end=' ')