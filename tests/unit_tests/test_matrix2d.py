import pytest

from Wake_up_Neo.wake_up_neo_lib.matrix_op import Matrix2D, Matrix2DOperations


class TestMatrix2D:
    @pytest.mark.parametrize(
        "matrix",
        [
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [0, 0],
                [11, 11],
            ],
        ],
    )
    def test_init(self, matrix):
        assert isinstance(Matrix2D(matrix), Matrix2D)
        assert Matrix2D.is_2d_matrix(matrix) is None

    @pytest.mark.parametrize(
        "matrix",
        [
            [
                [1, "23"],
                [2, 123],
            ],
            [
                [1, 2],
                [3, 4.2],
            ],
            [[[[]]]],
        ],
    )
    def test_init_fail(self, matrix):
        with pytest.raises(Exception):
            assert Matrix2D.is_2d_matrix(matrix) is None


class TestMatrix2DOperations:
    def test_counter_clockwise_matrix(self, correct_matrix):
        assert Matrix2DOperations(
            correct_matrix
        ).counter_clockwise_matrix().matrix_object_view == [
            [1, 5, 6, 7],
            [8, 4, 3, 2],
        ]
