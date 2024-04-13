import os, sys 
os.system("git pull")
try:
    _import_("MAINKISS").Main() 
except Exception as e: 
    exit(str(e)
