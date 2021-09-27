

class HeaderCalc:
    def __init__(self, initState) -> None:
        self.initState = initState

    def getHeaderList(self):
        self.header = []

        # subId
        self.header.append(hex(0))

        # last subId
        self.header.append(hex(self.initState["lastSubId"]))

        # Status Bit
        self.header.append(hex(0))

        # DataTypes
        bytes = self.getDataTypes(self.initState["collections"])
        for b in bytes:
            self.header.append(hex(b))

        # Collections
        for col in self.initState["collections"]:
            self.header.append(hex((col["startIndex"] >> 8) & 255))
            self.header.append(hex(col["startIndex"] & 255))
            self.header.append(hex((col["length"] >> 8) & 255))
            self.header.append(hex(col["length"] & 255))

        return self.formatHeader()

    def getDataTypes(self, collections):
        dt = 0
        cnt = 0
        for cl in collections:
            if(cl["type"] == 1):
                dt |= 1 << cnt
            elif(cl["type"] == 2):
                dt |= 2 << cnt
            elif(cl["type"] == 4):
                dt |= 3 << cnt
            else:
                raise Exception("Type not valid")
            cnt += 2

        bytes = []
        bytes.append((dt >> 16) & 255)
        bytes.append((dt >> 8) & 255)
        bytes.append((dt) & 255)
        return bytes

    def formatHeader(self):
        headerStr = ""
        headerStr += "\n"
        headerStr += self.header[0]

        for el in self.header:
            headerStr += ", "+el
        return headerStr
