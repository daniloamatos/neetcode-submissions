class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        lista = []

        for i, n in enumerate(strs):
            key = str(sorted(n))

            if key in dic:
                lista[dic[key]].append(n)
            else:
                lista.append([n])
                dic[key] = len(lista) - 1
        return(lista)