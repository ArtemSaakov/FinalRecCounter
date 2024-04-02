# PSA counter for final rec .csv files

from pathlib import Path
import csv

data = []
while True:
	path = input("Drag file into window ")
	path = path.strip(''''"''')
	filepath = Path(path)
	try:
		with open(filepath, "r") as file_obj:
			reader = csv.DictReader(file_obj)
			for line in reader:
				data.append(line)
			break
	except:
		print("There was an issue reading the file—check the filepath and make sure it's .csv")
newDict = {}
while True:
	filterSelection = input("Do you want to show count of all coded pkgs at final rec, or only delivered? (type 'a' for all or 'd' for delivered): ").lower()
	if filterSelection == 'a':
		for d in data:
			if d["BLDG_ABBR"] == "ZANR" and d["PSA"] not in newDict.keys():
				newDict[d["PSA"]] = 1
			elif d["BLDG_ABBR"] == "ZANR" and d["PSA"] in newDict.keys():
				newDict[d["PSA"]] += 1
		break
	elif filterSelection == 'd':
		for d in data:
			if d["BLDG_ABBR"] == "ZANR" and d["PSA"] not in newDict.keys() and d["PACKAGE_STATUS"] == "0":
				newDict[d["PSA"]] = 1
			elif d["BLDG_ABBR"] == "ZANR" and d["PSA"] in newDict.keys() and d["PACKAGE_STATUS"] == "0":
				newDict[d["PSA"]] += 1
		break
	else:
		print("That ain't it")
newDict = dict(sorted(newDict.items()))
for entry in newDict.items():
    print(f"PSA: {entry[0]}, Number:  {entry[1]}")