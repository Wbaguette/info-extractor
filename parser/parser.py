from tika import parser
import re
import colors
import sys

def parse(path: str) -> str:
   parsed = parser.from_file(path)
   raw_content: str = parsed["content"]
   
   cleaned_content: str = re.sub(r'\n{4,}', '\n', raw_content).strip()
   if len(cleaned_content) == 0:
      colors.print_warning("The parsed file has no content.")
      sys.exit()
      
   colors.print_success("Successfully parsed your file and retrieved content.", False)   
   return cleaned_content
   