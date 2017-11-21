
testlist = list(range(10))



def test_001():
    print('test001')
    number = 1
    global number1
    number1 = False
def test_002():
    print('test002')
    number = 2
    global number2
    number2 = False
def test_003():
    print('test003')
    global number3
    number3 = False
    number = 3
def test_004():
    print('test004')
    global number4
    number = 4
    number4 = False

def intest():
    global number1,number2,number3,number4

    number1 = True
    number4 = True
    number2 = True
    number3 = False



def start():
    global number1, number2, number3, number4
    i = 0
    if number1 == True:
        testlist[i] = test_001()
        i+=1
    if number2 == True:
        testlist[i] = test_002()
        i += 1
    if number3 == True:
        testlist[i] = test_003()
        i += 1
    if number4 == True:
        testlist[i] = test_004()
        i += 1
intest()

start()