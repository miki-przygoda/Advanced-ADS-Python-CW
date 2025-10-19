"""Mainly to be used for testing APIs and the data structures introduced by task1"""

from data_extract import read_csv_file
from module_wrapper import build_index_from_rows
from utils.data_api import init_index, is_operational, get_station_id, get_station_name
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

station_rows, edge_rows = read_csv_file()
hashtable, records_by_id = build_index_from_rows(station_rows, edge_rows)

print("Testing the data API:\n")
init_index()
stationName = "Victoria"
print(f"Is {stationName} operational: " + str(is_operational(stationName)))
sid = get_station_id("Oxford Circus")
print("Station name: " + str(get_station_name(sid)))
stationName = "HelloWorldStation"
print(f"Is {stationName} operational: " + str(is_operational(stationName)))


print("\nRecords by id:\n")
for record in records_by_id:
    print(str(record.id) + " " + str(record.name))