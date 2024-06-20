import class_models as cm

def test_function(c):
    result = c + c
    print(result)
    #return result

def class_start():
    entry = input("Enter Agency name: ")
    x = cm.Agency(entry)
    
    print(x)