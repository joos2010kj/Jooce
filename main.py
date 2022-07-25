from pathlib import Path
from .utils import history
import inspect

class Jooce:
    @classmethod
    def state(cls):
        log = history("r")
        curr = log['__SELECT__']

        state = f"** Selection: {curr}\n** Functions: "
        state += ", ".join(log[curr]["functions"])

        print(state)

        return state

    @classmethod
    def list(cls, suppressed=False):
        log = history("r")

        lst = [f for f in log.keys() if f != "__SELECT__"]

        if not suppressed:
            print(lst)

        return lst
        
    @classmethod
    def create_storage(cls, name, override=False):
        log = history("r")

        if name in log and not override:
            raise SystemError("Filename already exists!")
        else:
            log[name] = {
                "path": str(Path(__file__).parent / "transcribe" / f"{name}.py"),
                "functions": [],
                "algorithms": []
            }

            history("w", log)

    @classmethod
    def select(cls, name):
        log = history("r")

        if name not in log:
            raise SystemError("Please double check the selected file path.")

        log["__SELECT__"] = name

        history("w", log)

    @classmethod
    def remove_storage(cls, name):
        log = history("r")

        if name not in log:
            raise SystemError("Please double check the selected file path.")

        del log[name]
        
        if log["__SELECT__"] == name:
            log["__SELECT__"] = None

        history("w", log)

    @classmethod
    def save(cls, func):
        log = history("r")
        curr = log["__SELECT__"]

        name = func.__name__
        code = inspect.getsource(func)
        code = "\n".join(code.split("\n")[:-1])

        assert name not in log[curr]["functions"], "Function name already exists"

        log[curr]["functions"].append(name)
        log[curr]["algorithms"].append(code)

        history("w", log)

    @classmethod
    def remove_function(cls, name):
        log = history("r")

        curr = log["__SELECT__"]

        if name not in log[curr]["functions"]:
            raise SystemError("Please double check the selected file path.")

        ind = log[curr]["functions"].index(name)

        del log[curr]["functions"][ind]
        del log[curr]["algorithms"][ind]
        
        history("w", log)

    @classmethod
    def transcribe(cls):
        log = history("r")
        curr = log["__SELECT__"]

        with Path(log[curr]['path']).open("w") as f:
            f.writelines('\n\n'.join(log[curr]["algorithms"]))
