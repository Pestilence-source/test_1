d1 = 100
d2 = 200
res = d1 + d2
print(res)
print('Добавил первый пользователь')


def test_func(x):
    print(x)


def test_func_2(x: [int, float], y: [int, float]) -> [int, float]:
    res = x + y
    return res