class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, A, N, X):
        # Your code here
        low = 0
        high = N - 1
        floor = -1
        while low <= high:
            middle = (low + high) // 2
            if A[middle] <= X:
                floor = middle
                low = middle + 1
            elif A[middle] > X:
                high = middle - 1
        return floor


a = Solution()
print(
    a.findFloor(
        [
            66,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            89,
            90,
            91,
            92,
            93,
            94,
            95,
            96,
            97,
            98,
            99,
            100,
            101,
            102,
            103,
            104,
            105,
            106,
            107,
            108,
            109,
            110,
            111,
            112,
            113,
            114,
            115,
            116,
            117,
            118,
            119,
            120,
            121,
            122,
            123,
            124,
            125,
            126,
            127,
            128,
            129,
            130,
        ],
        65,
        106,
    )
)
