import lang.templete
def choose_lang(lang:str)->lang.templete:
        import importlib
        return importlib.import_module(f"lang.{lang.replace('-', '_')}")