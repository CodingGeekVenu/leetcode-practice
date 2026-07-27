class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict ={}

        for words in strs:
            key = "".join(sorted(words))

            if key in final_dict:
                final_dict[key].append(words)
            else:
                final_dict[key] =[]
                final_dict[key].append(words)
        
        return list(final_dict.values())

        
        
            

        
