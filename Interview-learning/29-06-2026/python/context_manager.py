class ContextMananger:

    def __enter__(self):
        print("Entering")
    def  __exit__(self,exc_val,exc_tb,traceback):
        print("Exiting")


with ContextMananger():
    print("Inside block")