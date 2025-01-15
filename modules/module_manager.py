# module_manager.py
import pkgutil
import importlib
import examples

class ModuleManager:
    """모듈 및 예제를 동적으로 탐색 및 로드"""
    def list_modules(self):
        """지원되는 모듈 목록 탐색"""
        return {
            module_name: importlib.import_module(f"examples.{module_name}").__doc__
            for _, module_name, _ in pkgutil.walk_packages(examples.__path__)
        }

    def load_module(self, module_name):
        """모듈 로드"""
        return importlib.import_module(f"examples.{module_name}")