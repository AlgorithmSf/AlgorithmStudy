def solution(n, stations, w):
    answer = 0

    blanks = []

    blanks.append(stations[0] - w - 1)
    blanks.append(n - (stations[-1] + w))

    for i in range(1, len(stations)):
        blanks.append((stations[i] - w - 1) - (stations[i - 1] + w + 1) + 1)

    spread = 2 * w + 1
    for blank in blanks:
        if blank > 0:
            if blank % spread == 0:
                answer += (blank // spread)
            else:
                answer += (blank // spread + 1)

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))