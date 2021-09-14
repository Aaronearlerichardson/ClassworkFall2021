

def is_numeric(num):
    try:
        float(num)
        return True
    except Exception:
        return False


def get_new_y(tupe_1: tuple, tupe_2: tuple, new_x):

    assert len(tupe_1) == 2
    x1, y1 = tupe_1[:]
    assert len(tupe_2) == 2
    x2, y2 = tupe_2[:]
    for i in (x1, y1, x2, y2, new_x):
        assert is_numeric(i)
    assert x1 != x2

    m = abs(y1 - y2) / abs(x1 - x2)
    b = y1 - (m * x1)
    new_y = m * new_x + b

    return new_y
