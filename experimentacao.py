dados[head].with_columns(
    pl.struct(["Year", "Week"]).map_elements(
        lambda x: 
            get_first_day_of_week(x["Year"], x["Week"]),
            return_dtype=pl.Datetime
    ).alias("Data")
).sort(by=["Data"])

df = dados['users_ac_week'].with_columns(
    pl.struct(["Year", "Week"]).map_elements(
        lambda x:
            get_first_day_of_week(x["Year"], x["Week"]),
            return_dtype=pl.Datetime
    ).alias("Data")

)



result = df.group_by("Data").agg(
    pl.exclude(["Year", "Week", "Data"]).all.map_elements(lambda x: x[1], return_dtype=pl.Int64).sum()
)

df.group_by("Data").agg(pl.exclude(["Year", "Week"]).sum())

df.group_by("Data").agg(pl.exclude(["Year", "Week"]).sum()).tail(6)


ddt = df.filter(pl.col("Data")==df.filter((pl.col("Year")==2025)&(pl.col("Week")==1))["Data"][0])
ddt.group_by("Data").agg(pl.exclude(["Year", "Week"]).sum())