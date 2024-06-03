def find_coins_dynamic(change_sum: int) -> dict:
    sorted_coin_nominals_list = [1, 2, 5, 10, 25, 50]

    # створюємо таблицю k для зберігання оптимальних значень підзадач - (кожна комірка містить список монет, на старті цей спиcок пустий)
    k = [[[] for _ in range(change_sum + 1)] for _ in range(len(sorted_coin_nominals_list) + 1)]

    # будуємо таблицю k[][] from bottom to top
    for i in range(0, len(sorted_coin_nominals_list) + 1):  # рядки - номінали монет
        for s in range(1, change_sum + 1):  # стовпці - проміжні суми решти, для яких розраховуємо проміжні результати
            if i == 0:  # базовий випадок
                k[i][s] = [min(sorted_coin_nominals_list) for _ in range(s // min(sorted_coin_nominals_list))] # заповнюємо монетами найменшого номіналу
            elif sorted_coin_nominals_list[i - 1] <= s:  # якщо поточний номінал монет менше або дорівнює поточній сумі решти
                temp = []  # розраховуємо варіант як сумму поточного номіналу та вже знайденого рішення з комірки, з індексом = різниці між поточною сумою та поточним номіналом
                temp.extend(k[i][s - sorted_coin_nominals_list[i - 1]])
                temp.extend([sorted_coin_nominals_list[i - 1]])
                if len(temp) < len(k[i-1][s]):  # порівнюємо розрахований варінт з рішенням з верхньої комірки, тобто найкращим для цієї поточної суми рішення на основі попередньо обчислених номіналів
                    k[i][s] = temp #рішення з верхньої комірки, тобто найкраще для цієї поточної суми рішення на основі попередньо обчислених номіналів
                else:
                    k[i][s] = k[i-1][s]  # то додаємо рішення з верхньої комірки, тобто найкраще для цієї поточної суми рішення на основі попередньо обчислених номіналів
            else:  # якщо поточний номінал більше ніж поточна сума,
                temp = []
                temp.extend(k[i-1][s])  # то додаємо рішення з верхньої комірки, тобто найкраще для цієї поточної суми рішення на основі попередньо обчислених номіналів
                k[i][s] = temp
    # print(k)
    result = k[len(sorted_coin_nominals_list)][change_sum]

    # друкуємо рішення у наочному вигляді - список монет, з яких складається сума решти - як на мене, то так зручніше сприймати результат
    print(f'\nСписок монет для решти в {change_sum} грошових одиниць = {result}')

    # але через те, що за умовами завдання треба повернути словник, то
    # наповнюємо словник ключами з тих номіналів монет, що є у рішенні,
    res_dict = {}
    for nom in set(result):
        res_dict[nom] = 0

    # підраховуємо кількість монет кожного номіналу
    for coin in result:
        res_dict[coin] += 1

    # повертаємо відповідь у вигляді словника, як того вимагають умови завдання
    return res_dict


change_sum = 113
print(f'Решта {change_sum} грошових одиниць у тому вигляді, як вимагає задача: {find_coins_dynamic(change_sum)}\n')
