# TODO for data gathering

- [IANA IPv4 assignment](https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml)

- [IANA IPv6 assignment](https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml)

- [IANA AS assignment](https://www.iana.org/assignments/as-numbers/as-numbers.xhtml)

- Private IP ranges

- Update and split Google ranges between Google Cloud and Google Services

## Classification of Services

The returned data should provide the user with an understanding where this IP could belong to the closest source. The closest source tends to be wrapped around the following:

- private IP (ex. 10.0.0.0/8, 172.16.0.0/12, 192.0.0.0/24 ranges)
- Software as a Service provider - (ex. video as a service such as Zoom, monitoring as a service such as Pingdom, code repository as a service such as Github).
- Cloud Service Provider (ex. Amazon Web Services - AWS, Microsoft Azure, Google Cloud, Oracle Cloud, etc).
- Content Delivery Network (ex. Cloudflare, Fastly)
- Tier 1 networks (ex. Lumen/CenturyLink, AT&T)
