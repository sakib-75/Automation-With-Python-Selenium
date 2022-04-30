import pytest


@pytest.fixture(params=["a", "b", "c"])
def test_demo_params(request):
    param = request.param
    print("  SETUP mod arg", param)


@pytest.mark.parametrize("a,b,final", [(2, 4, 6), (3, 7, 10), (23, 21, 44)])
def test_demo_parametrize(a, b, final):
    assert a + b == final
