def past(h, m, s):
    milliseconds = int(3600000 * h + 60000 * m + 1000 * s)
    return milliseconds

if __name__ == "__main__":
    h = 0
    m = 1
    s = 1
    print(past(h, m, s))


def test_mytests():
    assert past(0,1,1) == 61000
    assert past(1,1,1) == 3661000
    assert past(0,0,0) == 0
    assert past(1,0,1) == 3601000
    assert past(1,0,0) == 3600000
