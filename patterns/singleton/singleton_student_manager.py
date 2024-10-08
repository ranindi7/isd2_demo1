class SingletonStudentManager:
    __instance = None
    __next_student_number = 20240000

    def __new__(cls):
        """
        Constructs the SingletonStudentManagaer instance but 
        only if it does not already exist in memory
        """
        # if there is no instance of this class in memory:
        if not cls.__instance:
            # create the instance
            cls.__instance = super(SingletonStudentManager, cls).__new__(cls)
        # return the instance that was in memory
        # or if there wasn't one in memory, return the
        # instance that was just created
        return cls.__instance
    
    def get_next_student_number(cls) -> int:

        student_number = cls.__next_student_number
        cls.__next_student_number += 1
        return student_number