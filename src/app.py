import sys
from pathlib import Path
import json
from test_util.state_calc import StateCalc

if(len(sys.argv)!=2):
    print("No conf file name applied! Program will exit!")
    sys.exit()

filename=sys.argv[1]

path=Path(F"{filename}")

if(not path.exists()):
    print(F"path does not exist on {path.absolute()}")
    sys.exit()

conf=json.loads(path.read_text())

stateCalc=StateCalc(conf)
stateCalc.open_menu()


