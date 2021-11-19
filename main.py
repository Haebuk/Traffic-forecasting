from traffic.traffic_forecasting import TrafficForecasting

if __name__ == '__main__': # 예측값 테스트 프린팅
    tf = TrafficForecasting()
    print(tf.predict())