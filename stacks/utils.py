from typing import Any, Mapping, Sequence

import yaml


def load_stack_config(base_dir: str, names: Sequence[str]) -> Mapping[str, Any]:
    parameters = {}
    for name in names:
        path = f"{base_dir}/{name}.yml"
        with open(path, "r") as f:
            contents = yaml.safe_load(f)
            parameters[name] = contents

    return parameters
