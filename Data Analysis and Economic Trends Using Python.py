

import pandas as pd
df = pd.read_csv("3610010701-eng (1).csv", on_bad_lines='skip')
df.columns = ["year", "category", "value"]

summary = df.groupby(["year", "category"])["value"].sum().reset_index()

summary["growth_rate"] = summary.groupby("category")["value"].pct_change()

latest_year = summary["year"].max()

latest = summary[summary["year"] == latest_year]
top_categories = latest.sort_values("value", ascending=False).head(3)

latest_year = summary["year"].max()

latest = summary[summary["year"] == latest_year]
top_categories = latest.sort_values("value", ascending=False).head(3)

growth_summary = summary.dropna().groupby("category")["growth_rate"].mean()

for category, growth in growth_summary.items():
    print(
        f"The {category} category experienced an average annual growth rate of "
        f"{growth:.2%}, suggesting {'expansion' if growth > 0 else 'contraction'}."
    )