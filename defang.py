import subprocess
import sys

def return_defanged(fanged_str:str, protocol_defang = False) -> str:
   defanged_str = ""
   if protocol_defang:
      if "http" in fanged_str and fanged_str.find("http") == 0:
         fanged_str = fanged_str.replace("http","hXXp",1)

      if "ftp" in fanged_str and  fanged_str.find("ftp") == 0:
         fanged_str = fanged_str.replace("ftp","fXp",1)

   # check if url has been defanged already
   if "[.]" in fanged_str:
      print("URL seems to be defanged already...")
   
   for i in range(len(fanged_str)):
      if fanged_str[i] == "." and fanged_str[i-1] != "[" and fanged_str[i+1] != "]":
         defanged_str += "[.]"
      else:
         defanged_str += fanged_str[i]
   
   return defanged_str

fanged_str = input("Enter URL or IP Address, enter 'multiple' if multiple:\n")

defang_protocol_too = False
try:
   if sys.argv[1] == "--defang_protocol":
      defang_protocol_too = True
except:
   pass


if fanged_str == "multiple":
   fanged_ar = []
   print("Paste multiple, separated by a newline character, Ctrl+D or blank line to save:")
   
   # take in multiple lines of input
   while True:
      try:
         line = input()
      except EOFError:
         break
      if not line.replace(" ",""):
         break
      # append line after each \n
      fanged_ar.append(line)

   print("\n")
   defanged_str = ""
   for fang in fanged_ar:
      # for each url / ip in fanged_ar, defang each, print them out, and add to defanged_str
      # (w/ a newline between each ip / url)
      cur_defanged = return_defanged(fang, defang_protocol_too)
      print(cur_defanged)
      defanged_str += cur_defanged + "\n"
   print()
   
   # copy to clipboard
   subprocess.run("pbcopy", text=True, input=defanged_str)
   print("Copied to Clipboard!")

else:
   # defang string
   defanged_str = return_defanged(fanged_str, defang_protocol_too)

   # print defanged
   print(f'\n{defanged_str}\n')

   # copy to clipboard
   subprocess.run("pbcopy", text=True, input=defanged_str)
   print("Copied to Clipboard!")


