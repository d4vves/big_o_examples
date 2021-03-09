### O(1) - Constant - O of 1

# list = ['Dave', 'Taylor', 'Kenny', 'Jason']

# def constant(list):
#     return list[-1]

# print(constant(list))

### O(n) - Linear - O of N

# def linear(list):
#     for idx, name in enumerate(list):
#         print(idx, name)

# linear(list)

### O(n^2) - Quadratic - O of n squared

# def quadratic(list):
#     for name in list:
#         for letter in name:
#             print(letter)

# quadratic(list)

### O(log(n)) - Logarithmic - O of log n

# name_list = ['Blake', 'Chassity', 'Dave', 'Drake', 'Elyssa', 'Ilka', 'Jackson', 'Jason', 'Jeffrey', 'Jeremiah', 'Kenny', 'Patrick', 'Taylor', 'Trisha' 'Vince', 'Yasaman']

## LINEAR VERSION TO COMPARE LOG VERSION TO:

# def linear(list, search):
#     count = 0
#     for name in list:
#         count += 1
#         print('ITERATION:', count)
#         if name == search:
#             return f'Found value of {name}.'

# print(linear(name_list, 'Blake'))

## LOG VERSION:

# def logarithmic(list, search):
#     count = 0
#     min = 0
#     max = len(list) - 1
#     index = None
#     element = None

#     while min <= max:
#         print('MIN:', min)
#         print('MAX:', max)
#         index = int((min + max) / 2)
#         element = list[index]
#         print('NEW INDEX', index)
#         print('NEW ELEM:', element)
#         count += 1
#         print('ITERATION', count)

#         if element < search:
#             min = index + 1
#         elif element > search:
#             max = index - 1
#         else:
#             return f'Found Value of {element}.'
#     return False

# print(logarithmic(name_list, 'Blake'))