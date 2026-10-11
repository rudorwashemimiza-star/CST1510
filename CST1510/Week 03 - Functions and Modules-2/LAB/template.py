"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu 
Lane  : IT      
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS


def status_of(percent): 
    """Return the status for a given percentage"""
    if percent >= 100:
       
        return "OVER LIMIT"
    elif percent >= 90 :
        
        return "WARNING"
    else: 
        return "OK"


# ==================================================================== INPUT


hostname = input("Enter hostname:")   # replace with an input() call
value = float(input("Enter value:"))    # replace with an input() call, converted
limit = float(input("Enter limit:"))     # replace with an input() call, converted


# ================================================================== PROCESS


difference = value-limit   
percent    =  (value /limit) * 100      
status     = status_of (percent)          


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print("Hostname:", hostname)
print("Value:", value)
print("Limit:",limit)
print("Status:",status)
print("=" * 34)


# ==========================================================================
# 5. Before you finish:

