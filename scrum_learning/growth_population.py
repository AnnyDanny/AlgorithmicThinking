import math

def percentage(percent, whole):
  return math.floor((percent * whole) / 100.0)


def nb_year(p0, percent, aug, p):
    year = p0
    counter = 0
    i = 0
    while i <= p - 1:
        year = percentage(percent, year) + year + aug
        counter += 1
        i += 1
        if year >= p:
            break
    return counter


def test_mytest():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94