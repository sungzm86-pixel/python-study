name = input('이름을 입력하시오:')
birth_year = int(input('태어난 해를 입력하시오:'))
age = 2026 - birth_year

print(name, '님은 2026년에' ,age , '살 입니다.')
print(name + '님은 2026년에 ' + str(age) + '살 입니다.')
print('{}님은 2026년에 {}살 입니다.'.format(name, age))
print(f'{name}님은 2026년에 {age}살 입니다.')
#name 님은 2026년에 age살 입니다.