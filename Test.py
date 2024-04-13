import os, sys 
os.system("git pull")
try:
    _import_("Autopass").Main() 
except Exception as e: 
  exit(str(e))
