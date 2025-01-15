# **My Examples Project**

이 프로젝트는 Python으로 다양한 주제별 예제 코드를 관리하고 실행하기 위해 설계되었습니다. 사용자는 주제를 선택하고, 각 예제를 동적으로 탐색하여 실행할 수 있습니다.

---

## **프로젝트 구조**

프로젝트는 다음과 같이 구성되어 있습니다:

```
my_examples/
│
├── examples/                  # 예제 코드 파일이 포함된 디렉토리
│   ├── __init__.py            # 패키지를 초기화하고 모듈 로드를 처리
│   ├── tkinter_examples.py    # tkinter를 활용한 GUI 관련 예제 코드
│   ├── ml_examples.py         # 머신러닝 예제 코드
│   ├── analysis_examples.py   # 데이터 분석 예제 코드
│   ├── mmm.py                 # 기타 예제 코드 (테스트용 또는 일반 기능)
│
├── modules/                   # 모듈 관리 및 실행 로직
│   ├── __init__.py            # 패키지 초기화
│   ├── module_manager.py      # 모듈 탐색 및 로드 담당
│   ├── executor.py            # 사용자 입력 및 예제 실행 담당
│
├── run_examples.py            # 프로젝트의 메인 실행 파일
├── README.md                  # 프로젝트 설명 파일
├── requirements.txt           # 필요한 Python 패키지 목록
```

---

## **설치 및 실행**

### **1. 설치**

1. **Python 설치**:
   - [Python 공식 웹사이트](https://www.python.org/downloads/)에서 **Python 3.8 이상**을 설치합니다.

2. **필요한 패키지 설치**:
   ```bash
   pip install -r requirements.txt
   ```

---

### **2. 실행**

다음 명령어로 프로젝트를 실행합니다:
```bash
python run_examples.py
```

**출력 예시**:
```plaintext
=== 예제 주제 선택 ===
1. tkinter_examples - GUI 예제
2. ml_examples - 머신러닝 예제
3. analysis_examples - 데이터 분석 예제
실행할 주제 번호를 입력하세요 (예: 1):
```

---

## **새로운 예제 추가**

프로젝트는 새로운 주제나 예제를 쉽게 확장할 수 있도록 설계되었습니다.

### **1. 새로운 주제 추가**
1. `examples/` 디렉토리에 새 `.py` 파일 생성. 예:
   ```plaintext
   examples/web_examples.py
   ```

2. `example_`으로 시작하는 함수 정의:
   ```python
   def example_1():
       """웹 기능을 시연하는 예제"""
       print("이것은 새로운 웹 기능 예제입니다.")
   ```

3. 새 파일과 함수는 실행 시 자동으로 탐색되고 메뉴에 추가됩니다.

---

## **베스트 프랙티스**

- **함수 이름 규칙**: 모든 예제 함수 이름은 반드시 `example_`으로 시작해야 탐색 및 실행 가능합니다.
- **Docstring 작성**: 함수 및 모듈에 의미 있는 Docstring을 작성하여 가독성을 높이세요:
  ```python
  """
  이 모듈은 웹 관련 기능을 시연하는 예제를 포함합니다.
  """
  ```

---

## **Git 사용 방법**

### **1. 저장소 복제**
1. [Git 공식 웹사이트](https://git-scm.com/downloads)에서 Git을 설치합니다.
2. 저장소를 복제:
   ```bash
   git clone https://github.com/yonghwadragon/my_examples.git

   ```

### **2. 프로젝트 실행**
1. 프로젝트 디렉토리로 이동:
   ```bash
   cd my_examples
   ```
2. 메인 스크립트 실행:
   ```bash
   python run_examples.py
   ```

---

## **추가 정보**

- **동적 예제 로딩**: `examples/` 폴더에 새 예제를 추가하면 자동으로 탐색되고 실행 가능합니다.
- **캐싱**: Python 실행 시 생성되는 `__pycache__/` 폴더는 안전하게 무시하거나 `.gitignore`에 추가할 수 있습니다.

---

## **기여 가이드라인**

다음과 같은 방식으로 프로젝트에 기여할 수 있습니다:
- 새로운 예제 추가.
- 문서 개선.
- 버그 수정 또는 코드 최적화.
