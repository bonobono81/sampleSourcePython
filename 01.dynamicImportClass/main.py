#import importlib
#####################################################################
# Dynamic Import Sample
######################################################################

#def loadModuleFunc(moduleNm):
#    selClass = importlib.import_module(moduleNm)
#    return selClass

def loadModuleFunc2(moduleNm):
    selClass = __import__('%s'%(moduleNm),fromlist=[moduleNm])
    return selClass
    
# Main함수
if __name__ == '__main__':
    print("MAIN.START")
    myClass = getattr(loadModuleFunc2("TestClass"), "TestClass")
    print(myClass)
    mainVal01 = myClass.print01()
    print("mainVal01: ", mainVal01)
    mainVal02 = myClass.print02()
    print("mainVal02: ", mainVal02)
    print("MAIN.END")
