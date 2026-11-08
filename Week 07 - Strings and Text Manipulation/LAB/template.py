"""
RECORD CHECK  -  my version
===========================

Name  :Milcah R Musanhu
Lane  : IT     
Date  :06 November 2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS
"""Cleans the messy server record using the parse_line function."""
def parse_line(raw_line):
    clean = raw_line.strip()
    hostname_part, rest = clean.split(",",1)
    hostname = hostname_part.strip().lower()

    fields = {}
    
    for part in rest.split(","):
        key, value = part.split("=")
        fields[key.strip().lower()] = float(value.strip())
    
    return{
           "hostname":hostname,
           "used"    :fields["used"],
           "total"   :fields["total"]
       }
"""Checks server percentage usage and returns its status"""
def status_of(used, total,warning =93):
    """Returns OVER LIMIT, WARNING and OK """

    percent = (used/total)*100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning:
        return "WARNING"
    else: 
        return "OK"
    

    

# ====================================================================== INPUT
"""Opens the file and reads all the records"""
with open("messy_lines.txt")as file:
       raw_records = file.readlines()

# =============================================================== PROCESS + OUTPUT
"""Counts all the records and flagged ones too"""
record_count = 0 
flagged_count = 0 
"""Processes each record and check its status"""
for raw_record in raw_records:
     record = parse_line(raw_record)
     status = status_of(record["used"], record["total"])
     print(record, status)
     record_count += 1

     if status != "OK":
          flagged_count += 1 
"""Prints the summary"""
print(f"Produced {record_count} records; {flagged_count} were flagged")


# ==========================================================================
