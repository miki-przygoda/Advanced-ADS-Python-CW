from data_extract import read_csv_file
from module_wrapper import build_index_from_rows

station_rows, edge_rows = read_csv_file()
hashtable, records_by_id = build_index_from_rows(station_rows, edge_rows)

for record in records_by_id:
    print(str(record.id) + " " + str(record.name))
