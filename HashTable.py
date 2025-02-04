from collections import Counter, defaultdict


class HashTable:
    def __init__(self, length=5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

    def set(self, key, value):
        index = hash(key) % self.max_len
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.max_len
        value = self.table[index]
        if not value:
            return None
        for i in value:
            if i[0] == key:
                return i[1]
        return None


def first_unique_char(s: str) -> int:
    n: int = len(s)
    check: list[int] = [0] * n
    for i, ch in enumerate(s):
        if check[i]:
            continue
        check[i] = 1
        is_unipue = True
        for j in range(i + 1, n):
            if ch == s[j]:
                check[j] = 1
                is_unipue = False
                break
        if is_unipue:
            return i
    return -1


def first_unique_char_dic(s: str) -> int:
    count: dict[str, int] = {}
    for ch in s:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


def first_unique_char_dic2(s: str) -> int:
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


def maxLen(arr: list[int]) -> int:
    n: int = len(arr)
    answer: int = 0
    for i in range(n):
        total: int = 0
        left: int = 1
        right: int = 1
        for j in range(i, n):
            total += arr[j]
            if total == 0:
                right = j
                answer = max(answer, right - left + 1)
    return answer


def maxLen_dic(arr: list[int]) -> int:
    total: int = 0
    dic: dict[int, list[int]] = defaultdict(list)
    dic[0] = [-1]
    for i in range(len(arr)):
        total += arr[i]
        dic[total].append(i)
    ans = 0
    for a in dic.values():
        ans = max(ans, a[-1] - a[0])
    # print(dic)
    return ans


def maxLen_dic2(arr: list[int]) -> int:
    dic: dict[int, int] = {0: -1}
    ans: int = 0
    total: int = 0
    for i in range(len(arr)):
        total += arr[i]
        if total in dic:
            ans = max(ans, i - dic[total])
        else:
            dic[total] = i
    # print(dic)
    return ans


def solution(n: int, words: list[str]) -> list[int]:
    check: set[str] = set()
    tail: str = words[0][0]
    for i, word in enumerate(words):
        if word in check or tail != word[0]:
            return [i % n + 1, i // n + 1]
        check.add(word)
        tail = word[-1]
    return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

"""A = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxLen_dic2(A))


for s in ("leetcode", "loveleetcode", "aabb"):
    print(first_unique_char_dic(s))

if __name__ == "__main__":
    capital = HashTable()
    country = ["Korea", "America", "China", "England", "Türkiye"]
    city = ["Seoul", "Washington", "Beijing", "London", "Ankara"]
    for co, ci in zip(country, city):
        capital.set(co, ci)

    print("해시 테이블의 상태")
    print("===============")
    for i, v in enumerate(capital.table):
        print(i, v)
    print()
    print("해시 테이블의 검색 결과")
    print("====================")
    print(f"Captial of America = {capital.get('America')}")
    print(f"Captial of Korea = {capital.get('Korea')}")
    print(f"Captial of England = {capital.get('England')}")
    print(f"Captial of China = {capital.get('China')}")
    print(f"Captial of Japan = {capital.get('Japan')}")
    print(f"Captial of Türkiye = {capital.get('Türkiye')}")
"""
