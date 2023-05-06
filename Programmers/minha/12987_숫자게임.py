def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    answer = 0
    b_idx = 0

    for a in A:
        if a < B[b_idx]:
            answer += 1
            b_idx += 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))