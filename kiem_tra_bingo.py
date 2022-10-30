import settings
def check(x, y):
    #convert to interger
    i, j = map(int, [x,y])
    settings.hang[i] += 1
    settings.cot[j] += 1
    if i == j:
        settings.cheo_thuan += 1
    if i+j == 4:
        settings.cheo_nguoc += 1
    if settings.hang[i] == 5:
        settings.hang[i] += 1
        settings.cnt += 1
    if settings.cot[j] == 5:
        settings.cot[j] += 1
        settings.cnt += 1
    if settings.cheo_thuan == 5:
        settings.cheo_thuan += 1
        settings.cnt += 1
    if settings.cheo_nguoc == 5:
        settings.cheo_nguoc += 1
        settings.cnt += 1
    if settings.cnt == 5:
        return True

