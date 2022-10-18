def ca_cows():
    cow = int(input())
    if 11 <= cow % 100 <= 14:
        return f"на поле {cow} коров"
    else:
        n = cow % 10
        if n == 1:
            return f"на поле {cow} корова"
        elif 2 <= n <= 4:
            return f"на поле {cow} коровы"
        else:
            return f"на поле {cow} коров"


print("Hello")