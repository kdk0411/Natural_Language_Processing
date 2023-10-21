# 2. Numpy
#   넘파이는 수치 데이터를 다루는 파이썬 패키지이다. Numpy의 핵심이라고 불리는
#   다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수
#   계산에서 주로 사용된다.
#   넘파이는 평의성 뿐만 아니라 속도면에서도 빠르다는 장점이 있다.
#   import numpy as np로 사용한다.
import numpy as np

# 2-1 np.array()
#   넘파이의 핵심은 ndarray이다. np.array는 리스트, 튜프, 배열로 부터 ndarray를
#   생성한다. 파이썬 자료구조 중 하나인 리스트를 가지고 배열을 생성해 보자.
#   # 1차원 배열
#   vec = np.array([1, 2, 3, 4, 5])
#   print(vec)
#   [1 2 3 4 5]
#   # 2차원 배열
#   mat = np.array([[10, 20, 30], [ 60, 70, 80]])
#   print(mat)
#   [[10 20 30]
#    [60 70 80]]
#   print('vec의 타입 :',type(vec))
#   print('mat의 타입 :',type(mat))
#   vec의 타입 : <class 'numpy.ndarray'>
#   mat의 타입 : <class 'numpy.ndarray'>
#   두가지가 동일한 타입을 가지는 것을 확인할 수 있다.
#
#   넘파이 배열에는 축의 개수(ndim)와 크기(shape)이 있다.
#   배열의 크기를 정확히 수지하는 것은 딥러닝에서 매우 중요하다.
#   print('vec의 축의 개수 :',vec.ndim) # 축의 개수 출력
#   print('vec의 크기(shape) :',vec.shape) # 크기 출력
#   vec의 축의 개수 : 1
#   vec의 크기(shape) : (5,)
#   print('mat의 축의 개수 :',mat.ndim) # 축의 개수 출력
#   print('mat의 크기(shape) :',mat.shape) # 크기 출력
#   mat의 축의 개수 : 2
#   mat의 크기(shape) : (2, 3)

# 2-2. ndarray의 초기화
#   np.zeros()는 배열의 모든 원소에 0을 삽입한다.
#   # 모든 값이 0인 2x3 배열 생성.
#   zero_mat = np.zeros((2,3))
#   print(zero_mat)
#   [[0. 0. 0.]
#    [0. 0. 0.]]
#
#   np.ones()는 배열의 모든 원소에 1을 삽입한다.
#   # 모든 값이 1인 2x3 배열 생성.
#   one_mat = np.ones((2,3))
#   print(one_mat)
#   [[1. 1. 1.]
#    [1. 1. 1.]]
#
#   np.full()은 배열에 사용자가 지정한 값을 삽입한다.
#   # 모든 값이 특정 상수인 배열 생성. 이 경우 7.
#   same_value_mat = np.full((2,2), 7)
#   print(same_value_mat)
#   [[7 7]
#    [7 7]]
#
#   np.eye()는 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성한다.
#   # 대각선 값이 1이고 나머지 값이 0인 2차원 배열을 생성.
#   eye_mat = np.eye(3)
#   print(eye_mat)
#   [[1. 0. 0.]
#    [0. 1. 0.]]
#    [0. 0. 1.]]
#
#   np.random.random()은 임의의 값을 가지는 배열을 생성한다.
#   # 임의의 값으로 채워진 배열 생성
#   random_mat = np.random.random((2,2)) # 임의의 값으로 채워진 배열 생성
#   print(random_mat)
#   [[0.3111881  0.72996102]
#    [0.65667734 0.40758328]]
#   이외에도 넘파이에는 배열을 만드는 다양한 방법이 존재한다.

# 2-3. np.arange()
#   np.arange(n)은 0 ~ n-1까지의 값을 가지는 배열을 생성한다.
#   # 0부터 9까지
#   range_vec = np.arange(10)
#   print(range_vec)
#   [0 1 2 3 4 5 6 7 8 9]
#
#   np.arange(i,j,k)는 i~j-1까지 k씩 증가하는 배열을 생성한다.
#   # 1부터 9까지 +2씩 적용되는 범위
#   n = 2
#   range_n_step_vec = np.arange(1, 10, n)
#   print(range_n_step_vec)
#   [1 3 5 7 9]

# 2-4. np.reshape()
#   np.reshape()은 내부 데이터는 변경하지 않으면서 배열의 구조를 바꾼다.
#   0~29까지의 숫자를 생성하는 arange(30)을 수행한 후, 원소의 개수가 30개
#   이므로 5행 6열의 행렬로 변경해보자.
#   reshape_mat = np.array(np.arange(30)).reshape((5,6))
#   print(reshape_mat)
#   [[ 0  1  2  3  4  5]
#    [ 6  7  8  9 10 11]
#    [12 13 14 15 16 17]
#    [18 19 20 21 22 23]
#    [24 25 26 27 28 29]]

# 2-5. 넘파이 슬라이싱
#   ndarray를 통해 만든 다차원 배열은 파이썬의 자료구조인 리스트처럼 슬라이스 기능을
#   지원한다. 슬라이싱 기능을 사용하여 특정 행이나 열들의 원소들에 접근할 수 있다.
#
#   mat = np.array([[1, 2, 3], [4, 5, 6]])
#   print(mat)
#   [[1 2 3]
#    [4 5 6]]
#   # 첫번째 행 출력
#   slicing_mat = mat[0, :]
#   print(slicing_mat)
#   [1 2 3]
#   # 두번째 열 출력
#   slicing_mat = mat[:, 1]
#   print(slicing_mat)
#   [2 5]

# 2-6. 넘파이 정수 인덱싱(Numpy integer indexing)
#   슬라이싱을 사용하면 배열로부터 부분 배열을 추출할 수 있지만 연속적이지 않은
#   원소로 배열을 만들 경우에는 슬라이싱으로는 만들 수 없다.
#   예를 들어 2행 2열의 원소와 5행 5열의 원소를 뽑아서 하나의 배열로 만들고자 하는 경우가 그렇다.
#   이 경우에는 인덱싱을 사용하여 배열을 구성할 수 있다.
#   인덱싱은 원하는 위치의 원소들을 뽑을 수 있다.
#
#   mat = np.array([[1, 2], [4, 5], [7, 8]])
#   print(mat)
#   [[1 2]
#    [4 5]
#    [7 8]]
#   특정 위치의 원소만을 가져와보자
#   # 1행 0열의 원소
#   # => 0부터 카운트하므로 두번째 행 첫번째 열의 원소.
#   print(mat[1, 0])
#   4
#   특정 위치의 원소 두 개를 가져와 새로운 배열을 생성해보자.
#   # mat[[2행, 1행],[0열, 1열]]
#   # 각 행과 열의 쌍을 매칭하면 2행 0열, 1행 1열의 두 개의 원소.
#   indexing_mat = mat[[2, 1],[0, 1]]
#   print(indexing_mat)
#   [7 5]

# 2-7. 넘파이 연산
#   넘파이를 사용하면 배열간 연산을 손쉽게 할 수 있다.
#   np,add(), np.subtract(), np.multiply(), np.divide()를 사용할 수 있다.
#   x = np.array([1,2,3])
#   y = np.array([4,5,6])
#   # result = np.add(x, y)와 동일.
#   result = x + y
#   print(result)
#   [5 7 9]
#
#   # result = np.subtract(x, y)와 동일.
#   result = x - y
#   print(result)
#   [-3 -3 -3]
#   # result = np.multiply(result, x)와 동일.
#   result = result * x
#   print(result)
#   [-3 -6 -9]
#   # result = np.divide(result, x)와 동일.
#   result = result / x
#   print(result)
#   [-3. -3. -3.]
#
#   넘파이에서 벡터와 행렬곱 또는 행렬끼리의 곱을 위해서는 np.dot()을 사용해야 한다.
#   mat1 = np.array([[1,2],[3,4]])
#   mat2 = np.array([[5,6],[7,8]])
#   mat3 = np.dot(mat1, mat2)
#   print(mat3)
#   [[19 22]
#    [43 50]]
