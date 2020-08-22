import Modules.demo as md

def func1():
    print("Special Variable "+__name__)
    print("Inside main module's function")

func1()
md.main()
md.func1()