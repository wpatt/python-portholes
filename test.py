

from pathlib import Path

f = Path(__file__).parent.joinpath('corpus/raw/registerofletter00eastuoft_djvu.txt').open()

for i in range(10):
    print(f.readline())


# thomasmiddleton's comment
