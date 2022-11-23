import numpy as np
count = 0
def random_predict(list_, item):
    
    low = 0
    high = len(list_) - 1
    
    global count
    
    while low <= high:
        count += 1
        mid = round((low + high) / 2)
        guess = list_[mid]
        if guess == item:
          return guess
        if guess > item:
          high = mid - 1
        else:
          low = mid + 1
    return None

my_list = []
for i in range(1, 101):
  my_list.append(i)

x = np.random.randint(1, 101)

print("Загаданное число:", random_predict(my_list, x))
print("Количество попыток:", count)