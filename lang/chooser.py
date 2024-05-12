from types import ModuleType
def choose_lang(lang:str)->ModuleType:
        import importlib
        return importlib.import_module(f"lang.{lang.replace('-', '_')}")