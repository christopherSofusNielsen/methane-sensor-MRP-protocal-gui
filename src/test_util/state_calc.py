import json
import math

from test_util.header_calc import HeaderCalc

COLLECTION_META_DATA_LEN = 6


class StateCalc:
    def __init__(self, collections) -> None:
        self.collections = collections

    def open_menu(self):
        print("[1] print collections")
        print("[2] print initialized state")
        print("[3] print header test array")
        choice = input("Select 1 og 2: ")
        if(choice == "1"):
            self.print_collections()
        elif(choice == "2"):
            self.state = create_state_init(self.collections)
            self.print_state()
        elif(choice == "3"):
            self.state = create_state_init(self.collections)
            headerCalc = HeaderCalc(self.state)
            self.headerList = headerCalc.getHeaderList()
            print(self.headerList)
        else:
            print("Not a choice, try again")
            self.open_menu()

    def print_collections(self):
        print(json.dumps(self.collections, indent=4, sort_keys=True))

    def print_state(self):
        if(not hasattr(self, "state")):
            print("Not possible")
        else:
            print(json.dumps(self.state, indent=4, sort_keys=True))


def create_state_init(collections):
    state = {}
    state["groupId"] = "unknown"
    state["nCollections"] = len(collections)

    # calc last subId
    totBytes = sum(c["samplings"]*c["type"] +
                   COLLECTION_META_DATA_LEN for c in collections)
    state["lastSubId"] = math.floor(totBytes/48)+2
    if(totBytes % 48 == 0):
        state["lastSubId"] -= 1

    # calc nBodies
    state["nBodies"] = math.ceil(totBytes/48)

    # add bodies
    state["bodies"] = ["WAITING"]*state["nBodies"]

    # add collection
    _cols = []

    startIndex = 0
    for col in collections:
        c = {}
        c["type"] = col["type"]
        c["startIndex"] = startIndex
        c["length"] = col["samplings"]*col["type"]+COLLECTION_META_DATA_LEN
        c["beginsInBody"] = math.floor(c["startIndex"]/48)
        c["endsInBody"] = math.floor((c["startIndex"]+c["length"])/48)
        if((c["startIndex"]+c["length"]) % 48 == 0):
            c["endsInBody"] -= 1

        startIndex += c["length"]
        _cols.append(c)

    state["collections"] = _cols

    return state
