"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu
Lane  : IT      
Date  : 17/10/2026

Run it:   python template.py

Checks server storage records, calculate the usage , and prints a report for each server.
"""

# =================================================================== FUNCTIONS


def check_record(value, limit, warning_at=90):
    """Works out the difference, percentage and status for one record."""
    difference = value - limit
    percent    = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= warning_at:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(record_id, value, limit, difference, percent, status):
    """Prints one bordered report. Nothing is worked out in here - only shown."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record_id}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


# ====================================================================== Store
# This code stores the servers records in a list of dictionaries.
records = [{"label": "srv-01", "value": 87, "limit": 120} , 
           {"label": "srv-02", "value": 85, "limit": 120} , 
           {"label": "srv-03", "value": 125, "limit": 120}] 


# =============================================================== PROCESS + OUTPUT
# Goes through each server, checks its storage usage and prints the result.
for record in records: 
   label = record["label"]
   value = record["value"]
   limit = record["limit"]

   difference, percent, status = check_record(value,limit)
   print_report(label , value, limit, difference, percent, status)



# ==========================================================================
# 
