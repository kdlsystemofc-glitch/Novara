import json

with open("lighthouse-mobile.json", "r", encoding="utf-8") as f:
    data = json.load(f)

reqs = data.get("audits", {}).get("network-requests", {}).get("details", {}).get("items", [])
print(f"Total requests: {len(reqs)}")
for r in reqs:
    url = r.get("url", "").split("/")[-1]
    priority = r.get("priority", "")
    mime = r.get("mimeType", "")
    size = r.get("resourceSize", 0) // 1024
    start = round(r.get("networkRequestTime", 0) * 1000)
    end = round(r.get("networkEndTime", 0) * 1000)
    print(f"  {url:35} | prio={priority:7} | mime={mime:15} | size={size:3}KB | t={start}..{end}ms")
