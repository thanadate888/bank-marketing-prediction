import pandas as pd
import random

# จำนวนข้อมูล
n = 500

jobs = ["admin.", "technician", "services", "management", "retired",
        "blue-collar", "student", "entrepreneur", "housemaid"]

marital_status = ["married", "single", "divorced"]
education = ["primary", "secondary", "tertiary"]
default = ["yes", "no"]
housing = ["yes", "no"]
loan = ["yes", "no"]
contact = ["cellular", "telephone"]
month = ["jan","feb","mar","apr","may","jun",
         "jul","aug","sep","oct","nov","dec"]
poutcome = ["success", "failure", "other", "unknown"]
target = ["yes", "no"]

data = []

for _ in range(n):
    row = [
        random.randint(18, 70),                     # age
        random.choice(jobs),
        random.choice(marital_status),
        random.choice(education),
        random.choice(default),
        random.randint(-2000, 100000),               # balance
        random.choice(housing),
        random.choice(loan),
        random.choice(contact),
        random.randint(1, 31),                       # day
        random.choice(month),
        random.randint(30, 3000),                    # duration
        random.randint(1, 50),                       # campaign
        random.randint(-1, 500),                     # pdays
        random.randint(0, 20),                       # previous
        random.choice(poutcome),
        random.choice(target)
    ]
    data.append(row)

columns = [
    "age", "job", "marital", "education", "default",
    "balance", "housing", "loan", "contact",
    "day", "month", "duration", "campaign",
    "pdays", "previous", "poutcome", "y"
]

df = pd.DataFrame(data, columns=columns)

# บันทึกแบบ UCI ใช้ ;
df.to_csv("data/bank-full.csv", sep=";", index=False)

print("สร้างไฟล์ data/bank-full.csv เรียบร้อย ✅")