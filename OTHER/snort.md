**Instructor: Alexis Ahmed**

#### Set Nework Adapter to Promiscuous Mode: `ip link set <interface> promisc on`

#### Snort Utils:
- main configuration file - `/etc/snort/snort.conf`
  - Perform the following configurations to `snort.conf`:
    - set **HOME_NET** from **any** to the **ip_range** you wanna monitor. Eg: **192.168.2.0/24**
    - run `snort -T -i <interface> -c /etc/snort/snort.conf` to validate the configurations set
- rules directory location - `/etc/snort/rules/`
  - `/etc/snort/rules/` contains a file: `local.rules` where we can add our own rules
  - [SNORPY](http://www.cyb3rs3c.net/) can be used to create snort rules with ease and add them to **local.rules** file

#### Snort rule syntax:

> \<**Action**\> \<**Protocol**\> \<**Source_Address**\> \<**Source_Port**\> \<**Direction**\> \<**Destination_Address**\> \<**Destination_Port**\> **(Rule Option)**
>
> Here: **Action**, **Protocol**, **Source_Address**, **Source_Port**, **Direction**, **Destination_Address**, **Destination_Port** are all **Rule Headers**
>
>>  **Snort Rule Example**: alert icmp any any -> $HOME_NET any (msg: "ICMP Attempt Attack"; sid: 1000005;)
>>
>> In the above example:
>> |||
>> |---------------------------|------------------------------------------|
>> | **Action**                | alert                                    |
>> | **Protocol**              | icmp                                     |
>> | **Source_Address**        | any                                      |
>> | **Source_Port**           | any                                      |
>> | **Direction**             | ->                                       |
>> | **Destination_Address**   | $HOME_NET                                |
>> | **Destination_Port**      | any                                      |
>> | **Rule Option**           | msg: "ICMP Attempt Attack"; sid: 1000005 |

- Some rules added in local.rules that can be tested:
  ```
  alert icmp any any -> $HOME_NET any (msg: "ICMP Ping Detected"; sid: 100001; rev:1;)

  alert tcp any any -> $HOME_NET 22 (msg: "SSH Authentication Attempt"; sid: 100002; rev:1;)
  ```
  **NOTE:** Make sure the **sid** (signature id) is unique for the rules you create


- Run snort as follows: `snort -q -l /var/log/snort -i <interface> -A console -c /etc/snort/snort.conf`

- View the logs captured using snort: `/var/log/snort`. This can also be straightly opened using **Wireshark** if `-A` with no values are defined and for Syslog like format use the `fast` value for `-A` flag

Use [this link](https://www.snort.org/downloads/#rule-downloads) to download Community or Subscription rules for snort.