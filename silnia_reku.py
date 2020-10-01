def funkcja_silni(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * funkcja_silni(n - 1)
    
print(funkcja_silni(5))
