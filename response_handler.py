import colors
import os
import textwrap

def get_user_choice(response: str, path: str):
   while True:
      choice = colors.choice("""How would you like the response formatted?
Press [P] to have it printed out here.
Press [S] to save it as raw text in the same directory as the initial file.\n
      """).lower()
      
      if choice == "p":
         handle_print_res(response)
         break
      elif choice == "s":
         handle_save_res(response, path)
         break
      else:
         colors.print_warning("Invalid choice. Try again.")
         
def handle_print_res(response: str):
   colors.full_text_print(response)
   
def handle_save_res(response: str, path: str):
   directory = os.path.dirname(path)
   base_filename, _ = os.path.splitext(os.path.basename(path))
   new_filename = f"{base_filename}_output.txt"
   new_filepath = os.path.join(directory, new_filename) 
   
   lines = response.splitlines()
   wrapped_lines = []
   
   for line in lines:
      wrapped_line = textwrap.fill(line, 100)
      wrapped_lines.append(wrapped_line)
      
   with open(new_filepath, "w") as f:
      f.write("\n".join(wrapped_lines))
              
   colors.print_success(f"Saved response to: {new_filepath}", True)