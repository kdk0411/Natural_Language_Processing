# 3. 맷플롯립
#   맷플롯립은 데이터를 차트(chart)나 플롯(plot)으로 시각화하는 패키지이다.
#   데이터 분석에서 Matplotlib은 데이터 분석 이전에 데이터 이해를 위한
#   시각화나, 데이터 분석 후에 결과를 시각화하기 위해서 사용된다.
#   import matplotlib.pyplot as plt로 사용한다.

# 3-1. 라인 플롯 그리기
#   plt.plot()은 라인 플롯을 그리는 기능을 수행한다.
#   plot()에 x축과 y축의 값을 기재하고 그림을 표시하는 show()를 통해서 시각화해보자.
#   plt.title('test')
#   plt.plot([1,2,3,4],[2,4,8,6])
#   plt.show()

# 3-2. 축 레이블 삽입하기
#   x축과 y축 각각에 축이름을 삽입하고 싶다면 xlabel('넣고 싶은 축이름')과
#   ylabel('넣고 싶은 축이름')을 사용한다.
#   plt.title('test')
#   plt.plot([1,2,3,4],[2,4,8,6])
#   plt.xlabel('hours')
#   plt.ylabel('score')
#   plt.show()

# 3-3. 라인 추가와 범례 삽입하기
#   다수의 plot()을 하나의 그래프에 나타낼 수 있다. 여러개의 라인 플롯을
#   동시에 사용할 경우에는 각 선이 어떤 데이터를 나타내는지를 보여주기 위해 범례(legend)
#   를 사용할 수 있다.
#   plt.title('students')
#   plt.plot([1,2,3,4],[2,4,8,6])
#   plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
#   plt.xlabel('hours')
#   plt.ylabel('score')
#   plt.legend(['A student', 'B student']) # 범례 삽입
#   plt.show()