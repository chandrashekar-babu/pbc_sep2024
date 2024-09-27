import mathtools

def test_square_int():
    assert mathtools.square(2) == 4

def test_square_str():
    assert mathtools.square("hello") == 0

def test_sqrt_str():
    assert mathtools.sqrt("hello") == 0