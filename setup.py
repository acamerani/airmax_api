def config_default():
      con=[]
      file=open("config.txt","r")
      riga=file.readline()
      while riga!="":
            vet=riga.split(":")
            con.append((vet[1].strip("\n")))
            riga=file.readline()
      return con
