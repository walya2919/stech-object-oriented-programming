def three_average(a : int, b : int, c : int):
    return (a + b + c) / 3

def top_three_average(a : int, b : int, c : int, d : int):
    return (a + b + c + d - min(a,b,c,d)) / 3