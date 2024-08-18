def triangular_numbers_sequence(n):
    # n : sentence number in sequence
    return (n*(n+1))//2

def square_sequence(n):
    return n**2

def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

def Arithmetic_sequence(n,first_num_sequence, distance):
    return first_num_sequence + (n-1) * distance

def geometric_progression(n, first_num_progression, ratio_value):
    # ratio_value : the value that is equal to = each sentence//previous sentence
    return first_num_progression * ratio_value ** (n-1)

def multiple_nums_geometric_progression(first_num_progression, an, n):
    # an : the value of the sequence sentence in number n : must be integer
    return (first_num_progression * an)**(n/2)


# def scientific_symbol_returner(n):
#     x = 0
#     for i in str(n):
#         print(i, end=" ")
#         if i == "0":
#             x += 1
#     print(x)
#     # print(n, "n")
#     # str_n = str(n).replace("0","")
#     # str_n = str_n.replace(".", "")
#     # print(str_n)
#     # if len(str(n)) > 1:
#     #     number = str(int(n))[0]+"."+str(int(n)[1:])
#     #     print(number)
#     # else:
#     #     print(len(str(int(n))))
#
# scientific_symbol_returner(0.000000000173)
