doors = [False] * 101 # мы можем начать с двери 1. Будем игнорировать индекс 0 
 
for i in range(1, 101): 
    # для второго прохода х=2, поэтому мы начинаем с двери 2, для 3-го прохода мы начинаем с двери 3 и т.д. 
    for j in range(i, 101, i): 
        doors[j] = not doors[j] # использование "not" для инвертирования логического значения  
# выводим значение только открытых дверей 
for i in range(1, 101): 
    if doors[i] is True: # или просто если двери[i]: 
        print(i)