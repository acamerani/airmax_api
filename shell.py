import sys
if len(sys.argv)==1:
    print("\n")
    print("--help                visualizza la lista di comandi disponibili")
    print("-s                    specifica la subnet sulla quale fare il controllo")
    print("-u                    indica quale user utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
    print("-ps                   indica quale password utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
    print("-p                    indica quale porta utilizzare, altrimenti utilizza la porta di default 80")
else:
    i=0
    if (len(sys.argv))>1 and (sys.argv[1])=="--help":
        print("\n")
        print("--help                visualizza la lista di comandi disponibili")
        print("-s                    specifica la subnet sulla quale fare il controllo")
        print("-u                    indica quale user utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
        print("-ps                   indica quale password utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
        print("-p                    indica quale porta utilizzare, altrimenti utilizza la porta di default 80")
    if "-s" in sys.argv:
        ind_subnet=sys.argv.index("-s")+1
        subnet=sys.argv[ind_subnet]
        print(subnet)
    if "-u" in sys.argv:
        ind_user=sys.argv.index("-u")+1
        user=sys.argv[ind_user]
        print(user)
    if "-ps" in sys.argv:
        ind_password=sys.argv.index("-ps")+1
        password=sys.argv[ind_password]
        print(password)
    if "-p" in sys.argv:
        ind_porta=sys.argv.index("-p")+1
        porta=sys.argv[ind_porta]
        print(porta)
    if "-s" not in sys.argv:
        print("specificare un IP o una classe di IP")
    if "-u" not in sys.argv:
        print("user di default")
    if "-ps" not in sys.argv:
        print("password di default")
    if "-p" not in sys.argv:
        print("porta di default")
