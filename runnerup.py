a = input("masukan angka dengan separator spasi : ")


def runnerup(_list):
    b = _list.split(" ")
    highest = int(b[0])
    secondary = int(b[0])
    for i in range(len(b)):
        if int(b[i]) > highest:
            highest = int(b[i])

    for i in range(len(b)):
        if int(b[i]) > secondary and int(b[i]) != highest:
            secondary = int(b[i])
    print ("runnerup is : ",secondary)


runnerup(a)