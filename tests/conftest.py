import sys
from pathlib import Path

# The template extensions are loaded by copier from a path, they are not an installed package
sys.path.insert(0, str(Path(__file__).parents[1] / "extensions"))
