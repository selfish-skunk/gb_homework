# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

n = int(input('Введите число n: '))

nums_gen = (num for num in range(1, n + 1) if num % 2 != 0)

print(list(nums_gen))
