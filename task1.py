import timeit

s = '''
def find_coins_greedy(change_sum : int) -> dict:
    sorted_coin_nominals_list = [50, 25, 10, 5, 2, 1]
    change_dict = {}

    for nominal in sorted_coin_nominals_list:
        temp = change_sum // nominal
        if temp != 0:
            change_dict[nominal] = temp
            change_sum = change_sum % nominal

    return change_dict

print('Сума для розрахунку решти: ', change_sum)
print('Результат роботи жадібного алгоритму:', find_coins_greedy(change_sum))
'''

change_sum = 2578

f_time = timeit.timeit('find_coins_greedy' + "(change_sum)", setup=s, number=1, globals=globals())

print(f'Час роботи жадібного алгоритму: {f_time} сек.')