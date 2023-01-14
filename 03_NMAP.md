**Instructor: Nima Shahmoradi**

#### Nmap Flags:

  **NOTE: A normal nmap scan without specifying what port to scan will consider the common 1000 ports used**
  - `-F` - Scan 100 common ports
  - `-O` - OS Fingerprinting
  - `-sV` - Service Version Detection
  - `-sC` - Performs a script scan using the default set of scripts (equivalent to `--script=default`)
  - `-A` - Aggressive scan that performs OS Detection(`-O`), Service Version Detection(`-sV`), Script Scanning(`-sC`)
  - `-Pn` - skip host discovery. If the target blocks ICMP requests, this will result in Nmap assuming that the host is down.
  - `-sn` - don't perform port scan after host discovery (also called as **Ping Scan**)
  - **Combo Scan?** :
    - `-sSU` - combination of SYN Scan and UDP Scan
    - `-sSV` - combination of SYN Scan and Service version detection
    > **NOTE: In general `-s*` is called scan all types. Any type of scan that are not mutually exclusive in context can be combined**
  - `-T<x>` - set the speed of the scan (valid values for **\<x\>**: **0 - 5**)
  - `-D RND:<x>` - generate random \<x\> number of ip addresses and send packets
  - `-D <random_private_ip1,[ip2,...,ME]>` - same as `-D RND:<x>` but manual ip entry (Here, `ME` is your local IP)
  - `-p <x>` - scan a single port **\<x\>** 
  - `-p<x>-<y>` - set port scan range from **\<x\>** to **\<y\>**
  - `-p<a>,<b>,<c>...` - only scan port **\<a\>, \<b\>, \<c\>,...** and so on
  - `-p-` - scan all ports
  - `-d` - increase debugging level (`-dd` for greater effect)
  - `-v` - verbose level (`[-vv | -v2] | [-vvv | -v3] ` for more verbosity)
  - `--packet-trace` - show all packets sent and received
  - `--osscan-guess` - Guess OS detection results
  - `-iL <ip_list.txt>` - Read targets from **ip_list.txt**
  - `-n` - Never do DNS resolution (equivalent to `-R` i.e. Always resolve)
  - `-oA <filename>` - save output to file **\<filename\>**.(nmap, xml, gnmap) all at once
  - `-oN [-oX | -oG | -oS] <filename>` - save output to file **\<filename\>** as nmap | xml | gnmap | scriptkiddie format


---

#### Nmap Port Scanning:

- **ACK PROBE SCAN**: `nmap -sA 192.168.8.123`
  > **Ports are unfiltered**: (src)`ACK`, (dst)`RST` **[For both open & closed ports]**
  >
  >> Here **"unfiltered"** means firewall is **turned off** or **not present**]
  > 
  > **Ports are filtered**: (src)`ACK`, (dst)`<No Response / Destination unreachable>`
  >
  > **NOTE: TCP ACK won't work for stateful firewalls**

- **TCP Scan**: `nmap -sT -p445 192.168.8.123`
  > **Port Opened**: (src)`SYN`, (dst)`SYN, ACK`, (src)`ACK`, (src)`RST`
  > 
  > **Port Closed**: (src)`SYN`, (dst)`RST, ACK`

- **SYN / STEALTH Scan**: `nmap -sS -p445 192.168.8.123`
  > **Port Opened**: (src)`SYN`, (dst)`SYN, ACK`, (src)`RST`
  > 
  > **Port Closed**: (src)`SYN`, (dst)`RST, ACK`

- **FIN Scan**: `nmap -sF -p445 192.168.8.123`
  > **Port Opened**: (src)`FIN`
  > 
  > **Port Closed**: (src)`SYN`, (dst)`RST, ACK`

- **NULL Scan**: `nmap -sN -p445 192.168.8.123`
  > **Port Opened**: (src)`<None>`
  > 
  > **Port Closed**: (src)`<None>`, (dst)`RST, ACK`

- **XMAS Scan**: `nmap -sX -p445 192.168.8.123`
  > **Port Opened | Filtered**: (src)`FIN, PSH, URG`
  > 
  > **Port Closed**: (src)`FIN, PSH, URG`, (dst)`RST, ACK`

- **UDP Scan**: `nmap -sU -p161 192.168.8.123`
  > **Port Opened | Filtered**: (src)`<Datagram>`
  > 
  > **Port Closed**: (src)`<Datagram>`, (dst)`<Dst/Port unreachable>`

---

#### Nmap Script Scanning:

> **To run a script**: `--script` `<script_category>` | `<script_name>`
>> - `<script_category>` = `auth` | `broadcast` | `brute` | `default` | `discovery` | `dos` | `exploit` | `external` | `fuzzer` | `intrusive` | `malware` | `safe` | `version` | `vuln`
>>
>> - `<script_name>` = **see this location(**`/usr/share/nmap/scripts`**)**
>
> **Description about a specific script**: `nmap --script-help <script_name>.nse`

- Examples:
  - SMB Vulnerability - `nmap -sS --script smb-vuln-ms08-067 <target's_ip>`
  - Vulners - `nmap -sS -sV --script vulners <target's_ip>`
  - SSH Bruteforcing - `nmap --script ssh-brute -p22 <target's_ip> --script-args userdb=<usernames_list.txt>,passdb=<passwords_list.txt>`

- NSE can also be downloaded from online. Few ones are mentioned below:
  - [nmap-vulners](https://github.com/vulnersCom/nmap-vulners.git)
  - [vulscan](https://github.com/scipag/vulscan.git)

For more: [NSE-USAGE](https://nmap.org/book/nse-usage.html)

---

#### Nmap Enumeration:

- **HTTP Enumeration** - `nmap -sV --script http-enum <target's_ip>`
- **DNS Enumeration** - `nmap -sSU -p 53 --script dns-nsec-enum --script-args dns-nsec-enum.domains=example.com <target's_ip>`
- **MySQL Enumeration** - `nmap --script mysql-enum <target's_ip>`
- **SMB Users Enumeration** - `nmap --script smb-enum-users.nse <target's_ip>`

---

#### Custom NSE scripting:

**Lua** programming language is used for creating NSE scripts.

Following is an example script for finding whether a port is open

> **filename:** `my_script.nse`
>```lua
>description=[[
>  This is a simple script example that determines if a port is open.
>]]
>
>author = "C3L35T3"
>
>-- RULE --
>portrule = function(host, port)
>        return port.protocol == "tcp"
>                and port.state == "open"
>end
>
>-- ACTION --
>action = function(host, port)
>        return "This port is open!"
>end
>```
> **to run script:** `nmap -p80,443 --script my_script <target's_ip>`
>
> For more: [NSE Doc](https://nmap.org/book/nsedoc.html)

---

#### Nmap Integration
- Metasploit Integration:
  > $: `msfconsole`
  >
  > $msf> `db_nmap -V -sV <target's_ip>`
  - Different types of commands similar to the above one can be seen using Armitage that is a GUI version of metaploit by going to: `Hosts > Nmap Scan`

---

#### Extras:
- [NmapAutomator](https://github.com/21y4d/nmapAutomator.git)

---
