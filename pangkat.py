def pangkat(a,b):
    d = 0
    e = 1
    for i in range(0, b):
        d = a * e
        e = d
    result = "{a1} pangkat {b1} = {d1}".format(a1 = a, b1 = b, d1 = d)
    print(result)
    # print("{a1} pangkat {b1} = ", d)
    

bil1 = int(input("masukan bilangan: "))
bil2 = int(input("masukan pangkat: "))
pangkat(bil1,bil2)