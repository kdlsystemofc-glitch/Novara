import json

with open("lighthouse-mobile.json", "r", encoding="utf-8") as f:
    data = json.load(f)

audits = data.get("audits", {})

print("=== CORE WEB VITALS & METRICS ===")
for m in ["first-contentful-paint", "largest-contentful-paint", "total-blocking-time", "cumulative-layout-shift", "speed-index", "interactive"]:
    item = audits.get(m, {})
    print(f"  {m}: {item.get('displayValue')} (score: {item.get('score')}, numericValue: {item.get('numericValue')})")

print("\n=== LOW SCORING AUDITS (< 0.9) ===")
for k, v in audits.items():
    score = v.get("score")
    if score is not None and score < 0.9:
        print(f"  [{k}] score={score} | title={v.get('title')} | displayValue={v.get('displayValue')}")
        details = v.get("details", {})
        items = details.get("items", [])
        if items:
            for item in items[:5]:
                url = item.get("url", item.get("source", ""))
                wasted = item.get("wastedMs", item.get("wastedBytes", ""))
                print(f"       -> {url} | wasted: {wasted}")
