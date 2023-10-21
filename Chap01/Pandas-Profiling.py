# 판다스 프로파일링
# 데이터 내 값의 분포, 변수 간의 관계, Null값과 같은 결측값(missing values)
# 존재 유무 등을 파악하는 것을 EDA(탐색적 데이터 분석)이라고 한다.
# 이 과정에서는 많은 양의 데이터를 가진 데이터프레임을
# .profile_report()라는 명령으로 탐색하느 ㄴ패키지인 판다스 프로파일링을 알아보자.
# pip install -U pandas-profiling으로 설치가 필요하다.

# 1. 실습파일 불러오기
import pandas as pd
import pandas_profiling
data = pd.read_csv('spam.csv', encoding='latin1')
# 5개의 행만 출력해보자
data[:5]

# 2. 리포트 생성하기
pr = data.profile_report() # 프로파일링 결과 리포트를 pr에 저장
# data.profile_report() # 바로 결과 보기
pr.to_file('./pr_reprot.html') # pr_report.html 파일로 저장