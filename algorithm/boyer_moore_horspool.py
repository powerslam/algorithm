from collections import defaultdict

pattern = 'tiger'
t = 'asdkftwoefiqtoiojlkandbnqettigerakdfjjaogeifitqoqkakdjnvrtigerjqofiqowfiorqijowafijgooiqfeoiqoirjfoiqfjoiiog'

# jump table 만들기
def make_jump_table(pattern):
    # default dict를 통해 pattern 내에 존재하지 않는 값에 대응
    jump_table = defaultdict(lambda: len(pattern))
    
    # 마지막 원소 제외하고 skip 할 값 할당하기
    for i in range(len(pattern) - 1):
        # 값이 더 작은 것을 할당시키기 위해서
        # 별도의 조치 없이 값을 할당함
        jump_table[pattern[i]] = len(pattern) - i - 1
    
    return jump_table

def boyer_moore_horspool(t, pattern, jump_table):
    ret = []
    i, t_len, p_len = 0, len(t), len(pattern)

    # 비교문자열 t에서 pattern 문자열의 길이만큼 빠지고, 거기에 1을 더하면 가능한 마지막 패턴 비교가 되니까
    # i = t_len - p_len 까지만 가능
    # @@@ 헷갈리면 직접 적어서 생각해보기 @@@
    while i < t_len - p_len + 1:
        j = p_len - 1
        while j >= 0:
            if t[i + j] != pattern[j]:
                break

            j -= 1

        # 끝까지 매칭이 잘 된 경우
        else:
            ret.append(i)

        # 만약에 마지막 문자가 중간에도 있다면 거기부터 탐색을 시작할 것이고
        # 그렇지 않으면 pattern 길이 만큼 skip 할 거임
        # 구현 방식에 따라서 겹치는 문자열도 찾을 수 있고, 아닐 수도 있음
        # 만약에 else 문에 i += len(pattern) 해놓고 continue 문을 추가했다면
        # 겹치는 부분에 대해서는 skip을 할 거임
        i += jump_table[t[i + p_len - 1]]

    return ret

jump_table = make_jump_table(pattern)
print(boyer_moore_horspool(t, pattern, jump_table))
