class Singleton:
    __instance = None
    project = ""
    filepath = ""

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    @staticmethod
    def get_project():
        return Singleton.project

    @staticmethod
    def set_project(project):
        Singleton.project = project

    @staticmethod
    def get_path():
        return Singleton.filepath

    @staticmethod
    def set_path(path):
        Singleton.filepath = path

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
