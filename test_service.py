from mock import patch
from service import Service

@patch('service.Service.bad_random')
def test_bad_random(bad_random):
    service = Service()

    bad_random.return_value = 0
    assert service.bad_random() == 0

    bad_random.return_value = 2
    assert service.bad_random() == 2


@patch('service.Service.bad_random')
def test_divide(bad_random):
    service = Service()

    bad_random.return_value = 2
    assert service.divide(1) == 2
    assert service.divide(2) == 1

    bad_random.return_value = -4
    assert service.divide(-4) == 1
    assert service.divide(-2) == 2
    assert service.divide(4) == -1

    bad_random.return_value = 0
    assert service.divide(1) == 0


    #test for dividing number by zero
    bad_random.return_value = 3
    try:
        service.divide(0)
    except ZeroDivisionError:
        assert True

def test_abs_plus():
    service = Service()

    assert service.abs_plus(-1) == 2

    assert service.abs_plus(0) == 1

    assert service.abs_plus(1) == 2

# @patch('service.Service.bad_random')
# @patch('service.Service.divide')
# def test_complicated_function():
#     service = Service()
#     print("function4")