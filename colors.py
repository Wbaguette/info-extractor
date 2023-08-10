RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def print_warning(msg: str):
   print(RED + "\nERROR: " + msg + RESET)
      
def print_success(msg: str, newlined: bool):
   if newlined:
      print(GREEN + "\nSUCCESS: " + msg + RESET)
   else: 
      print(GREEN + "SUCCESS: " + msg + RESET)

def choice(msg: str) -> str:
   choice = input(MAGENTA +  "\n" + msg + RESET)
   return choice

def full_text_print(text: str):
   print("\n" + YELLOW + text + RESET)