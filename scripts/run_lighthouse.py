import http.server
import socketserver
import subprocess
import threading
import json
import time
import os
import sys

PORT = 8080
DIRECTORY = os.path.abspath("site")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        # silence server logs
        pass

def run():
    print(f"Serving {DIRECTORY} on port {PORT}...")
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    time.sleep(1)

    output_path = os.path.abspath("lighthouse-mobile.json")
    if os.path.exists(output_path):
        os.remove(output_path)

    cmd = [
        "npx.cmd" if sys.platform == "win32" else "npx",
        "lighthouse",
        f"http://127.0.0.1:{PORT}/index.html",
        "--output=json",
        f"--output-path={output_path}",
        "--chrome-flags=--headless=new --no-sandbox",
        "--only-categories=performance,accessibility,best-practices,seo"
    ]

    print("Running Lighthouse mobile audit...")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        print("Lighthouse returncode:", proc.returncode)
        if proc.returncode != 0:
            print("STDOUT:", proc.stdout[:1000])
            print("STDERR:", proc.stderr[:1000])
    except Exception as e:
        print("Error running Lighthouse:", e)
    finally:
        server.shutdown()
        server.server_close()
        print("Server stopped.")

    if not os.path.exists(output_path):
        print("Output file not generated!")
        return

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = data.get("categories", {})
    print("\n--- LIGHTHOUSE SCORES (MOBILE) ---")
    for cat_id, cat_info in categories.items():
        score = cat_info.get("score")
        score_pct = int(score * 100) if score is not None else "N/A"
        print(f"- {cat_info.get('title')}: {score_pct}/100")

    audits = data.get("audits", {})
    opportunities = []
    for audit_id, audit in audits.items():
        details = audit.get("details", {})
        if details and details.get("type") == "opportunity":
            wasted_ms = details.get("overallSavingsMs", 0)
            wasted_bytes = details.get("overallSavingsBytes", 0)
            score = audit.get("score", 1)
            if score is not None and score < 1:
                opportunities.append({
                    "id": audit_id,
                    "title": audit.get("title"),
                    "score": score,
                    "wastedMs": wasted_ms,
                    "wastedBytes": wasted_bytes,
                    "description": audit.get("description", "")
                })

    # Sort opportunities by wastedMs descending, then wastedBytes descending
    opportunities.sort(key=lambda x: (x["wastedMs"], x["wastedBytes"]), reverse=True)

    print("\n--- TOP OPPORTUNITIES ---")
    for i, opp in enumerate(opportunities[:5], 1):
        savings_text = []
        if opp["wastedMs"] > 0:
            savings_text.append(f"{opp['wastedMs']:.0f} ms")
        if opp["wastedBytes"] > 0:
            savings_text.append(f"{opp['wastedBytes'] / 1024:.1f} KB")
        savings = ", ".join(savings_text) if savings_text else "Score < 1"
        print(f"{i}. {opp['title']} (Economia potencial: {savings})")
        print(f"   Score: {opp['score']}")

if __name__ == "__main__":
    run()
