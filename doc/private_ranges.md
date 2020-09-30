# Private IP ranges

These IP address ranges are traditionally private IP address space, defined by [various IETF specifications](https://tools.ietf.org), and are not routable on the public internet.

## IPv4

The following table are to identify IPv4 ranges and their associated standard.

| Address Block      | Present Use                   | Reference                                                                        |
| ------------------ | ----------------------------- | -------------------------------------------------------------------------------- |
| 0.0.0.0/8          | "This" Network                | [RFC 1122, Section 3.2.1.3](https://tools.ietf.org/html/rfc1122#section-3.2.1.3) |
| 10.0.0.0/8         | Private-Use Networks          | [RFC 1918](https://tools.ietf.org/html/rfc1918)                                  |
| 100.64.0.0/10      | Private-Use Networks          | [RFC 6598](https://tools.ietf.org/html/rfc6598)                                  |
| 127.0.0.0/8        | Loopback                      | [RFC 1122, Section 3.2.1.3](https://tools.ietf.org/html/rfc1122#section-3.2.1.3) |
| 169.254.0.0/16     | Link Local                    | [RFC 3927](https://tools.ietf.org/html/rfc3927)                                  |
| 172.16.0.0/12      | Private-Use Networks          | [RFC 1918](https://tools.ietf.org/html/rfc1918)                                  |
| 192.0.0.0/24       | IETF Protocol Assignments     | [RFC 5736](https://tools.ietf.org/html/rfc5736)                                  |
| 192.0.2.0/24       | TEST-NET-1                    | [RFC 5737](https://tools.ietf.org/html/rfc5737)                                  |
| 192.88.99.0/24     | 6to4 Relay Anycast            | [RFC 3068](https://tools.ietf.org/html/rfc3068)                                  |
| 192.168.0.0/16     | Private-Use Networks          | [RFC 1918](https://tools.ietf.org/html/rfc1918)                                  |
| 198.18.0.0/15      | Device / Network Interconnect | [RFC 2544](https://tools.ietf.org/html/rfc2544)                                  |
| 198.51.100.0/24    | TEST-NET-2                    | [RFC 5737](https://tools.ietf.org/html/rfc5737)                                  |
| 203.0.113.0/24     | TEST-NET-3                    | [RFC 5737](https://tools.ietf.org/html/rfc5737)                                  |
| 224.0.0.0/4        | Multicast                     | [RFC 3171](https://tools.ietf.org/html/rfc3171)                                  |
| 240.0.0.0/4        | Reserved for Future Use       | [RFC 1112, Section 4](https://tools.ietf.org/html/rfc1112#section-4)             |
| 255.255.255.255/32 | Limited Broadcast             | [RFC 919 / RFC 922, Section 7](https://tools.ietf.org/html/rfc919#section-7)     |

## IPv6

**Under Construction**

[RFC2526](https://tools.ietf.org/html/rfc2526)  
[RFC4193](https://tools.ietf.org/html/rfc4193) - Unique Local Address  
[RFC4038](https://tools.ietf.org/html/rfc4038) - Mapping IPv4 in IPv6 for dual stack transition

## IPv4 - IPv6 Equivalent

| IPv4            | IPv6 Equivalent | Used for                           |
| --------------- | --------------- | ---------------------------------- |
| 0.0.0.0         | ::/128          | Unspecified                        |
| 127.0.0.1       | ::1/128         | Loopback                           |
| N/A             | ::ffff/96       | IPv4 mapped                        |
| 10.0.0.0/8      | fc00::/7        | Unique Local Addresses             |
| 172.16.0.0/12   | fc00::/7        | Unique Local Addresses             |
| 192.168.0.0/16  | fc00::/7        | Unique Local Addresses             |
| 169.254.0.0/16  | fe80::/10       | Link-Local Addresses               |
| N/A             | 2001:0000::/32  | Teredo, IPv6 tunneling to IPv4 NAT |
| 198.18.0.0/15   | 2001:0002::/48  | Benchmarking                       |
| N/A             | 2001:0010::/28  | Orchid - Experiment only           |
| 192.88.99.0/24  | 2002::/16       | 6to4 addressing                    |
| 192.0.2.0/24    | 2001:db8::/32   | Documentation only                 |
| 198.51.100.0/24 | 2001:db8::/32   | Documentation only                 |
| 203.0.113.0/24  | 2001:db8::/32   | Documentation only                 |
| N/A             | 2000::/3        | Global Unicast                     |
| 224.0.0.0/4     | ff00::/8        | Multicast                          |
