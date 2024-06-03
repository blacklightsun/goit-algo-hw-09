def find_coins_greedy(change_sum : int) -> dict:
    sorted_coin_nominals_list = [50, 25, 10, 5, 2, 1]
    change_dict = {}

    for nominal in sorted_coin_nominals_list:
        temp = change_sum // nominal
        if temp != 0:
            change_dict[nominal] = temp
            change_sum = change_sum % nominal

    return change_dict

print(find_coins_greedy(113))
