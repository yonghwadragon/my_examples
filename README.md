# 프로젝트 설명

# **My Examples Project**
이 프로젝트는 다양한 주제별 예제 코드를 관리하고 실행하기 위한 Python 프로젝트입니다. 주제별 예제를 선택하고, 각 예제를 동적으로 탐색하여 실행할 수 있습니다.

---

## **프로젝트 구조**
my_examples/
│
├── examples/
│   ├── __init__.py       # 공통 초기화 (패키지로 인식)
│   ├── tkinter_examples.py # GUI 관련 예제 코드
│   ├── ml_examples.py    # 머신러닝 관련 예제 코드
│   ├── analysis_examples.py # 데이터 분석 예제 코드
│
├── README.md             # 프로젝트 설명
├── run_examples.py       # 실행 파일 (주제 선택 및 예제 실행)


---

## **설치 및 실행**

### **1. 설치**
1. Python 설치:
   - [Python 공식 웹사이트](https://www.python.org/downloads/)에서 Python 3.8 이상을 설치합니다.

2. 필수 패키지 설치:
   - 다음 명령어를 사용하여 필요한 Python 패키지를 설치합니다:
     ```bash
     pip install -r requirements.txt
     ```
   - **예상 패키지 목록**:
     - `matplotlib`
     - `pandas`

---

### **2. 실행**
1. **`run_examples.py` 실행**:
   - 터미널에서 다음 명령어를 실행합니다:
     ```bash
     python run_examples.py
     ```

2. **출력 예시**:
=== 예제 주제 선택 ===

tkinter_examples - GUI 예제
ml_examples - 머신러닝 예제
analysis_examples - 데이터 분석 예제 실행할 주제 번호를 입력하세요 (예: 1):

3. **주제 선택**:
- 번호를 입력하여 실행할 주제를 선택합니다. 예:
  ```
  실행할 주제 번호를 입력하세요 (예: 1): 1
  ```

4. **예제 선택**:
- 선택한 주제의 예제를 번호로 선택합니다. 예:
  ```
  === tkinter_examples 예제 실행 ===
  1. example_1 - 간단한 윈도우 창 만들기
  2. example_2 - 버튼 추가하기
  3. example_3 - 텍스트 입력 창과 출력
  실행할 예제 번호를 입력하세요 (예: 1): 
  ```

5. **결과 확인**:
- 선택한 예제가 실행됩니다.

---

## **추가 및 확장**

### **1. 새로운 예제 추가**
1. **새로운 주제 추가**:
- `examples/` 폴더에 새 파일을 생성합니다. 예:
  ```
  examples/new_topic_examples.py
  ```

2. **예제 함수 정의**:
- 함수 이름은 반드시 `example_`으로 시작해야 합니다:
  ```python
  def example_1():
      """새로운 예제 설명"""
      print("이 예제는 새로운 주제입니다.")
  ```

3. **자동 탐색**:
- 새 주제를 추가하면 `run_examples.py`에서 자동으로 탐색하고 실행할 수 있습니다.

---

## **주요 코드 설명**

### **1. `__init__.py`**
- **역할**:
- `examples` 폴더를 Python 패키지로 인식.
- 모듈 탐색, 선택적 노출 등의 초기화를 설정.
- **사용 방법**:
- 원하는 설정(모듈 탐색, 주요 함수 노출 등)을 선택.

### **2. `tkinter_examples.py`**
- GUI 관련 예제 코드가 포함된 모듈.
- 예제 목록:
- `example_1`: 간단한 윈도우 창 만들기.
- `example_2`: 버튼 추가하기.
- `example_3`: 텍스트 입력 창과 출력.
- `example_4`: 간단한 계산기.

### **3. `run_examples.py`**
- 사용자 인터페이스 제공.
- 주제를 선택하고, 해당 주제의 예제를 실행하는 역할.

---

## **예제 주제 설명**

### **1. GUI 예제 (tkinter_examples.py)**
- Python의 `tkinter`를 활용한 GUI 예제.
- 실행 예시:
- 버튼 클릭 시 메시지 출력.
- 간단한 계산기 구현.

### **2. 머신러닝 예제 (ml_examples.py)**
- 머신러닝 관련 기초 예제:
- 선형 회귀, KNN 분류 등.

### **3. 데이터 분석 예제 (analysis_examples.py)**
- 데이터 분석 및 시각화 예제:
- `pandas`를 사용한 데이터프레임 생성.
- `matplotlib`를 활용한 간단한 플롯 생성.

---

- ## **Docstring 작성 시 주의사항**:
  1. **Docstring 위치**:
     - 반드시 파일의 **맨 위**에 작성되어야 합니다.
     - `import` 문보다 앞에 있어야 Python이 이를 모듈의 Docstring으로 인식합니다.
  2. **Docstring 형식**:
     - 삼중 따옴표(`"""`)로 감싸야 하며, 한 줄 또는 여러 줄로 작성 가능합니다.
     - 예:
       ```python
       """
       이 모듈은 GUI 관련 예제를 포함합니다.
       """

---

## **기타**
- **example_0 및 example_zz**:
  - 함수 이름이 `example_`으로 시작하기만 하면 탐색 및 실행에 포함됩니다.
  - 이름은 사전 순서로 정렬되어 출력됩니다. 예: `example_0`, `example_2`, `example_zz`.

- **파일 이름 규칙**:
  - 파일 이름은 `.py` 확장자를 가진 모든 파일이 탐색 대상입니다.
  - 예: `web_examples.py` 또는 `web.py` 모두 동작하며, 프로젝트 컨벤션에 따라 선택 가능합니다.
  
- **`__pycache__`**:
- Python이 실행 시 자동 생성하는 캐시 폴더.
- 삭제해도 문제가 없으며, 필요 시 `.gitignore`에 추가 가능.
- **확장성**:
- 새로운 예제를 추가하면 자동으로 실행 가능하도록 설계.