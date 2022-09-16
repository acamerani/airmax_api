import sys
from setup import config_default
from api import con_api
subnet=""
user=""
password=""
porta=""
protocollo=""
if len(sys.argv)==1:
    print("\n")
    print("COMANDI SHELL")
    print("--help                visualizza la lista di comandi disponibili")
    print("-s                    specifica la subnet sulla quale fare il controllo")
    print("-u                    indica quale user utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
    print("-ps                   indica quale password utilizzare, altrimenti usa quelle di default di ubiquiti ubnt")
    print("-p                    indica quale porta utilizzare, altrimenti utilizza la porta di default 80")
    print("-pt                   indica il protocollo da utilizzare, http o https")
    print("-d                    user, password, porta e protocollo presi dal file di configurazione")
else:
    i=0
    if (len(sys.argv))>1 and (sys.argv[1])=="--help":
        print("\n")
        print("COMANDI SHELL")
        print("--help                visualizza la lista di comandi disponibili")
        print("-s                    specifica la subnet sulla quale fare il controllo")
        print("-u                    indica quale user utilizzare")
        print("-ps                   indica quale password utilizzare")
        print("-p                    indica quale porta utilizzare")
        print("-pt                   indica il protocollo da utilizzare, http o https")
        print("-d                    user, password, porta e protocollo presi dal file di configurazione")
        print("\n")
    if "-s" in sys.argv:
        ind_subnet=sys.argv.index("-s")+1
        subnet=sys.argv[ind_subnet]
        print("\n"+subnet)
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
    if "-pt" in sys.argv:
        ind_protocollo=sys.argv.index("-pt")+1
        protocollo=sys.argv[ind_protocollo]
        print(protocollo)
    if "-d" in sys.argv:
        con_list=config_default()
        if protocollo=="":
            protocollo=con_list[0]
        if subnet=="":
            subnet=con_list[1]
        if user=="":
            user=con_list[2]
        if password=="":
            password=con_list[3]
        if porta=="":
            porta=con_list[4]
    if "-s" not in sys.argv:
        print("specificare un IP o una classe di IP")
    if "-u" not in sys.argv:
        print("user di default")
    if "-ps" not in sys.argv:
        print("password di default")
    if "-p" not in sys.argv:
        print("porta di default")
    if "-pt" not in sys.argv:
        print("protocollo di default")


con_api(protocollo,subnet,user,password,porta)
