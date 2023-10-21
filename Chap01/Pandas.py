# 1. Pandas
#   판다스는 파이썬 데이터 처리를 위한 라이브러리이다. 파이썬을 이용한
#   데이터 분석과 같은 작업에서 필수 라이브러리로 알려져있다.
#   import panads as pd로 사용한다.
# 1-1. Series(시리즈)
#   시리즈 클래스는 1차원 배열의 값에 각 값에 대응되는 인덱스를 부여할 수 있는 구조를 가지고 있다.
#   sr = pd.Series([17000, 18000, 1000, 5000],
#                  index=["피자", "치킨", "콜라", "맥주"])
#   print('시리즈 출력 :')
#   print('-'*15)
#   print(sr)
#   시리즈 출력 :
#   ---------------
#   피자    17000
#   치킨    18000
#   콜라     1000
#   맥주     5000
#   dtype: int64
#
#   값과 인덱스를 출력할 수 있다.
#   print('시리즈의 값 : {}'.format(sr.values))
#   print('시리즈의 인덱스 : {}'.format(sr.index))
#   시리즈의 값 : [17000 18000  1000  5000]
#   시리즈의 인덱스 : Index(['피자', '치킨', '콜라', '맥주'], dtype='object')

# 1-2. DataFrame(데이터프레임)
#   데이터프레임은 2차원 리스트를 매개변수로 전달한다. 2차원이므로 행,열 2가지의
#   인덱스가 존재한다. 이는 행과 열을 가지는 자료구조라고 할 수 있다.
#   시리즈가 인덱스+값이였다면 데이터프레임은 행,열,값으로 3가지의 값으로 구성된다.
#   values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   index = ['one', 'two', 'three']
#   columns = ['A', 'B', 'C']
#
#   df = pd.DataFrame(values, index=index, columns=columns)
#
#   print('데이터프레임 출력 :')
#   print('-'*18)
#   print(df)
#   데이터프레임 출력 :
#   ------------------
#          A  B  C
#   one    1  2  3
#   two    4  5  6
#   three  7  8  9
#
#   데이터프레임의 값을 출력할 수 있다.
#   print('데이터프레임의 인덱스 : {}'.format(df.index))
#   print('데이터프레임의 열이름: {}'.format(df.columns))
#   print('데이터프레임의 값 :')
#   print('-'*18)
#   print(df.values)
#   데이터프레임의 인덱스 : Index(['one', 'two', 'three'], dtype='object')
#   데이터프레임의 열이름: Index(['A', 'B', 'C'], dtype='object')
#   데이터프레임의 값 :
#   ------------------
#   [[1 2 3]
#    [4 5 6]
#    [7 8 9]]

# 1-3. 데이프레임 생성
#   데이터프레임은 리스트(List), 시리즈(Series), 딕셔너리(Dict), Numpy의 ndarrys,
#   또 다른 데이터프레임으로부터 생성할 수 있다.
#   리스트와 딕셔너리로 데이터프레임을 생성해보자.
#   1. 이중 리스트로 생성
#   data = [
#       ['1000', 'Steve', 90.72],
#       ['1001', 'James', 78.09],
#       ['1002', 'Doyeon', 98.43],
#       ['1003', 'Jane', 64.19],
#       ['1004', 'Pilwoong', 81.30],
#       ['1005', 'Tony', 99.14],
#   ]
#
#   df = pd.DataFrame(data)
#   print(df)
#         0         1      2
#   0  1000     Steve  90.72
#   1  1001     James  78.09
#   2  1002    Doyeon  98.43
#   3  1003      Jane  64.19
#   4  1004  Pilwoong  81.30
#   5  1005      Tony  99.14
#   생성된 데이터프레임에 열을 지정할 수 있다.
#   df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
#   print(df)
#        학번        이름     점수
#   0  1000     Steve  90.72
#   1  1001     James  78.09
#   2  1002    Doyeon  98.43
#   3  1003      Jane  64.19
#   4  1004  Pilwoong  81.30
#   5  1005      Tony  99.14
#
#   2.딕셔너리를 통해 데이터프레임을 생성해보자.
#   data = {
#       '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
#       '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
#       '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
#       }
#
#   df = pd.DataFrame(data)
#   print(df)
#        학번        이름     점수
#   0  1000     Steve  90.72
#   1  1001     James  78.09
#   2  1002    Doyeon  98.43
#   3  1003      Jane  64.19
#   4  1004  Pilwoong  81.30
#   5  1005      Tony  99.14

# 1-4. 데이터프레임 조회
#   아래 명령어는 데이터프레임에서 원하는 구간만을 확인하기 위해 사용된다.
#   df.head(n) -> 앞 부분을 n개만 보기
#   df.tail(n) -> 뒷 부분을 n개만 보기
#   df['열이름'] -> 해당되는 열을 확인
#
#   실습
#   # 앞 부분을 3개만 보기
#   print(df.head(3))
#        학번      이름     점수
#   0  1000   Steve  90.72
#   1  1001   James  78.09
#   2  1002  Doyeon  98.43
#   # '학번'에 해당되는 열을 보기
#   print(df['학번'])
#   0    1000
#   1    1001
#   2    1002
#   3    1003
#   4    1004
#   5    1005
#   Name: 학번, dtype: object

# 1-5. 외부 데이터 읽기
#   Pandas는 CSV, 텍스트, Excel, SQL, HTML, JSON등 다양한 데이터 파일을 읽고
#   데이터프레임을 생성할 수 있다.
#   아래는 csv파일을 읽는 것이다.
#   df = pd.read_csv('example.csv')
#   print(df)
#      student id      name  score
#   0        1000     Steve  90.72
#   1        1001     James  78.09
#   2        1002    Doyeon  98.43
#   3        1003      Jane  64.19
#   4        1004  Pilwoong  81.30
#   5        1005      Tony  99.14
#   이경우에는 인덱스가 자동으로 부여된다.
#   print(df.index)
#   RangeIndex(start=0, stop=6, step=1)
