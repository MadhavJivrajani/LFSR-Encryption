feedback_poly = {
    2: [1],
    3: [2],
    4: [3],
    5: [3],
    6: [5],
    7: [6],
    8: [6, 5, 4],
    9: [5],
    10: [7],
    11: [9],
    12: [11, 10, 4],
    13: [12, 11, 8],
    14: [13, 12, 2],
    15: [14],
    16: [14, 13, 11],
    17: [14],
    18: [11],
    19: [18, 17, 14],
    20: [17],
    21: [19],
    22: [21],
    23: [18],
    24: [23, 22, 17]
}

"""
def one_hot_encode(n):
    coeffs = []
    coeffs.append(1)
    for i in range(1, n):
        if i in feedback_poly[n]:
            coeffs.append(1)
        else:
            coeffs.append(0)
    return coeffs
"""
def one_hot_encode(n):
    coeffs = []
    coeffs.append(-1)
    for i in range(1, n):
        if i in feedback_poly[n]:
            coeffs.append(-1)
        else:
            coeffs.append(0)
    return coeffs
