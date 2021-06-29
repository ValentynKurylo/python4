'''
прога, що виводить кількість кожного символа з введеної строки,
наприклад:
st = 'as 23 fdfdg544' #введена строка
'''

st = 'as 23 fdfdg544'
s = []
for i in st:
   s.append((i, st.count(i)))
s.sort()
for j in range(1, len(s)):
   if s[j] != s[j-1]:
      print(s[j])



'''
1)  есть лист:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
пример:
['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list = ['GT' if i > 4 else 'LT' for i in numbers]
print(list)
'''

'''
2) есть два листа:
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]

записать в лист тюплы (x,y) если x+y == 0
пример:
[(1, -1), (2, -2), (5, -5)]
'''
'''
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
t = [(i, j) for i in list1 for j in list2 if i + j == 0]
print(t)
'''