class vscode:
    def execute(self):
        print("Compiling")
        print("Running")

class Myeditor:
    def execute(self): #duck typed function
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute() #duck typed as ide needs only be object of a class having function called execute

ide = vscode()
lap = Laptop()
lap.code(ide)

ide = Myeditor()
lap.code(ide) #duck typed