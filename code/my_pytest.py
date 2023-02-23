def func(x):
    return x + 1


def test_func():
    assert func(12) == 13

if __name__ == '__main__':
    pytest.main([__file__])
