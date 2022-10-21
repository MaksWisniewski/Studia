class Student:
    def __init__(self):
        self.private_info = ""

    def log_internal_operations(self, function_name):
        print(f"{function_name} is processing private info!")

    def get_private_info(self):
        self.log_internal_operations("get_private_info")
        return self.private_info

    def set_private_info(self, info):
        self.log_internal_operations("set_private_info")
        self.private_info = info


# How should we change the getter/setter to be more Pythonic, but still call the important internal function?
frank = Student()
frank.set_private_info("Frank Sinatra")
print(frank.get_private_info())
