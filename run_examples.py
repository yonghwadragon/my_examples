from modules.module_manager import ModuleManager
from modules.executor import Executor

def main():
    manager = ModuleManager()
    executor = Executor(manager)
    executor.execute()

if __name__ == "__main__":
    main()