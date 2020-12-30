
from pathlib import Path



class CfgPath:

    def __init__(self, cfg_path: str) -> None:
        self.path = Path(cfg_path)

        if not self.path.exists:
            raise FileNotFoundError(self.get_path())


    def get_path(self) -> str:
        return self.path.resolve()
