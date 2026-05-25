class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm: dict = {}
        for i in strs:
            sortedi = "".join(sorted(i))
            if sortedi not in hashm:
                hashm[sortedi]=[i]
            else:
                hashm[sortedi].append(i)
        return list(hashm.values())