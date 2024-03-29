def solution(sticker):
    sticker_cnt = len(sticker)

    if sticker_cnt == 1:
        return sticker[0]

    dp1 = [0] * sticker_cnt
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, sticker_cnt - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2 = [0] * sticker_cnt
    dp2[1] = sticker[1]
    for i in range(2, sticker_cnt):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(max(dp1), max(dp2))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))