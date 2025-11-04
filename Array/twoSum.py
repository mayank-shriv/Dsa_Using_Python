class TwoSum:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def brute_force(self) -> list[int] | None:
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
        return None

    def hashmap(self) -> list[int] | None:
        seen = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None


if __name__ == "__main__":
    nums = [12, 22, 3, 2223, 1, 223, 443, 2]
    target = 5

    solver = TwoSum(nums, target)
    print("brute_force ->", solver.brute_force())
    print("hashmap     ->", solver.hashmap())