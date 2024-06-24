import re

######## Variables #######

file = """UNA:+.? '
UNB+UNOA:3+1234567890123:14+1234567890124:14+140516:1552+MSGNR111++++++1'
UNH+1+ORDERS:D:01B:UN:EAN008'
BGM+220+DOCNR1234'
DTM+137:20140519:102'
DTM+2:20140520:102'
NAD+BY+5682357469542::9'
NAD+DP+3839204839274::9'
NAD+SU+0293083940382::9'
LIN+1++1122334455667:EN'
QTY+21:11.00:PCE'
UNS+S'
CNT+2:1'
UNT+12+1'
UNZ+1+MSGNR111'
"""


def split_unless_escaped(string, delimiter, escape):
    parts = []
    current = ""
    escaped = False
    for char in string:
        if escaped:
            current += char
            escaped = False
        elif char == escape:
            escaped = True
        elif char == delimiter:
            parts.append(current)
            current = ""
        else:
            current += char
    parts.append(current)  # Add the last part
    return parts

######## Main Metode #######


def check(_file: str):
    s_idx = 0

    ############################## HEADER ##################################
    ########### UNA:+.? '
    if _file.startswith("UNA:"):
        CT = _file[3]
        DT = _file[4]
        KT = _file[5]
        FT = _file[6]
        ST = _file[8]
        s_idx = 1
    else:
        print(f"WARNING: 'UNA' is recommended in line 1.")
        CT = ":"
        DT = "+"
        KT = "."
        FT = "?"
        ST = "'"

    _file = _file.replace("\n", "")
    # _file = _file.replace(" ", "")
    # _file = _file.replace("\t", "")

    segments = split_unless_escaped(_file, ST, FT)
    daten = [split_unless_escaped(segment, DT, FT) for segment in segments]
    composites = [[split_unless_escaped(element, CT, FT) for element in data] for data in daten]

    if s_idx >= len(segments):
        print("ERROR: FILE IS EMPTY")
        return "ERROR: FILE IS EMPTY"

    ########### UNB+UNOA:3+1234567890123:14+1234567890124:14+140516:1552+MSGNR111++++++1'
    if not segments[s_idx].startswith("UNB"):
        print("ERROR: UNB (Interchange start) is missing. Should be directly after 'UNA'.")
    else:
        UNOA = daten[s_idx][1]
        SENDER = daten[s_idx][2]
        EMPFAENGER = daten[s_idx][3]
        s_idx += 1
        if s_idx >= len(segments):
            print("ERROR: FILE IS INCOMPLETE AFTER UNA")
            return "ERROR: FILE IS INCOMPLETE AFTER UNA"

    ############################## MAIN/GROUP?
    _gcount = 0
    while not segments[s_idx].startswith("UNZ"):
        if segments[s_idx].startswith("UNG"):
            _gcount += 1
            s_idx = UNG_group_start(daten, s_idx)
        elif segments[s_idx].startswith("UNH"):
            s_idx = UNH_transaction_start(daten, s_idx)
        else:
            print(f"ERROR: In Interchange {segments[s_idx]} only 'UNG' or 'UNH' allowed in line {s_idx + 1}.")

    GCOUNT = int(daten[s_idx][1])
    GREFERENCE = daten[s_idx][2]
    if _gcount != GCOUNT - 1:
        print(f"ERROR: In line {s_idx + 1}, {GCOUNT} Groups expected but only {_gcount} Groups given!")


############################## FUNCTIONS

def UNG_group_start(daten: list, s_idx: int):
    MTYPE = daten[s_idx][1]
    VERSION = daten[s_idx][7]
    _tcount = 0

    s_idx += 1
    if s_idx >= len(daten):
        print("ERROR: FILE IS INCOMPLETE! Missing UNZ (Group end)!")
        return "ERROR: FILE IS INCOMPLETE! Missing UNZ (Group end)!"

    while not daten[s_idx][0].startswith("UNE"):
        if daten[s_idx][0].startswith("UNH"):
            _tcount += 1
            s_idx = UNH_transaction_start(daten, s_idx)
        else:
            print(f"ERROR: In line {s_idx + 1} 'UNH' expected but '{daten[s_idx][0]}' given!")

    TCOUNT = int(daten[s_idx][1])
    TREFERENCE = daten[s_idx][2]
    if _tcount != TCOUNT:
        print(f"ERROR: In line {s_idx + 1}, {TCOUNT} Transactions expected but only {_tcount} Transactions given!")

    s_idx += 1
    if s_idx >= len(daten):
        print("ERROR: FILE IS INCOMPLETE! Missing UNZ (Interchange end)!")
        return "ERROR: FILE IS INCOMPLETE! Missing UNZ (Interchange end)!"

    return s_idx


def UNH_transaction_start(daten: list, s_idx: int):
    _scount = 0

    s_idx += 1
    if s_idx >= len(daten):
        print("ERROR: FILE IS INCOMPLETE! Missing UNT (Transaction end)!")
        return "ERROR: FILE IS INCOMPLETE! Missing UNT (Transaction end)!"

    while not daten[s_idx][0].startswith("UNT"):
        transaction_details(daten[s_idx], s_idx)
        _scount += 1
        s_idx += 1
        if s_idx >= len(daten):
            print("ERROR: FILE IS INCOMPLETE! Missing UNT (Transaction end)!2")
            return "ERROR: FILE IS INCOMPLETE! Missing UNT (Transaction end)!"

    SCOUNT = int(daten[s_idx][1])
    if SCOUNT - 2 != _scount:
        print(f"ERROR: In line {s_idx + 1}, {SCOUNT} Segments expected but only {_scount} Segments given!")

    TREFERENCE = daten[s_idx][2]

    s_idx += 1
    if s_idx >= len(daten):
        print("ERROR: FILE IS INCOMPLETE! Missing UNZ (Interchange end)!2")
        return "ERROR: FILE IS INCOMPLETE! Missing UNZ (Interchange end)!"

    return s_idx


def transaction_details(daten: list, s_idx: int):
    print("Transaction data: ", daten)
    if daten[0] in ('DTM', 'NAD', 'LIN', 'QTY', 'BGM', 'UNS', 'CNT'):
        exec(daten[0]+"(daten)")
    else:
        print(f"ERROR: transaction detail {daten[0]} is not known in line {s_idx + 1}.")


############################## Small tag functions

def DTM(segment: list):
    data = segment[1].split(":")
    if data[2] == "102":
        if int(data[1][0:3]) > 3000:
            print(f"ERROR: date at {segment}! Year should be smaller than 3000!")
        if int(data[1][4:5]) > 12:
            print(f"ERROR: date at {segment}! Month should be smaller than 13!")
        if int(data[1][6:7]) > 31:
            print(f"ERROR: date at {segment}! Day should be smaller than 32!")
    elif data[2] == "203":
        if int(data[1][0:3]) > 3000:
            print(f"ERROR: date at {segment}! Year should be smaller than 3000!")
        if int(data[1][4:5]) > 12:
            print(f"ERROR: date at {segment}! Month should be smaller than 13!")
        if int(data[1][6:7]) > 31:
            print(f"ERROR: date at {segment}! Day should be smaller than 32!")
        if int(data[1][8:9]) > 31:
            print(f"ERROR: date at {segment}! Hour should be smaller than 24!")
        if int(data[1][10:11]) > 60:
            print(f"ERROR: date at {segment}! Minute should be smaller than 60!")
    else:
        print("DTM: ", data[2], "not known.")


def NAD(segment: list):
    ...


def LIN(segment: list):
    ...


def QTY(segment: list):
    ...


def BGM(segment: list):
    ...


def UNS(segment: list):
    if segment[1] not in ('S', 'D'):
        print("ERROR: The parameter of UNS has to be 'S' or 'D'!")


def CNT(segment: list):
    ...


######## RUN ##########
if __name__ == '__main__':
    check(file)
