
class Permutation:
    def __init__(self, list: list[int]):
        self.list = list
    
    def __str__(self):
        res = "\n idx: "
        for idx, val in enumerate(self.list):
            res += f"{idx+1:2d} "
        res += "\n val: "
        for val in self.list:
            res += f"{val:2d} "
        return res
    
    def invert(self):
        res = [0] * len(self.list)
        for idx, val in enumerate(self.list):
            res[val-1] = idx+1
        return Permutation(res)
    
    def getInversions(self):
        """
        Efficeintly compute the number of inversions in a permutation by doing a merge sort
        """
        def mergeSort(arr: list[int]) -> int:
            if len(arr) == 1:
                return 0
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            inversions = mergeSort(left) + mergeSort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    inversions += len(left) - i
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            return inversions

        return mergeSort(self.list[:])
    
    def minSwaps(self):
        """
        Compute the minimum number of swaps needed to sort the permutation
        """
        
        def dfs(idx: int, visited: list[bool], graph: list[int]) -> int:
            visited[idx] = True
            res = 0
            neighbor = graph[idx]
            if not visited[neighbor]:
                res += dfs(neighbor, visited, graph)
            return res + 1

        n = len(self.list)
        graph: list[int] = [-1] * n
        for idx, val in enumerate(self.list):
            graph[idx] = val-1
        visited = [False] * n
        res = 0
        for idx in range(n):
            if not visited[idx]:
                res += dfs(idx, visited, graph) - 1
        return res
    
    def getSign(self):
        """
        Compute the sign of a permutation
        """

        inversions = self.getInversions()
        return (-1)**inversions


def main():
    p = [2, 3, 5, 4, 1]
    perm = Permutation(p)
    permInv = perm.invert()
    print(f"permutation and its inverse: {perm}\n {permInv}")
    print(f"number of inversions in the permutation: {perm.getInversions()}")
    print(f"number of inversions in the inverse permutation: {permInv.getInversions()}")
    print(f"sign of permutation: {perm.getSign()}")
    print(f"sign of inverse permutation: {permInv.getSign()}")
    print(f"minimum number of swaps to sort the permutation: {perm.minSwaps()}")
    print(f"minimum number of swaps to sort the inverse permutation: {permInv.minSwaps()}")

if __name__ == "__main__":
    main()
