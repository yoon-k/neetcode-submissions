class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for a in s:
            s_dict[a] = s_dict[a] + 1 if a in s_dict else 1
        for b in t:
            t_dict[b] = t_dict[b] + 1 if b in t_dict else 1
        return s_dict == t_dict