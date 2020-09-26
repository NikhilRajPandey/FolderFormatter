import os

class Formater:
   @staticmethod
   def isInlist(param_list,item):
      # Checking from last for no reason
      for curr_item in param_list[::-1]:
         if curr_item == item: return True
      return False

   @staticmethod
   def arrange_files():
      formats_ = [] # This will contain those files whose format folder is maded
      all_files = os.listdir()

      for file in all_files:
         if os.path.isfile(file):
            seprated_file = file.split('.')

            if len(seprated_file) == 1: extension = 'NoExtension'
            else: extension = seprated_file[1]

            if(not Formater.isInlist(formats_,file)): os.system(f"mkdir {extension}")
            os.system(f"mv {file} {extension}/")
   
if __name__ == "__main__":
    Formater.arrange_files()
