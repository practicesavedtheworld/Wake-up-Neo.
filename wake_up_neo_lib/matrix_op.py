import decimal
from dataclasses import dataclass
from typing import Any, TypeAlias

import trafaret as t

MATRIX: TypeAlias = list[list[int]]
INNER_MATRIX_ELEM_TYPE: TypeAlias = int, float, decimal.Decimal


@dataclass(slots=True)
class Matrix2D:
    matrix: MATRIX

    def __init__(self, matrix: MATRIX) -> None:
        """Initialize and checking"""

        self.is_2d_matrix(matrix=matrix)
        self.matrix = matrix

    @staticmethod
    def is_2d_matrix(matrix: Any, inner_type: INNER_MATRIX_ELEM_TYPE = int) -> None:
        """Check is the given matrix is 2D matrix, if it's true check inner matrix type"""

        t.List(t.List(t.Int)).check(matrix)
        for row in matrix:
            assert all(
                map(
                    lambda digit: isinstance(digit, inner_type),
                    row,
                )
            ) is True

    def counter_clockwise_matrix(self) -> MATRIX:
        """ """
        # TODO add descriptions

        if len(self.matrix) == 1:
            return self.matrix

        result = []
        top = 0
        bottom = len(self.matrix) - 1
        left = 0
        right = len(self.matrix[0]) - 1
        direction = 1

        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(right, left - 1, -1):
                    result.append(self.matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    result.append(self.matrix[i][left])
                left += 1
            elif direction == 2:
                for i in range(left, right + 1):
                    result.append(self.matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(self.matrix[i][right])
                right -= 1

            direction = (direction + 1) % 4

        # TODO need return the matrix view object

        return result
