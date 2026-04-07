class Solution:
    def groupAnagrams(self, strs):
        storage = {}
        for item in strs:
            key = "".join(sorted(item))                    # compute the grouping key
            if key not in storage:
                storage[key] = []
            storage[key].append(item)   # add to that group
        return list(storage.values())         