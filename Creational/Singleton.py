class Singleton:

    __global_pointer = None

    @staticmethod
    def get_instance():
        if Singleton.__global_pointer is None:
            Singleton()
        return Singleton.__global_pointer

    def __init__(self):

        if Singleton.__global_pointer is None:
            Singleton.__global_pointer = self
        else:
            raise Exception("Unable to Create Multiple instances of Singleton")


if __name__ == '__main__':
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    print("Are both instances the same? ", s1 == s2)

    print("Trying to create a new instance of singleton class")
    s3 = Singleton()
    print(s3)
