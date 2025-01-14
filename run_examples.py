# 실행 파일 (주제 선택 및 예제 실행)
import pkgutil
import importlib
import examples
import inspect

def list_modules():
    """지원되는 모듈 목록 동적 탐색"""
    modules = {}
    for loader, module_name, is_pkg in pkgutil.walk_packages(examples.__path__):
        module = importlib.import_module(f"examples.{module_name}")
        modules[module_name] = getattr(module, "__doc__", "No description available.")
    return modules

def main():
    # 주제 선택
    modules = list_modules()
    print("=== 예제 주제 선택 ===")
    for i, (module, desc) in enumerate(modules.items(), 1):
        print(f"{i}. {module} - {desc}")

    while True:
        try:
            choice = int(input("실행할 주제 번호를 입력하세요 (예: 1): "))
            if 1 <= choice <= len(modules):
                selected_module = list(modules.keys())[choice - 1]
                break
            else:
                print("유효하지 않은 번호입니다. 다시 입력하세요.")
        except ValueError:
            print("숫자를 입력해야 합니다. 다시 입력하세요.")

    # 모듈 동적 로드
    module = importlib.import_module(f"examples.{selected_module}")
    examples = {
        name: func
        for name, func in vars(module).items()
        if name.startswith("example_") and callable(func)
    }

    # 예제 선택
    print(f"=== {selected_module} 예제 실행 ===")
    for i, (name, func) in enumerate(examples.items(), 1):
        doc = inspect.getdoc(func) or "No description available."
        print(f"{i}. {name} - {doc}")

    while True:
        try:
            choice = int(input("실행할 예제 번호를 입력하세요 (예: 1): "))
            if 1 <= choice <= len(examples):
                selected_example = list(examples.values())[choice - 1]
                print(f"{selected_example.__name__}을(를) 실행합니다...")
                selected_example()
                break
            else:
                print("유효하지 않은 번호입니다. 다시 입력하세요.")
        except ValueError:
            print("숫자를 입력해야 합니다. 다시 입력하세요.")

if __name__ == "__main__":
    main()
