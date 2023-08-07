import pytest


@pytest.fixture(scope="class")
def correct_matrix():
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]

