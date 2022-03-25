from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        data = csv.DictReader(file)
        return list(data)


# Foram utilizado as seguintes fontes para compreender
# como converter o arquivo csv em um dicionario
# https://python-forum.io/thread-9859.html
# https://www.youtube.com/watch?v=5CEsJkKhS78&ab_channel=KrisJordan
