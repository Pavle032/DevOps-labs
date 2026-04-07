def func1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
res1 = func1(999)
res2 = func1(1000)
print(f"999! : {res1}")
print(f"1000! : {res2}")
print(f"First compare: {res1 == res2}")
print(f"The 1000! is bigger then 999! by: {res2 - res1}")
RES1 = res2 - res1
Res1 = str(RES1)
print(f"And there is {len(Res1)} numbers in that number")
print