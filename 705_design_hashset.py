"""Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""


class MyHashSet:

    idx = 0

    def __init__(self):
        pass

    def add(self, key: int) -> None:
        setattr(self, str(key), self.idx)
        self.idx += 1

    def remove(self, key: int) -> None:
        if hasattr(self, str(key)):
            delattr(self, str(key))

    def contains(self, key: int) -> bool:
        if hasattr(self, str(key)):
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


if __name__ == '__main__':

    obj = MyHashSet()
    obj.add(1)
    obj.add(3)
    obj.add(2)

    obj.remove(3)
    print(obj.contains(1))
    print('done')
