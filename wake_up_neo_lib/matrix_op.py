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
        """Check is the given matrix is 2D matrix, if it's true check inner matrix
        type"""

        t.List(t.List(inner_type)).check(matrix)
        for row in matrix:
            assert (
                all(
                    map(
                        lambda digit: isinstance(digit, inner_type),
                        row,
                    )
                )
                is True
            )


class MatrixView(Matrix2D):
    @property
    def matrix_object_view(self):
        """Return matrix object that we can work with"""

        return self.matrix

    def __str__(self):
        """
        Return classic matrix view. For e.g.:
        1 | 2 | 34
        5 | 6 | 21
        4 | 2 | 3
        """

        classic = "\n".join(
            [" | ".join(map(str, row)) for row in self.matrix_object_view]
        )
        return classic


class Matrix2DOperations(Matrix2D):
    def counter_clockwise_matrix(self, direction: int = 1) -> MatrixView:
        """Passes through given matrix onto counterclockwise direction and
        saved passed element. In the end return new matrix had got
        by spiral movement.

        It begins from top left corner and move into ↓ direction
        Direction value:
         ← direction = 0
         ↓ direction = 1
         → direction = 2
         ↑ direction = 3
        Moves will be continued until matrix has not ended.
        """

        if len(self.matrix) == 1:
            return MatrixView(self.matrix)

        result = []
        top = 0
        bottom = len(self.matrix) - 1
        left = 0
        right = len(self.matrix[0]) - 1
        direction = direction

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

        for el in range(len(self.matrix)):
            row_len = len(self.matrix[0])
            result.append(result[:row_len])
            del result[:row_len]

        self.matrix = result
        return MatrixView(self.matrix)
