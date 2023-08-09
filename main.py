import sys
import file_handler
import colors
import response_handler

from ai import auth
from ai import requests
from parser import parser

# PLAN OF ATTACK : 
# [✓] Properly pass in file paths via CLI and check if they are valid to info extract  
# [✓] Check if the file is parseable => is it corrupt or empty?   
# [✓] If they are valid, do OpenAI auth 
# [✓] Send request 
# [✓] How should the response be formatted? => Saved to the same directory as the original file path or just printed out?

# Future: GUI to make it not so insanely hard to pass files

def main():
   args: [str] = sys.argv
   validate_args_len(args)                                    # Can only have 1 file passed in
      
   file_path: str = args[1]
   file_handler.validate_path_exists(file_path)               # Verify the path even exists
   file_type = file_handler.validate_file_type(file_path)     # Verify the file type of the path is supported for info extracting
   
   parsed_file_content = parser.parse(file_path)
   auth.auth()
   
   response = requests.send(parsed_file_content, file_type)
   response_handler.get_user_choice(response, file_path)
   
def validate_args_len(args: [str]):
   if len(args) > 2:
      colors.print_warning("Please only pass in 1 file path to have info extracted. In the future multiple file paths will be supported.")
      sys.exit()
      
   if len(args) == 1:
      colors.print_warning("Whoops. You forgot to pass the file path.")
      sys.exit()
      
if __name__ == "__main__":
   main()