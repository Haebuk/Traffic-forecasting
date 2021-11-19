# 과제 상세

 - 주제: 뒤끝의 서버에는 많은 트래픽이 발생하므로, 이를 예측하는 일이 중요합니다. 이전 하루 동안의 트래픽을 기반으로 다음 1시간 동안의 트래픽을 예측하는 모듈을 작성하고, 이를 서버 개발팀에 제공하기 위하여 API화 하십시오.

 - 조건: 사용 기술 스택은 전부 자유. 모듈의 예측값은 5분 단위의 값이며, 길이가 12인 리스트가 반환되어야 합니다.

 - 기타: 
    1. 예측 알고리즘은 간단해도 됩니다. 모델의 수준보다는 그 외적인 부분에 집중하여 평가하겠습니다.

    2. 이전 하루 동안의 트래픽은 http://ec2-3-37-89-254.ap-northeast-2.compute.amazonaws.com/data 에서 얻으실 수 있습니다.  

# 코드 설명
## 구조
```
📦ROOT
    ┣ ...
    📦traffic
        ┣📜constants.py
        ┣📜requirements.txt
        ┗📜traffic_forecasting.py
    ┣📜.gitignore
    ┣📜app.py
    ┣📜Dockerfile
    ┣📜main.py
    ┗📜README.md
```
- 서버 실행 파일은 `📦traffic` 폴더 바깥에 있다고 가정했습니다. (`📜app.py`)
- `📜main.py`에는 예측 리스트를 받을 수 있는 테스트 코드가 작성되어 있습니다.
- `📜Dockerfile`에는 이미지 빌드 후 실행 시 `📜main.py`와 동일한 역할을 수행합니다.

## Quick Start
- 5분 단위로 이루어진 다음 1시간 트래픽 예측량 리스트 출력
     ```
    $ python main.py
    ```
- 도커로 실행시
    ```
    $ docker pull cwryu6252/traffic-forecasting:latest &&
    docker run cwryu6252/traffic-forecasting:latest 
    ```
- 플라스크 웹 서버에서 API 호출
    ```
    $ python app.py
    ```
    `{server_url}/traffic/forecast` 에서 리스트 값 반환 가능
    - 결과
    ```
    $ curl -X POST localhost:5000/traffic/forecast
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100   225  100   225    0     0     28      0  0:00:08  0:00:07  0:00:01    48
    [1425.5492601384008,1531.4423927925939,1526.2836938530781,1566.2790600700112,1526.324701155978,1580.840447060151,1622.9621260236993,1636.082338095713,1651.163896343029,1654.2682001856952,1665.240301746872,1677.5182890983544]
    ```
