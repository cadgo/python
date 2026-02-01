from flask import Flask, jsonify
import paramiko, os
import json, sys
from datetime import datetime

HyperV='10.20.2.10'
HyperVUser='cadgo'
try:
    HyperVPass = os.environ["SSHPASS"]
except KeyError as e:
    raise KeyError(f"Please provde a valid SSHKEY")

StatusOutput = {"Status": "Ok", "Command": "", "ReturnCommand": ""}

app = Flask(__name__)

def ConnectSSH(command):
    con = paramiko.SSHClient()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        con.connect(HyperV, 22, username=HyperVUser, password=HyperVPass)
        stdin, stdout, stderr = con.exec_command(command)
        out = stdout.read().decode("utf-8")
        err = stderr.read().decode("utf-8")
        print(out)
        con.close()
    except Exception as e:
        print(f"Error {e}")
        raise Exception(f"Some error happend, connecting to host")
    try:
        cexec = json.loads(out)
    except json.decoder.JSONDecodeError as e:
        print(e)
        StatusOutput["Status"] = "Error"
        StatusOutput["Command"] = command
        StatusOutput["ReturnCommand"] = ""
        ferrjson = json.dumps(StatusOutput)
        return json.loads(ferrjson)
    StatusOutput["Status"] = "Ok"
    StatusOutput["Command"] = command
    StatusOutput["ReturnCommand"] = cexec
    return StatusOutput

@app.route('/getvm', methods=['GET'])
def getvm():
    command =  (
    'powershell -Command "@(Get-VM | '
    'Select-Object Name, State, Status, CPUUsage, MemoryAssigned) '
    '| ConvertTo-Json -Depth 3"'
)
    commandExec = ConnectSSH(command)
    print(f"Connection result {commandExec}")
    return jsonify({
            "status": "success",
            "vms": commandExec
        }), 200

@app.route('/startvm/<vmname>', methods=['GET'])
def startvm(vmname):
    command = f'powershell -Command "Start-vm {vmname} -Passthru -ErrorAction Stop | ConvertTo-Json"'
    print(command)
    commandExec = ConnectSSH(command)
    return jsonify(commandExec), 200


if __name__=="__main__":
    print("Starting app")
    app.run(host="0.0.0.0", port = 5000, debug=True)
