# Target backlog

Providers not yet scraped, to be worked through one at a time. Endpoints marked
**verified** returned HTTP 200 on 2026-06-11. Discovery angle: FedRAMP marketplace
(https://www.fedramp.gov/marketplace/products/?view=cards) sorted by reuse, plus
major non-US clouds.

## Machine-readable feeds (easy wins, verified)

- [ ] **Google goog.json** — https://www.gstatic.com/ipranges/goog.json
      (all of Google; diff against cloud.json to isolate Workspace/services ranges —
      see data/README.md TODO "split Google ranges")

## HTML docs (need scrapers or periodic refresh)

- [ ] **IBM Cloud** — https://cloud.ibm.com/docs/cloud-infrastructure?topic=cloud-infrastructure-ibm-cloud-ip-ranges
      (timed out during verification; may be slow or gated)
- [ ] **Slack** — https://slack.com/help/articles/360001603387
      (egress mostly AWS; actual IPs served at my.slack.com, different page)
- [ ] **Adobe Experience Cloud / Sign** — https://helpx.adobe.com/sign/system-requirements.html
      (consistently timed out during fetch; may require different URL or be blocked)
- [ ] **Databricks** — per-region NAT/control-plane IPs scattered across region sub-pages;
      no single aggregation page found

## Login / portal required (defer)

- [ ] **ServiceNow** (top-reuse FedRAMP) — ranges only in support-portal KB, login required
- [ ] **Workday** — per-tenant docs, no public aggregate
- [ ] **Salesforce Government Cloud** — separate from ip-ranges.salesforce.com, KB only (login required)
- [ ] **Splunk Cloud** — docs return HTTP 403; per-stack, login required
- [ ] **Proofpoint** — https://help.proofpoint.com (per-cluster pages, login required)
- [ ] **Elastic Cloud** — per-region docs, login required to view actual IPs
- [ ] **Palo Alto Prisma Access** (FedRAMP SSE) — API needs tenant key
- [ ] **Netskope** (FedRAMP SSE) — per-tenant download URL
- [ ] **iboss** (FedRAMP SSE) — node ranges via support portal
- [ ] **Akamai CDN** — SiteShield/origin lists are portal-only;
      ASN-based fallback possible: AS36183, AS35994, AS35993, AS30675, AS23455,
      AS23454, AS22207, AS20189, AS18717, AS18680, AS17334, AS16702, AS16625, AS12222
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
- **Box** — support article contains no IP data (verified 2026-06-11)
- **Qualys** — platform-identification page lists domains only, no IP ranges (verified 2026-06-11)
- **Sumo Logic** — collector FAQ contains no IP data, only domain names (verified 2026-06-11)
