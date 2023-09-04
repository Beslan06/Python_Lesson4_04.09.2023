def map_arguments(**kwargs):
    argument_mapping = {}
    for key, value in kwargs.items():
        argument_mapping[value if hashable(value) else str(value)] = key
    return argument_mapping

def hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

# Пример использования функции
result = map_arguments(a=1, b="Hello", c=[1, 2, 3], d={"name": "Kristina"})

# Вывод результата
for key, value in result.items():
    print(f"{key}: {value}")
