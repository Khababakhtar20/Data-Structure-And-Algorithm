class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] = freq[i] + 1
            else:
                freq[i] = 1

        max_freq = 0
        for key in freq:
            if freq[key] > max_freq:
                max_freq = freq[key]

        buckets = [[] for _ in range(max_freq + 1)]

        for key in freq:
            count = freq[key]
            buckets[count].append(key)

        result = ''
        for i in range(max_freq, 0, -1):
            for char in buckets[i]:
                result += char * i

        return result
