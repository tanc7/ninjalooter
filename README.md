# ninjalooter

Design draft for a comprehensive, multi-platform, post-exploitation framework

  Lister Unlimited Cybersecurity Solutions, LLC.
  Non-Proprietary Segment of Ninjalooter (AKA Open-Source/Shareware version)

# Notes: Mac OSX Post-Exploitation Modules are a number one priority for this project

To better differentiate this product compared to its competitors, we primarily focus on exploiting Mac boxes.

Exploit kits targeting Windows and Linux are far too oversaturated, but we see a major lack of up-to-date exploits targeting Macs.

As in... (all in one criteria)

	1. Up-to-date. Not some keychain dumping exploit in the first half of 2009. It has to be current.
	2. Useful. As it, no gimicky or bite-less flaws meant to annoy rather than productively loot and pivot.
	3. Easy to use. Needs to be as easy as "specifying who is the loot destined for", compiling the bot, and then dropping off that bot in a owned host and sending it on its way.

# Goals and objectives: The Atomic Bomb of Post-Exploitation

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

# This is NOT a RAT

The author insists that ninjalooter, despite being RAT-like in behavior, is NOT a Remote Access Trojan. Instead, it is a malicious bot solely dedicated towards post-exploitation of a target.

Differences between ninjalooter and a common Remote Access Trojan (Meterpreter, Pupy, Empire, etc.)

1. Remote Access Trojans either grant or maintain access. Ninjalooter does neither, rather ninjalooter simply helps you exfiltrate and loot files.

2. Remote Access Trojans often flaunt multiple techniques to evade detection. While ninjalooter may perform the same techniques, ninjalooter is strictly a malicious bot that is trying to hide it's ransacking of the victim's directories.

3. Remote Access Trojans are (sometimes) spawned from Reverse Shells via a binary/patched upgrade (Meterpreter) or the execution of a new process (whether solely-in-memory, or as a persistence module, or downloaded and executed via a reverse shell). Ninjalooter is a autonomous, post-exploitation bot, that is immediately activated and functions autonomously after being compiled and "dropped through a shell".

4. Remote Access Trojans are used throughout the pentesting kill-chain, but commonly observed at the initial stages being combined with a exploit or spearphishing attack. Usage of ninjalooter is located usually at the very end of the penetration testing process, immediately following privilege escalation, and preceding pivoting. Ninjalooter works best with full root access so it can hurry it getting it's work done and possesses multiple modules that assist in the pivoting process immediately following it's deployment.

5. Remote Access Trojans have many modules that can be selectively activated via a custom command shell. Ninjalooter works best when left alone and handles it's tasks asynchronously. Commands to ninjalooter is pushed into a queue, where it is automatically downloaded upon return from a successful mission. 

6. Remote Access Trojans can be automated to a limited extent via scripting languages. Ninjalooter is entirely autonomous, and functions better if "left alone to do its job". It does not like interaction, and doesn't want to be bothered. However, you can give it additional tasks through the command queue, hopefully if ninjalooter returns successfully in its mission, it'll find itself more tasks to busy itself with.


# Insistence on doing it "Their Way"...

What do I mean when I say, "let's do it their way..."

  1. I mean instead of using Windows 10's implementation of OpenSSH, we should use Powershell Sessions and Server Message Block protocols to exfiltrate files and negotiate connections, bringing up and down virtual networking devices

  2. Instead of using Python, we are going to use Swift and Objective-C to code Mac OSX exploits

  3. Instead of crudely making copycats of the .ipa file structure, we are going to use Mac OSX's packaging tools to properly create the format ourselves, and use py2app to convert Python code into Macho Binaries and .app executables

Doing it THEIR way is the better way.

  a. It conforms to ever-changing compatibility standards
  b. It is more likely to bypass protection methods
  c. It is more likely to successfully run

How are we going to do it, "their way"?

Well, I successfully installed a copy of Mac OSX High Sierra on my Ubuntu-KVM laptop, which opens up access to tools such as Xcode. Furthermore, it created a fairly recent and up-to-date platform for penetration testing purposes. I am now learning the Apple-method of zero-configuration networking, which is quite extensive and huge to comprehend.


**Let's do it, their way**

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
