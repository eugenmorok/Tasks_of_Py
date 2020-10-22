import sys
input_list = sys.argv[1:]
input_list.insert(0, 0)
#print(input_list)
empty_list = [sys.argv[1]]
for i in range(1, (len(input_list)-1)):
    a = int(input_list[i+1]) - int(input_list[i])
    a = str(a)
    #print(a)
    empty_list.append(a)
    #print(empty_list)
print(" ".join(empty_list))

import sys

values = sys.argv[1:]

# Список для хранения значений.
diff_values = []

# Предыдущее значение.
prev_value = 0

for value in values:
    # Вычисляем разницу.
    value = int(value)
    diff = value - prev_value

    # Добавляем в список.
    diff_values.append(str(diff))

    # Обновляем прошлое значение.
    prev_value = value

# Выводим результат.
print(" ".join(diff_values))