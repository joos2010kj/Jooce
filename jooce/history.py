from pathlib import Path
import json

def history(op="r", content=None):
    if not (Path(__file__).parent / "history.json").exists():
        with (Path(__file__).parent / "history.json").open("w") as f:
            f.writelines("{}")

    with (Path(__file__).parent / "history.json").open(op) as f:
        if op == "r":
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {"__SELECT__": None}

            return data
        elif op == "w":
            json.dump(content, f, indent=4, sort_keys=True)

    return None
