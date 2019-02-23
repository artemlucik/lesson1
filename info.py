first_name = 'Artem'
last_name  = 'Lucishin'


print(f'{first_name} {last_name}')


list_test = ['3','5','7','9','10.5']
print(list_test)

list_test.append('Python')
print(list_test)

print(list_test[0])
print(list_test[-1])
print(list_test[1:5])

del list_test[-1]

print(list_test)

#####

dic = {'city': 'Moscow', 'temperature': '20'}
print(dic.get('city'))

dic['temperature'] = float(dic.get('temperature')) - 5

print(dic)


print(dic.get('country'))
print(dic.get('country', 'Russia'))


dic['date'] = '27.05.2019'

print(dic)
print(len(dic))

