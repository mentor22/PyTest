def func1():
    print("Welcome to "+__name__)
    print("Hello User inside demo modules function")  

def main():
    if __name__ == "__main__":#will call main function only when this is the first module to run(point of execution starts) 
        func1()

main()