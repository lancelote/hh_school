# Запись n! обозначает число равное произведению n*(n-1)*(n-2)*...*1 и
# называется факториал. Например, 6! = 6*5*4*3*2*1 = 720. Сумма всех цифр в
# факториале 6 равна 7+2+0=9
#
# Найдите сумму всех цифр в 252!

from math import factorial

print(sum(map(int, str(factorial(252)))))
