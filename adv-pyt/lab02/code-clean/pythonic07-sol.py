class Student:
    def __init__(self):
        self._private_info = ""

    # Note: we want to keep this next function as is.
    @staticmethod
    def log_internal_operations(function_name):
        print(f"{function_name} is processing private info!")

    @property
    def private_info(self):
        self.log_internal_operations("get_private_info")
        return self._private_info

    @private_info.setter
    def private_info(self, info):
        self.log_internal_operations("set_private_info")
        self._private_info = info


frank = Student()
frank.private_info = "Frank Sinatra"
print(frank.private_info)
