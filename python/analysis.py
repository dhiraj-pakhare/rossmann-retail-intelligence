import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Load and merge data
train = pd.read_csv("train.csv", low_memory=False)
store = pd.read_csv("store.csv")
df = pd.merge(train, store, on="Store")
df["Date"] = pd.to_datetime(df["Date"])
df['StateHoliday'] = df['StateHoliday'].replace({'0': 'None', 'a': 'Public', 'b': 'Religious', 'c': 'School'})
df = df[(df['Open'] != 0) & (df['Sales'] > 0)]
df = df.dropna(subset=[
    "Store", "DayOfWeek", "Date", "Sales", "Customers", "Open", "Promo",
    "StateHoliday", "SchoolHoliday", "StoreType", "Assortment", "CompetitionDistance"
])

print("✅ Loaded rows:", len(df))

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@D28992005p",
        database="rossmann"
    )
    print("✅ Connected to MySQL")
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO sales (
            Store, DayOfWeek, Date, Sales, Customers, Open, Promo,
            StateHoliday, SchoolHoliday, StoreType, Assortment, CompetitionDistance
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    success_count = 0
    fail_count = 0

    for i, row in df.iterrows():
        try:
            row_data = (
                int(row["Store"]),
                int(row["DayOfWeek"]),
                row["Date"].date(),
                int(row["Sales"]),
                int(row["Customers"]),
                int(row["Open"]),
                int(row["Promo"]),
                str(row["StateHoliday"]),
                int(row["SchoolHoliday"]),
                str(row["StoreType"]),
                str(row["Assortment"]),
                float(row["CompetitionDistance"])
            )
            cursor.execute(insert_query, row_data)
            success_count += 1

            if success_count % 10000 == 0:
                print(f"✅ Inserted {success_count} rows so far...")

        except Exception as e:
            print("❌ Insert failed:", e)
            fail_count += 1

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Final insert count: {success_count}")
    print(f"❌ Failed inserts: {fail_count}")

except mysql.connector.Error as err:
    print("❌ MySQL connection failed:", err)


df.to_csv("rossmann_sales.csv", index=False)
