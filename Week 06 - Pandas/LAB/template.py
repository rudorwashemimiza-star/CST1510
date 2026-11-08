"""
RECORD CHECK  -  my version
===========================

Name  : Milcah R Musanhu
Lane  : IT      
Date  : 06 November 2026

Run it:   python template.py


"""
"""Imports pandas and matplotlib to display charts"""
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
Df = pd.read_csv("servers.csv")  
print(Df)


# ================================================================= PROCESS

Df["percent"] = (Df["used_gb"] / Df ["total_gb"]) *100 
"""Applies a condition to assign a status to each server"""
Df ["status"] = Df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90 
    else "OK"
)
# ================================================================== OUTPUT

print(Df)
print(Df[Df["status"] != "OK"])
print(Df.groupby("status").size())
Df.to_csv("servers_report.csv", index=False)

Df["status"].value_counts().plot(kind="bar")
plt.title("Status Counts")
plt.savefig("status_counts.png")
plt.show()


# ==========================================================================
