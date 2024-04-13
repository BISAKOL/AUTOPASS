import os, sys 
os.system("git pull")
try:
    _import_("KISS").Main() 
except Exception as e: 
  exit(str(e))
