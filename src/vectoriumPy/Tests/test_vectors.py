import pytest

from vectoriumPy import Vectors


def test_vector_subtraction():
    result = Vectors(5, 7, 9) - Vectors(1, 2, 3)
    assert result.to_list() == [4.0, 5.0, 6.0]


def test_vector_scalar_multiplication():
    assert (Vectors(1, 2, 3) * 3).to_list() == [3.0, 6.0, 9.0]
    assert (3 * Vectors(1, 2, 3)).to_list() == [3.0, 6.0, 9.0]
    with pytest.raises(TypeError):
        Vectors(1, 2, 3) * Vectors(1, 2, 3)


def test_unit_vector():
    unit = Vectors(3, 4).unit_vector()
    assert unit.to_list() == pytest.approx([0.6, 0.8], rel=1e-6)
    with pytest.raises(ZeroDivisionError):
        Vectors(0, 0).unit_vector()


def test_angle_with():
    assert Vectors(1, 0).angle_with(Vectors(0, 1)) == pytest.approx(90, rel=1e-6)
    assert Vectors(1, 0).angle_with(Vectors(1, 0)) == pytest.approx(0, rel=1e-6)
    with pytest.raises(ZeroDivisionError):
        Vectors(0, 0).angle_with(Vectors(1, 0))
