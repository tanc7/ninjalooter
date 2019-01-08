# ninjalooter
Design draft for a comprehensive, multi-platform, post-exploitation framework

# hiGoals and objectives

To completely replace common post exploitation frameworks such as Metasploit by making a niche-product, a product that focuses strictly on taking advantage of a privileged shell to loot the system.

That means the task of obtaining that shell is left to the attacker, who already have many options to get that shell. Whether they make their own payload or generate one. 

Ninjalooter is designed to be a "specialty thermobaric bomb". The means of dropping that bomb and getting the bomb safely to the target is still the attackers responsibility.

Many competing products often lack comprehensive post exploitation capabilities. Some have additional pivoting features and others can interface with one another. Some can open proxies in their native language (like PHP) and many other neat tricks, but the seemingly simple task of ransacking the file structure of all known users and passwords, shared credentials, and hashes seem to either be nonexistent or spotty.

Rather, most attackers are advertised the effectiveness of a payload in bypassing protections. Not how well can it carry it's damage or rampage.

We assume you already got that part figured out. And you want a means to loot a pwned box regardless of OS or framework.

We also assume you want a..

1. Persistent tunnel established to push "malware upgrades" at will

2. Endless pivoting options by a multitude of methods including but not limited to... SMB shares, Apple File Protocol, infecting local repositories (like RHEL corporate repositories), rogue DNS servers, named pipes, powershell session creation, this includes using the aforementioned rogue DNS servers to point to rogue Windows update servers

3. Immediate switch to botnet builder mode. With your choice of command and control, Google Golang, Nodejs, PHP, Java in a easy to use, point and click interactive web interface. 

What else do you want... I'm thinking

4. A rogue ecosystem builder. Easily port JavaScript, Java, Ruby, Python, PHP into compromised hosts that do not natively have it installed. 

5. Domain post exploitation options. Shut down browser sandboxes remotely, flag honeypots and fill it with useless shells and misinformation, discreetly assassinate endpoint protection like Symantec SEP and Cisco AMP.

6. Redundant storage and backup infector. Monitor usage of backup volumes in real time to determine usage and possible tangible locations of backup volumes. Monitor changes throughout the network on file system changes and predict where to strike the incident response team.

How the fuck do you do that?!? You got to have some really dumb workers for me to track that kind of information.

Or use a exploit like brutal kangaroo to attack air-gapped systems and slowly aggregate the information I need to discern how the backup storage is deployed.

This part is the long term project. I gotta catch IRT with their pants down.

What else do you want?!?

7. Okay. Maybe we need a better environment to generate compatible payloads. No more, shell script bullshit, or relying on msfvenom. 

I want a virtualized environment. OSX with py2app to make you your macho .app files and pkgbuilder your . IPA format. Because doing it their way is the right way. 

I want a virtualized Windows environment to make me pe32 files and .dll's. 

I don't want no trouble from Apple either.

Maybe, a virtualized cloud service that just generates the right payloads for the customer. I legitimately paid for the license for Windows, Mac, and OSX. I legitimately own the cloud servers. You simply submit your payload for compilation. And I send it back to you within a minute.

I will use my own app signing key for all Android apps and iPhone apps. I'm getting paid for it, and I didn't do anything wrong IMO.

What's the difference between me and gcc? A lot of people that use me instead are mostly dicks.

The worst I seen is that the key will get flagged and the app gets deleted. I don't think I'm going to face criminal charges for this. All I do is compile shit. I compile shit for people that don't have the virtualized means to put together their app themselves.


What I don't realize is that there does not seem to be all in one solution for post exploitation. Even though we know how to access the hive, unshadow passwords, and dump the keychain. 


The hard part is actually the pivoting part, being able to maintain your momentum without being detected.


# Required languages and frameworks to write this

Python and C
Objective-C and Swift

Focus on learning Python and Swift now that I can develop apps on Mac OSX using bootlegged copy. Both appear to be built on top of their parent language and offer flexibility and prewritten modules as well as development time cuts.

A little bit of...

Java, Ruby, Nodejs, and PHP

New capabilities...

Apply all evasion methods covered by NSS during their testing of anti-malware endpoint protection.

1.  In memory execution
2. Binary obfuscation
3. Payload and traffic encoding
4. Antivirus evasion via shutdown commands or changing of payload signature
5. Injection or migration into another process
6. Hiding of argument variables
7. Usage of symbolic links and hidden directories
8. Appending itself into another program/script/binary file
9. Rogue DNS/HTTP/DHCP/SMB/SSH Servers and proxies
10. Changing or scrambling the nature of the PE32 file and/or armoring the code to prevent disclosure of exploit upon capture (not as easily), *this requires a custom toolkit written for each platform, for example the Machine Object files of Mac OSX. And requires extended testing to ensure it didn't break the payload. This also applies to binary encoding*
11. Encrypting payload with one way hash key. (More useful in scripting languages).
12. XOR encoding of binary. 
13. Sandbox evasion
14. VM detection

Can be compiled into binary format, pe32, macho/app, Lin, and Python .py, Android .apk and iPhone . IPA

Autonomous post exploitation bot. Designed to be dropped through a reverse shell or remote access Trojan

Detects environment and can attack numerous operating systems. Can attack Windows, Mac OSX, Linux, Android and iPhone iOS

Automatic privilege escalation.

Hard coded to contact your C2 server. Each bot is compiled before use every time. Compile the bot when you get a shell, and drop it through and execute it.

It's normal operation is to loot all tangible credentials and cleartext passwords and has somewhat the same functionality as a remote access Trojan. The difference is that the ninjalooter is designed solely for post exploitation. While RATs can consist of a attack phase as well (spearphishing emails, or injection via shellcode). 

*Windows HIVE credentials
*Unshadowed /etc/passwd /etc/shadow files
*Mac OSX keychain https://arstechnica.com/information-technology/2012/09/mac-os-x-keychain-pillaging-app/
*Android sqlite databases
*iPhone creds
*Browser caches

Generates it's own encrypted SSH connection and can utilize SOCKS and HTTPS proxies

Contains by default, powershell scripts and commands for Windows victims, bash scripts and executable binaries for Linux, and py2app for Mac OSX.

Comes with a shrunken down installation of Python interpreter, nodejs, PHP, Java, Ruby to allow additional frameworks to run through the bot.

Can natively generate it's own SOCKS and HTTPS proxies, and can interface with common RATs via local port forwarding to allow pivoting types of attacks (similar to Metasploit).

Can be configured to build botnets as a alternative functionality.
