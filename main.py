def find_max(numbers):
    """Возвращает максимальный элемент списка."""
    if not numbers:
        return None
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


print(find_max([3, 7, 2, 9, 4]))    # 9
print(find_max([-5, -2, -8, -1]))   # должно быть -1