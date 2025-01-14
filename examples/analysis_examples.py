"""
데이터 분석 예제 코드
"""
def example_1():
    """데이터프레임 생성 예제"""
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    print(df)

def example_2():
    """간단한 데이터 시각화"""
    import matplotlib.pyplot as plt
    x = [1, 2, 3]
    y = [4, 5, 6]
    plt.plot(x, y)
    plt.title("Simple Plot")
    plt.show()
