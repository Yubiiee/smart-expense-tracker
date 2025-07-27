import pandas as pd

data = {
    "Date": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
    "Amount": [500, 1200, 2500, 300, 1500],
    "Category": ["Food", "Transport", "Shopping", "Entertainment", "Bills"],
    "Description": ["Lunch at cafe", "Cab ride", "Groceries", "Netflix", "Electricity bill"]
}

df = pd.DataFrame(data)
df.to_csv("data/expenses.csv", index=False)
