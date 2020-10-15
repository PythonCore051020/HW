FOUR_DIGIT_NUMBER = 7859

mul = 1
for i in str(FOUR_DIGIT_NUMBER):
    mul = mul * int(i)

print(f"\nдобуток цифр числа {FOUR_DIGIT_NUMBER} = {mul}")

print(f"\nчисло {FOUR_DIGIT_NUMBER} в реверсному порядку {str(FOUR_DIGIT_NUMBER)[::-1]}")

print(f"\nПосортувати цифри, що входять в число {FOUR_DIGIT_NUMBER} {sorted(str(FOUR_DIGIT_NUMBER))}")

