import requests
import json
def con_api(protocollo,subnet,user,password,porta):
      login=protocollo+"://"+subnet+":"+porta+"/login.cgi"
      stat=protocollo+"://"+subnet+":"+porta+"/status.cgi"
      signal=protocollo+"://"+subnet+":"+porta+"/signal.cgi"
      try:
            r=requests.get(login,timeout=5)
            z=requests.post(login,data={"username":user,"password":password},cookies=r.cookies)
            q=requests.get(stat,cookies=r.cookies)
            valori=json.loads(q.text)
            nome=valori["host"]["hostname"]
            q=requests.get(signal,cookies=r.cookies)
            valori=json.loads(q.text)
            seg=valori["signal"]
      except Exception:
          seg="0"
      print (seg)




