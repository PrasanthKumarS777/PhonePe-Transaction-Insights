import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Pr%40santh001@localhost:5432/phonepe_db")

tables = ["agg_transaction","agg_users","agg_insurance",
          "map_transaction","map_users","map_insurance",
          "top_transaction","top_users","top_insurance"]

for t in tables:
    pd.read_sql(f"SELECT * FROM {t}", engine).to_csv(f"dashboard/data/{t}.csv", index=False)
    print(f"✅ {t}.csv exported")
