# Target backlog

Providers not yet scraped, to be worked through one at a time. Endpoints marked
**verified** returned HTTP 200 on 2026-06-11. Discovery angle: FedRAMP marketplace
(https://www.fedramp.gov/marketplace/products/?view=cards) sorted by reuse, plus
major non-US clouds.

## Machine-readable feeds (easy wins, verified)

- [ ] **Imperva** (FedRAMP WAF/CDN) — https://my.imperva.com/api/integration/v1/ips
- [ ] **MongoDB Atlas** (FedRAMP) — https://cloud.mongodb.com/api/atlas/v2/unauth/controlPlaneIPAddresses
      (requires header `Accept: application/vnd.atlas.2023-11-15+json`, returns 406 without it)
- [ ] **New Relic** synthetics egress — https://s3.amazonaws.com/nr-synthetics-assets/nat-ip-dnsname/production/ip-ranges.json
- [ ] **PagerDuty** webhook sources — https://app.pagerduty.com/webhook_ips
- [ ] **Bunny.net CDN** — https://api.bunny.net/system/edgeserverlist and https://api.bunny.net/system/edgeserverlist/ipv6
- [ ] **Gcore CDN** — https://api.gcore.com/cdn/public-ip-list
- [ ] **CacheFly CDN** — https://cachefly.cachefly.net/ips/cdn.txt
- [ ] **Vultr** (RFC 8805 geofeed) — https://geofeed.constant.com/?json
- [ ] **Apple iCloud Private Relay** egress — https://mask-api.icloud.com/egress-ip-ranges.csv
- [ ] **Starlink** geofeed — https://geoip.starlinkisp.net/feed.csv
- [ ] **Google goog.json** — https://www.gstatic.com/ipranges/goog.json
      (all of Google; diff against cloud.json to isolate Workspace/services ranges —
      see data/README.md TODO "split Google ranges")

## HTML docs / portal-only (need scrapers or manual refresh)

- [ ] **ServiceNow** (top-reuse FedRAMP) — ranges only in support-portal KB, login required
- [ ] **Workday** — per-tenant docs
- [ ] **Box** — https://support.box.com/hc/en-us/articles/360043696354
- [ ] **DocuSign** — https://www.docusign.com/trust/security/esignature
- [ ] **Cisco Webex** — https://help.webex.com/en-us/article/WBX264/
- [ ] **Twilio** — per-product pages, e.g. https://www.twilio.com/docs/sip-trunking/ip-addresses
- [ ] **Qualys** — per-platform pages, https://www.qualys.com/platform-identification/
- [ ] **Splunk Cloud** — per-stack docs
- [ ] **GitLab.com** — https://docs.gitlab.com/ee/user/gitlab_com/#ip-range
- [ ] **IBM Cloud** — https://cloud.ibm.com/docs/cloud-infrastructure?topic=cloud-infrastructure-ibm-cloud-ip-ranges
- [ ] **Slack** — https://slack.com/help/articles/360001603387 (egress mostly AWS)
- [ ] **Salesforce Government Cloud** — separate from ip-ranges.salesforce.com, KB only
- [ ] **Adobe Experience Cloud / Sign** — per-product docs
- [ ] **Proofpoint** — https://help.proofpoint.com (per-cluster pages)
- [ ] **Elastic Cloud** — per-region docs
- [ ] **Sumo Logic** — per-deployment docs
- [ ] **Databricks** — per-region NAT/control-plane IPs in docs

## Tenant API key required (defer)

- [ ] **Palo Alto Prisma Access** (FedRAMP SSE) — API needs tenant key
- [ ] **Netskope** (FedRAMP SSE) — per-tenant download URL
- [ ] **iboss** (FedRAMP SSE) — node ranges via support portal
- [ ] **Akamai CDN** — SiteShield/origin lists are portal-only
      (Akamai Connected Cloud compute = Linode, already covered)
- [ ] **Snowflake** — per-account hostnames/IPs via SYSTEM$ALLOWLIST, no global feed

## ASN-based candidates (extend src/dl/download_asn.py config)

Already configured: Alibaba (AS45102, AS37963), Tencent (AS132203, AS45090),
Huawei (AS136907), Baidu (AS38365), OVHcloud (AS16276, AS35540),
Hetzner (AS24940), Scaleway (AS12876), IONOS (AS8560).

- [ ] **UpCloud** — AS202053
- [ ] **Exoscale** — AS61098
- [ ] **Open Telekom Cloud** (T-Systems) — confirm ASN before adding
- [ ] **StackIT** (Schwarz Group) — confirm ASN before adding
- [ ] **OUTSCALE** (Dassault, SecNumCloud) — confirm ASN before adding
- [ ] **Aruba Cloud** (IT) — confirm ASN before adding
- [ ] **Kingsoft Cloud** (CN) — confirm ASN before adding
- [ ] **G42/Core42** (UAE), **Yandex Cloud** (AS200350, sanctions caveat) — optional

## Dead / not applicable (do not add)

- **Edgio, StackPath** — defunct
- **Azure Germany** — cloud retired 2021; existing azure-germany.json is frozen
- **CircleCI** — old dl.circleci.com/static/ip-ranges.json returns 404; IP ranges
  feature now requires auth
- **UptimeRobot** — old locations.txt endpoint returns 404; find replacement
- **AWS China** — already inside aws.json (cn-north-1 / cn-northwest-1)
