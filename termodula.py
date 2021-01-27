import sys
Name = "root"
Vmail = "localhost"
Address = ""

def SortArguments(args):
    # your code goes here
    pass


def GetArguments(Name = "root", Domen = "localhost", PsevdoAddress = "~"):
    PsevdoAddress = Address
    if Address == "":
        PsevdoAddress="~"
    Mail = "{}@{}".format(Name, Domen)
    
    print("[{} {}]".format(Mail, PsevdoAddress))
    # your code goes here
    pass


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
if __name__ == "__main__": # выход если внутри.
    main(sys.args)
