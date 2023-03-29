import os
os.system("clear")

# def main(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)
# print(main(name = 'olzhas', age = '20', i = 123, a = 123.123, b = [1, 2, 3]))

# a = 10
# for i in a:
#     print(i)

# def rec_num(number: int):
#     if number == 0:
#         return 1
#     return number * rec_num(number - 1)

# 10 * 9 i td
# print(rec_num(5))
# num = int(input("Введите число: "))
# factorial = rec_num(num)
# print(f"Факториал числа {num} равен = {factorial}")

def max_find_num(lists: list):
    n = len(lists)
    if n == 0:
        return "тест"
    
    if n == 1:
        return lists[0]
    
    return max(lists[n - 1], max_find_num(lists, n -1))

arr = [1, 2, 3]
n = len(arr)
print(max_find_num(arr, n))
    




















































































