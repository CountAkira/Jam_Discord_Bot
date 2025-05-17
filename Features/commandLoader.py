import importlib
import pkgutil
import inspect
import Features 

def load_all_commands(tree, mycursor):
    print("🔍 Loading commands...")
    for finder, name, ispkg in pkgutil.walk_packages(Features.__path__, prefix="Features."):
        try:
            module = importlib.import_module(name)

            for func_name, func in inspect.getmembers(module, inspect.isfunction):
                if func_name.startswith("register_"):
                    print(f"🔗 Registering: {func_name} from {name}")
                    func(tree, mycursor)
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
