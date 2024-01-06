
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


    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("x1_values", DATA_X)
    def test_x2(self, x1_values):
        assert x1_values == 2

    @pytest.mark.sanity
    @pytest.mark.usefixtures('print_fixture_use')
    @pytest.mark.parametrize("y1_values", DATA_Y)
    def test_y2(self, y1_values):
        assert y1_values == 2
