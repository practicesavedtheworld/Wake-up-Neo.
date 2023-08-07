# Wake-up-Neo.



<details> 
 <summary> :pencil2: TEST ASSIGNMENT </summary> 
 <details>
   <summary> RU</summary>
   Тестовое задание требует написать библиотеку, включающую функцию "counter_clockwise_matrix". Эта функция должна принимать на вход двумерный массив или матрицу и 
выполнять обход элементов этой матрицы по спирали против часовой стрелки, начиная с верхнего левого угла. Результатом работы функции должна быть 
новая матрица, содержащая элементы исходной матрицы, расположенные в порядке обхода по спирали.

Подробнее о процессе обхода матрицы по спирали против часовой стрелки:

Пройти по правому столбцу матрицы сверху вниз.
Пройти по верхней строке матрицы слева направо.
Пройти по нижней строке матрицы справа налево.
Пройти по левому столбцу матрицы снизу вверх.
Этот процесс повторяется для оставшейся внутренней матрицы, если она существует, и продолжается до тех пор, пока все элементы матрицы не будут пройдены.

Например, если входная матрица имеет следующий вид:

1  2  3

4  5  6

7  8  9

То результатом работы функции "counter_clockwise_matrix" будет новая матрица:


1  4  7

8  9  2

5  6  3


Таким образом, задача заключается в написании библиотеки, содержащей функцию "counter_clockwise_matrix", которая будет выполнять обход
элементов входной матрицы по спирали против часовой стрелки, начиная с верхнего левого угла, и возвращать новую матрицу с элементами в заданном порядке.
 </details>

<details>
  <summary> EN </summary>

  The test assignment requires writing a library that includes the "counter_clockwise_matrix" function. This function must take a two-dimensional array or matrix as input and
traverse the elements of this matrix in a counterclockwise spiral, starting from the upper left corner. The result of the function should be
a new matrix containing the elements of the original matrix arranged in helix order.

More about the process of traversing the matrix in a counterclockwise spiral:

Go through the right column of the matrix from top to bottom.
Go through the top row of the matrix from left to right.
Walk along the bottom row of the matrix from right to left.
Go through the left column of the matrix from bottom to top.
This process is repeated for the remaining internal matrix, if it exists, and continues until all matrix elements have been traversed.

For example, if the input matrix is:

1 2 3

4 5 6

7 8 9

Then the result of the "counter_clockwise_matrix" function will be a new matrix:


1 4 7

8 9 2

5 6 3


So the challenge is to write a library containing a "counter_clockwise_matrix" function that will traverse
elements of the input matrix in a counterclockwise spiral, starting from the top left corner, and return a new matrix with elements in the given order.
</details>

</details>


In the created library, I decided to split the work with matrices into 3 entities. The functionality of the library is simple and includes checking that the input was a matrix, performing operations with the matrix, and getting a matrix object.

## Usage


### Requirements
```sh
git clone https://github.com/practicesavedtheworld/Wake_up_Neo..git
```
```sh
pip install requirements.txt dev-requirements.txt
```

### Run tests
```sh
cd Wake_up_Neo
```
```sh
pytest tests/ -v
```

### Using without installation

Works as a standart import

![matr import demo](https://github.com/practicesavedtheworld/Wake_up_Neo./assets/105741091/d38fbfbb-9a66-439f-a9bf-0c8de7c50bb8)


