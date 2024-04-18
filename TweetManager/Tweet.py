import time

class Tweets:
     def __init__(self, author, text):
          self.author = author
          self.text = text
          self.age = time.time()

     def getauthor(self):
          return self.author

     def gettext(self):
          return self.text

     def getage(self):
          elapsed = time.time()-self.age
          if elapsed < 60:
               return str(int(elapsed))+'s'
          elif elapsed/60 < 60:
               return str(int(elapsed/60))+'m'
          else:
               return str(int(elapsed/3600))+'h'
