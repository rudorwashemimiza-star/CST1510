"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu 
Lane  :IT      
Date  :9 October 2026

Run it:   python template.py

Asks for a hostname, value, and limit, calculates the status, and prints the report.
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
#Asks the user for the hostname, value and limit

hostname  = input("Enter hostname:")  
value     = float(input("Enter value:"))    
limit     = float(input("Enter limit:"))     


# ================================================================== PROCESS
#Calculates. the difference, percentage and status

difference = value-limit   
percent    = (value /limit) * 100      
status     = status_of (percent)          


# =================================================================== OUTPUT
#Displays the record details and status
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"Hostname: {hostname:>10}")
print(f"Value:    {value:>10.2f}")
print(f"Limit:    {limit:>10.2f}")
print(f"Status:   {status:>10}")
print("=" * 34)


# ==========================================================================


