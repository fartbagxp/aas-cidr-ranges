from ipwhois import IPWhois
from pprint import pprint

obj = IPWhois('74.125.225.229')
results = obj.lookup_rdap(depth=1)

print(results["asn"])
print(results.get("asn"))

results_stripped = {
    "asn": results.get("asn"),
    "asn_cidr": results.get("asn_cidr"),
    "asn_country_code": results.get("asn_country_code"),
    "asn_date": results.get("asn_date"),
    "asn_description": results.get("asn_description"),
    "asn_registry": results.get("asn_registry"),
    "entities": results.get("entities"),
    "net_start_address": results.get("network").get("cidr"),
    "net_end_address": results.get("network").get("end_address"),
    "net_cidr": results.get("network").get("cidr"),
    "net_type": results.get("network").get("type"),
    "net_organization": results.get("network").get("name"),
    "net_ref": results.get("network").get("links"),
}

if results.get("network") != None:
  if results.get("network").get("events") != None:
    for event in results.get("network").get("events"):
      if event.get("action") == "last changed":
        results_stripped["net_updated"] = event["timestamp"]
      elif event.get("action") == "registration":
        results_stripped["registration"] = event["timestamp"]

pprint(results_stripped)
