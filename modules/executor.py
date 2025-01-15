# executor.py
import inspect

class Executor:
    """사용자 입력 처리 및 예제 실행"""
    def __init__(self, module_manager):
        self.module_manager = module_manager

    def execute(self):
        modules = self.module_manager.list_modules()

        # 모듈 목록 출력
        print("=== 예제 주제 선택 ===")
        for i, (module_name, desc) in enumerate(modules.items(), 1):
            print(f"{i}. {module_name} - {desc or 'No description available'}")

        # 사용자 입력
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

        # 모듈 로드 및 실행
        module = self.module_manager.load_module(selected_module)
        examples = {
            name: func
            for name, func in vars(module).items()
            if name.startswith("example_") and callable(func)
        }

        print(f"=== {selected_module} 예제 실행 ===")
        for i, (name, func) in enumerate(examples.items(), 1):
            doc = inspect.getdoc(func) or "No description available."
            print(f"{i}. {name} - {doc}")

        # 사용자 입력 처리
        while True:
            try:
                example_choice = int(input("실행할 예제 번호를 입력하세요 (예: 1): "))
                if 1 <= example_choice <= len(examples):
                    selected_example = list(examples.values())[example_choice - 1]
                    print(f"{selected_example.__name__}을(를) 실행합니다...")
                    selected_example()
                    break
                else:
                    print("유효하지 않은 번호입니다. 다시 입력하세요.")
            except ValueError:
                print("숫자를 입력해야 합니다. 다시 입력하세요.")