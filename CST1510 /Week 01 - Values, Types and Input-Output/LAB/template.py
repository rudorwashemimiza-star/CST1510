"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu
Lane  : IT     
Date  :04 October 

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
#Input
hostname = input("")
gb_used = float(input())     
gb_total = float(input())   


#PROCESS


difference = gb_used - gb_total   
percent = gb_used / gb_total * 100     


#OUTPUT


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"Used           :{gb_used:>10.0f}")
print(f"Total          :{gb_total:>10.0f}")
print(f"Difference     :{difference:>10.2f}")
print(f"Percent        :{percent:>10.2f}")
print(f"Host           :{hostname:>10}")

print("=" * 34)


# ==========================================================================
