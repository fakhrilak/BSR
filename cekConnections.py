import subprocess

def CekConnections(ip):
    test = subprocess.Popen(["ping","-W","2","-c", "1",ip], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    output = output.split("\n")
    if len(output) == 7:
        return {
            "status" : True,
            "message" : output[4]
        }
    else:
        return {
            "status" : False,
            "message" : output[3]
        }
        
data = CekConnections(ip="192.168.1.17")
print(data["status"])
print(data["message"])