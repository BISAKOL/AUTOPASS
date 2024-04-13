import os, sys 
os.system("git pull")
try:
    _import_("KISS").Subscraption() 
except Exception as e: 
  exit(str(e))
