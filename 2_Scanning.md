**Instructor: Dimitris Amprazis**

#### Search Filters:
- Protocol filter: `http`
- Boolean filter: `http||arp`
- Comparison: 
    - source ip filter: `ip.src==216.58.198.14`
    - destination ip filter: `ip.dst==192.168.1.49`
    - `tcp.port eq 80`
    - `ip.dst != 192.168.1.1`
- Boolean & Comparison filter combination: `http&&ip.src==95.100.242.40`
- Misc:
  - View lost TCP Segment: `tcp.analysis.lost_segment`
  - View Retransmitted TCP Segment: `tcp.analysis.retransmission`

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

- **ICMP / Ping / Host Discovery Utils**:

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

  - **ICMP Codes**:

    | Query Codes                       |      Error Codes                  |
    |-----------------------------------|-----------------------------------|
    | **Type 0** - Echo Reply           | **Type 3** - Echo Reply           |
    | **Type 8** - Echo Request         | **Type 4** - Echo Request         |
    | **Type 9** - Router Advertisement | **Type 5** - Router Advertisement |
    | **Type 10** - Router Solicitation | **Type 11** - Router Solicitation |
    | **Type 13** - Timestamp Request   | **Type 12** - Timestamp Request   |
    | **Type 14** - Timestamp Reply

- **Nmap scan arguments:**
  - **-A** - OS Detection, service detection, script scanning
  - **-Pn** - display nmap from ICMP pinging to check if host is up. If the target blocks ICMP requests, this will result in Nmap assuming that the host is down.
  - **-T4** - set the speed of the scan(valid params: 0 - 5)
  - **-p1-65535** - set port scan range(-p- is an alternative to scan all ports)
