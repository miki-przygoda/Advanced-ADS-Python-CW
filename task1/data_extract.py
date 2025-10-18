import sys, os, csv

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def _is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def read_csv_file():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'London_Underground_data.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, start=1):
                cells = [c.strip() for c in row]

                if not any(cells):
                    continue

                if 'StationRows' not in locals():
                    StationRows = []
                if 'EdgeRows' not in locals():
                    EdgeRows = []

                if len(cells) >= 2 and cells[1] != "":
                    line = cells[0] or "Missing Line"
                    station = cells[1]
                    if len(cells) < 4 or (len(cells) >= 4 and cells[2] == "" and (len(cells) < 4 or cells[3] == "")):
                        StationRows.append(["StationRow", line, station])
                        continue

                if len(cells) >= 4 and cells[1] != "" and cells[2] != "" and _is_number(cells[3]):
                    line = cells[0] or "Missing Line"
                    a, b, t = cells[1], cells[2], cells[3]
                    EdgeRows.append(["EdgeRow", line, a, b, t])
                    continue

    except Exception as e:
        print(e)

    return StationRows, EdgeRows