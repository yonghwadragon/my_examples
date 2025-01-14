# examples/__init__.py

# 공통 초기화 (패키지로 인식)

"""
1. 2. 3. 에서 하나만 주석에서 빼서 사용.
"""

"""############# 1. 동적 노출 (모듈 탐색 기반) #############"""
import pkgutil
import importlib

# 모든 서브 모듈 동적으로 탐색 및 로드
__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    globals()[module_name] = module
    __all__.append(module_name)

# """############# 2. 선택적 노출 (주요 함수만 노출) #############"""
# from .tkinter_examples import example_1, example_2
# from .ml_examples import example_1 as ml_example_1, example_2 as ml_example_2
# from .analysis_examples import example_1 as analysis_example_1


# """############# 3. 모든 모듈 노출 #############"""
# # 각 모듈에서 모든 함수를 임포트
# from .tkinter_examples import *
# from .ml_examples import *
# from .analysis_examples import *