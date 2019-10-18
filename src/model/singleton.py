class Singleton:
    __instance = None
    project = ""
    @staticmethod
    def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
    @staticmethod
    def getProject():
        return Singleton.project
    @staticmethod
    def setProject(project):
        Singleton.project = project
    def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
