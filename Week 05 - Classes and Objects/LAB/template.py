"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu 
Lane  : IT      
Date  : 23 October 2026

Run it:   python template.py

"""

# ====================================================================== CLASS
class Record: 
    over_limit_count = 0
   
    def __init__(self, label, value, limit):
        """Defines a function and assigns the attrribute to the object"""
        self.label = label
        self.value = value
        self.limit = limit 


    def percent(self):
         """Calculates the percent and returns the value"""
         return (self.value / self.limit) * 100  

    def status(self):

        """Determines the record status based of its calculated percentage """
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        
        else: 
            return "OK"







# ==================================================================== RECORDS

def load_records(path):
    """Obtains records from a file and returns them in a list"""
    records = []

    with open( path,"r") as file: 
        for line in file:
            split = line.strip().split(",")
            record = Record(split[0],float(split[1]), float(split[2]))
            records.append(record)
    return records
records = load_records("server_data.txt")




# ==================================================================== OUTPUT

over_limit_count = 0 
for record in records:

    if record.status() == "OVER LIMIT":
        over_limit_count += 1 
 
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"hostname :   {record.label}")
    print(f"GB used  :   {record.value}")
    print(f"GB total :   {record.limit}")
    print(f"Status   :   {record.status()}")

    print("=" * 34)

print(f"The total number of servers over limit:  {over_limit_count}")

   


# ==========================================================================
# 
