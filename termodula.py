import sys


Name = "root"
Domen = "localhost"
Address = ""


def SortArguments(args):
    # your code goes here
    pass


def GetPsevdoAddress(Address): # ЕСли терминал смотрит с места где находится то ~
    if Address == "":
        return "~"
    else:
        return Address


def GetArguments(Name = "root", Domen = "localhost", Address = ""):
    PsevdoAddress = GetPsevdoAddress(Address)
    Mail = str(Name) + "@" + str(Domen)
    
    Hello = "[" + Mail + " " + PsevdoAddress + "]$ "
    CommandLine = input(Hello)
    
    return StringToList(CommandLine)


def TerminalArguments():
    # your code goes here
    pass


def Terminal():
    # your code goes here
    pass


def TerminalFiles():
    # your code goes here
    pass


def main(args):
    args = SortArguments(args)
    TerminalArguments(args)
    TerminalFiles("read/term/set.term")
    while True:
        args = GetArguments()
        Terminal(args)
    # your code goes here
    pass


# Код программы, а не модуля:
if __name__ == "__main__": # выход если не внутри.
    main(sys.args)
