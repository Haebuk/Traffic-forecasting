import io

import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
import numpy as np

from traffic import constants


class TrafficForecasting:
    """이전 하루 동안의 트래픽을 기반으로 다음 1시간 동안의 트래픽을 예측하는 모듈에 대한 클래스
    """

    def __init__(self):
        self.url = constants.URL
        self.window_size = constants.WINDOW_SIZE
        self.response = constants.RESPONSE

    def get_df_from_url(self):
        """트래픽 데이터 URL로 부터 데이터프레임을 생성하는 함수

        Returns:
            [pandas.core.frame.DataFrame]: 트래픽 데이터 데이터프레임
        """
        s = requests.get(self.url).content
        df = pd.read_json(io.StringIO(s.decode("utf-8")))
        return df

    def create_windows(self):
        """트래픽 데이터 데이터프레임에서 윈도우를 생성하는 함수

        Returns:
            X: [numpy.ndarray]: 트래픽 윈도우 데이터
            y: [numpy.ndarray]: X 마지막 값의 바로 다음 값
        """
        df = self.get_df_from_url()
        X, y = [], []
        for i in range(self.window_size, len(df)):
            X.append(df["traffic"][i - self.window_size : i])
            y.append(df["traffic"][i])
        return np.array(X), np.array(y)

    def create_model(self):
        """트래픽 예측을 위한 모델을 생성하는 함수
        Linear Regression 모델에 윈도우 데이터로 변환한 데이터로 학습

        Returns:
            [sklearn.linear_model._base.LinearRegression]: 데이터를 학습한 모델
        """
        X, y = self.create_windows()
        model = LinearRegression()
        model.fit(X, y)
        return model

    def predict(self):
        """학습한 모델을 바탕으로 다음 1시간의 트래픽을 예측하는 함수
        1. X의 마지막 윈도우에서 값을 예측하고, 예측 값을 X에 추가
        2. 예측 값을 반환 리스트에 추가
        3. 1,2를 반복하여 길이가 12인(5분 단위 1시간) 리스트 생성

        Returns:
            [list]: 5분 단위로 예측된 길이가 12인 트래픽 데이터 리스트
        """
        df = self.get_df_from_url()
        model = self.create_model()
        result = []
        X = df["traffic"].values
        for _ in range(12):
            result.append(model.predict(X[-self.window_size :].reshape(1, -1)))
            X = np.append(X, result[-1])
        result = list(map(lambda x: x[0], result))
        return result
