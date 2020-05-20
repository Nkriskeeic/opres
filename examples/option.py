import sys
sys.path.append('../opres')  # bad practice. forgive me

from typing import Any, Dict

from opres import Option, Some, Nothing


class DummyDatabase:
    def __init__(self):
        self._storage: Dict[str, Any] = {}

    def insert(self, key: str, value: Any):
        # destructive Wow!
        self._storage[key] = value

    def find(self, key: str) -> Option[Any]:
        if key in self._storage:
            return Some(self._storage[key])
        else:
            return Nothing()


def run():
    db = DummyDatabase()
    db.insert('key1', 'value1')
    db.insert('key2', [10, 20, 30])

    data = db.find('key1')
    print(f"key1: data.unwrap={data.unwrap()}")

    data = db.find('key2')
    print(f"key2: length of data={data.map(len)}")

    data = db.find('key3')
    if data.is_nothing():
        print(f"key3: data is nothing")

    data = db.find('key3').map(len)
    if data.is_nothing():
        print(f"key3: length of data is nothing")

    print(f"key3: length of data is {db.find('key3').map_or(len, 0)}")


if __name__ == '__main__':
    run()
