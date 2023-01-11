**Instructor: Nima Shahmoradi**

#### Nmap Flags:

  - `-O` - OS Fingerprinting
  - `-A` - OS Detection, service detection, script scanning
  - `-sV` - Service Version Detection
  - `-sC` - Performs a script scan using the default set of scripts (equivalent to `--script=default`)
  - `-Pn` - skip host discovery. If the target blocks ICMP requests, this will result in Nmap assuming that the host is down.
  - `-sn` - don't perform port scan after host discovery (also called as **Ping Scan**)
  - `-T<x>` - set the speed of the scan (valid values for **\<x\>**: **0 - 5**)
  - `-p <x>` - scan a single port **\<x\>** 
  - `-p<x>-<y>` - set port scan range from **\<x\>** to **\<y\>**
  - `-p<a>,<b>,<c>...` - only scan port **\<a\>, \<b\>, \<c\>,...** and so on
  - `-p-` - scan all ports
  - `-d` - increase debugging level (`-dd` for greater effect)
  - `--packet-trace` - show all packets sent and received
  - `--osscan-guess` - Guess OS detection results
  - `-iL <ip_list.txt>` - Read targets from **ip_list.txt**
  - `-n` - Never do DNS resolution (equivalent to `-R` i.e. Always resolve)
  - `-oA <filename>` - save output to file **\<filename\>**.(nmap, xml, gnmap) all at once

---

#### Nmap Port Scanning:

- **TCP Scan**: `nmap -sT -p445 192.168.8.123`
  > **Port Opened**: (src)`SYN`, (dst)`SYN, ACK`, (src)`ACK`, (src)`RST`
  > 
  > **Port Closed**: (src)`SYN`, (dst)`RST, ACK`

- **SYN Scan**: `nmap -sS -p445 192.168.8.123`
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
  > **Port Closed**: (src)`<Datagram>`, (dst)`Dst/Port unreachable`

---

#### Nmap Script Scanning:

> **To run a script**: `--script` `<script_category>` | `<script_name>`
>> - `<script_category>` = `auth` | `broadcast` | `brute` | `default` | `discovery` | `dos` | `exploit` | `external` | `fuzzer` | `intrusive` | `malware` | `safe` | `version` | `vuln`
>>
>> - `<script_name>` = **view** `/usr/share/nmap/scripts`
>
>**Description about a specific script** - `nmap --script-help <script_name>.nse`
>
For more: [NSE-USAGE](https://nmap.org/book/nse-usage.html)

---
