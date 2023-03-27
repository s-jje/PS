from typing import List
import re


def solution(files: List[str]) -> List[str]:
    files.sort(key=lambda f: int(re.split('(\d+)', f, maxsplit=1)[1]))
    files.sort(key=lambda f: re.split('(\d+)', f, maxsplit=1)[0].lower())
    return files
