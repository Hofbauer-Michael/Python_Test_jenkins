
import conftest
import pytest


class Test:
    DATA_X = (
        1,
        1,
        1,
        1
    )

    DATA_Y = (
        1,
        2,
        1,
        1
    )

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("x1_values", DATA_X)
    @pytest.mark.parametrize("y1_values", DATA_Y)
    def test_one(self, x1_values, y1_values):
        assert x1_values == y1_values

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("x1_values", DATA_X)
    @pytest.mark.parametrize("y1_values", DATA_Y)
    def test_two(self, x1_values, y1_values):
        assert x1_values == y1_values

