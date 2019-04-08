actualReturnDate = input()
expectedReturnDate = input()

actualReturnDay = int(actualReturnDate.split(" ")[0])
actualReturnMonth = int(actualReturnDate.split(" ")[1])
actualReturnYear = int(actualReturnDate.split(" ")[2])

expectedReturnDay = int(expectedReturnDate.split(" ")[0])
expectedReturnMonth = int(expectedReturnDate.split(" ")[1])
expectedReturnYear = int(expectedReturnDate.split(" ")[2])

if actualReturnYear > expectedReturnYear:
    print("10000")

if actualReturnMonth > expectedReturnMonth:
    if actualReturnYear == expectedReturnYear:
        print("{}".format(500 * (actualReturnMonth - expectedReturnMonth)))

if actualReturnDay > expectedReturnDay:
    if actualReturnMonth == expectedReturnMonth:
        if actualReturnYear == expectedReturnYear:
            print("{}".format(15 * (actualReturnDay - expectedReturnDay)))

if actualReturnYear < expectedReturnYear:
    print("0")

if actualReturnYear == expectedReturnYear:
    if actualReturnMonth < expectedReturnMonth:
        print("0")

if actualReturnYear == expectedReturnYear:
    if actualReturnMonth == expectedReturnMonth:
        if actualReturnDay < expectedReturnDay:
            print("0")
