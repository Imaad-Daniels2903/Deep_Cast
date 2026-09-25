import sys
from pathlib import Path
current_file = Path(__file__).resolve()
project_root = current_file.parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
import setup_wizard
import os
from deep_cast.ui import cli


def cli_entry() :
    if not os.path.isfile(".env") :
        setup_wizard.main()
        
    t = cli.terminal()
    t.start()
    
    
if __name__ == "__main__" : 
    cli_entry()