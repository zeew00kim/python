import sys

intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

if __name__ == "__main__" :
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print(f"default size of int : {sys.getsizeof(intVar)}")
    print(f"default size of float : {sys.getsizeof(floatVar)}")
    print(f"default size of bool : {sys.getsizeof(boolVar)}")
    print(f"default size of str : {sys.getsizeof(strVar)}")
    print(f"default size of list : {sys.getsizeof(listVar)}")
    print(f"default size of tuple : {sys.getsizeof(tupleVar)}")
    print(f"default size of dictionary : {sys.getsizeof(dictVar)}")
    print(f"default size of set : {sys.getsizeof(setVar)}")