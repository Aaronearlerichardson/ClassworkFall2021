
def is_numeric(num):
    try:
        float(num)
        return True
    except Exception:
        return False


def get_new_y(coords_1: tuple, coords_2: tuple, new_x):

    assert len(coords_1) == 2
    x1, y1 = coords_1[:]
    assert len(coords_2) == 2
    x2, y2 = coords_2[:]
    for i in (x1, y1, x2, y2, new_x):
        assert is_numeric(i)
    assert x1 != x2

    m = abs(y1 - y2) / abs(x1 - x2)
    b = y1 - (m * x1)
    new_y = m * new_x + b

    return new_y


def check_third(coords_1: tuple, coords_2: tuple, check_coords: tuple):
    expected_y = get_new_y(coords_1, coords_2, check_coords[0])
    if expected_y == check_coords[1]:
        return True
    else:
        return False
