import os, json, pandas as pd

BASE = "data/pulse/data"
OUT = "dashboard/data"
os.makedirs(OUT, exist_ok=True)

def save(rows, name):
    pd.DataFrame(rows).to_csv(f"{OUT}/{name}.csv", index=False)
    print(f"Done: {name}.csv")

# agg_transaction
rows = []
for state in os.listdir(f"{BASE}/aggregated/transaction/country/india/state"):
    sp = f"{BASE}/aggregated/transaction/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]["transactionData"]
            for t in d:
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "transaction_type":t["name"],
                    "transaction_count":t["paymentInstruments"][0]["count"],
                    "transaction_amount":t["paymentInstruments"][0]["amount"]})
save(rows, "agg_transaction")

# agg_users
rows = []
for state in os.listdir(f"{BASE}/aggregated/user/country/india/state"):
    sp = f"{BASE}/aggregated/user/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]
            brands = d.get("usersByDevice") or []
            for b in brands:
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "brand":b["brand"],"user_count":b["count"],
                    "registered_users":d["aggregated"]["registeredUsers"],
                    "app_opens":d["aggregated"]["appOpens"]})
save(rows, "agg_users")

# agg_insurance
rows = []
for state in os.listdir(f"{BASE}/aggregated/insurance/country/india/state"):
    sp = f"{BASE}/aggregated/insurance/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]["transactionData"]
            for t in d:
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "policy_count":t["paymentInstruments"][0]["count"],
                    "premium_amount":t["paymentInstruments"][0]["amount"]})
save(rows, "agg_insurance")

# map_transaction
rows = []
for state in os.listdir(f"{BASE}/map/transaction/hover/country/india/state"):
    sp = f"{BASE}/map/transaction/hover/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]["hoverDataList"]
            for item in d:
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "district":item["name"],
                    "transaction_count":item["metric"][0]["count"],
                    "transaction_amount":item["metric"][0]["amount"]})
save(rows, "map_transaction")

# map_users
rows = []
for state in os.listdir(f"{BASE}/map/user/hover/country/india/state"):
    sp = f"{BASE}/map/user/hover/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]["hoverData"]
            for district, val in d.items():
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "district":district,
                    "registered_users":val["registeredUsers"],
                    "app_opens":val["appOpens"]})
save(rows, "map_users")

# map_insurance
rows = []
for state in os.listdir(f"{BASE}/map/insurance/hover/country/india/state"):
    sp = f"{BASE}/map/insurance/hover/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]["hoverDataList"]
            for item in d:
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "district":item["name"],
                    "policy_count":item["metric"][0]["count"],
                    "premium_amount":item["metric"][0]["amount"]})
save(rows, "map_insurance")

# top_transaction
rows = []
for state in os.listdir(f"{BASE}/top/transaction/country/india/state"):
    sp = f"{BASE}/top/transaction/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]
            for item in (d.get("districts") or []):
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "entity_name":item["entityName"],
                    "transaction_count":item["metric"]["count"],
                    "transaction_amount":item["metric"]["amount"]})
save(rows, "top_transaction")

# top_users
rows = []
for state in os.listdir(f"{BASE}/top/user/country/india/state"):
    sp = f"{BASE}/top/user/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]
            for item in (d.get("districts") or []):
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "entity_name":item["name"],
                    "registered_users":item["registeredUsers"]})
save(rows, "top_users")

# top_insurance
rows = []
for state in os.listdir(f"{BASE}/top/insurance/country/india/state"):
    sp = f"{BASE}/top/insurance/country/india/state/{state}"
    for year in os.listdir(sp):
        for q in os.listdir(f"{sp}/{year}"):
            d = json.load(open(f"{sp}/{year}/{q}"))["data"]
            for item in (d.get("districts") or []):
                rows.append({"state":state,"year":int(year),"quarter":int(q[:-5]),
                    "entity_name":item["entityName"],
                    "policy_count":item["metric"]["count"],
                    "premium_amount":item["metric"]["amount"]})
save(rows, "top_insurance")

print("All 9 CSVs exported successfully.")
