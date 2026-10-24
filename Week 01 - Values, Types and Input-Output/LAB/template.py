"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu
Lane  : IT     
Date  :04 October 

Run it:   python template.py

Calculates and displays the difference and percentage used through a record check report""" 

#Input
"""Takes the hostname,the amount of data used and the total data limit"""
hostname  = input("")
gb_used   = float(input())     
gb_total  = float(input())
user      = input("")  


#PROCESS
"""Calculates the difference between the amount used and the total limit
then calculates the percentage of the total limit that was used."""

free = gb_total - gb_used   
percent = gb_used / gb_total * 100     


#OUTPUT
"""Displays Record Check, the amount used,the total,the difference,the percentage, and the hostname"""

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"Used           :{gb_used:>10.2f}")
print(f"Total          :{gb_total:>10.2f}")
print(f"Free           :{free:>+10.2f}")
print(f"Percent        :{percent:>10.2f} %")
print(f"User           :{user:>10}")
#User displays the  name of the person who is inputting the data. 

print("=" * 34)


# ==========================================================================
