def check():
    hang = [0]*5
    cot = [0]*5
    cheo_thuan = 0
    cheo_nguoc = 0
    cnt = 0
    for k in range(25):
        # convert to interger
        i, j = map(int, input().split())
        hang[i] += 1
        cot[j] += 1
        if i == j:
            cheo_thuan += 1
        if i+j == 4:
            cheo_nguoc += 1
        if hang[i] == 5:
            hang[i] += 1
            cnt += 1
        if cot[i] == 5:
            cot[i] += 1
            cnt += 1
        if cheo_thuan == 5:
            cheo_thuan += 1
            cnt += 1
        if cheo_nguoc == 5:
            cheo_nguoc += 1
            cnt += 1
        print(cnt)
