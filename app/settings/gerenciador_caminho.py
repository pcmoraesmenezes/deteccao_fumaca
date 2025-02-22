from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class GerenciadorCaminho:
    ROOT : Path = Path.cwd()
    MODEL_PATH : Path = ROOT / 'best.pt'

