import sys
import os
import colors

allowed_files: [str] = [".pptx", ".ppt", ".pdf"]

def validate_path_exists(path: str):
   if not os.path.exists(path):
      colors.print_warning(path + " does not exist. Please double check the path you provided is a real file.")
      sys.exit()

def validate_file_type(path: str) -> str:
   _, file_passed_type = os.path.splitext(path)
   if not file_passed_type:
      colors.print_warning(path + " is not a file. Its possible you passed a folder or directory and not a file.")
      sys.exit()
   else:
      if not file_passed_type in allowed_files:
         colors.print_warning(file_passed_type + " is not supported for parsing. Supported file types: " + ", ".join(allowed_files))
         sys.exit()
      colors.print_success("Preliminary checks passed for: " + path, True)
      return file_passed_type