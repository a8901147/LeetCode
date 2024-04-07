class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []

        for c in order:
            if c in counter:
                res.extend([c]*counter[c])
                del counter[c]

        for c in counter:
            res.extend([c]*counter[c])

        return "".join(res)
            