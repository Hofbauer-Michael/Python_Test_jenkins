import conftest
import pytest


class Test_03:
    DATA_X = (
        1,
        1,
        1,
        1
    )

    DATA_Y = (
        1,
        1,
        1,
        1
    )

    @pytest.mark.skip
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("x1_values", DATA_X)
    def test_x1(self, x1_values):
        assert x1_values == 1

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("y1_values", DATA_Y)
    def test_y1(self, y1_values):
        assert y1_values == 1

class Test_04:
    DATA_X = (
        1,
        1,
        1,
        1
    )

    DATA_Y = (
        1,
        1,
        1,
        1
    )

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("x1_values", DATA_X)
    def test_x1(self, x1_values):
        assert x1_values == 1

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("y1_values", DATA_Y)
    def test_y1(self, y1_values):
        assert y1_values == 1

