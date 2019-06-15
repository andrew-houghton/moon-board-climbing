import csv
import json


def main(year):
	with open(f'hold_positions_{year}.csv', newline='') as csvfile:
		rows = list(csv.reader(csvfile))

	hold_positions = {}
	for item in rows:
		try:
			hold_positions[(item[1][0], item[1][1:])]=item
		except:
			print(item)
			raise

	holds = []
	for r in range(18,0,-1):
		for c in [chr(i) for i in range(65,65+11)]:
			key = (c, str(r))
			if key in hold_positions:
				img_info = hold_positions[key]
				holds.append([
					f"h{img_info[0]}.png",
					f"{c}{r}",
					f"rot_{img_info[2]}"
					])
			else:
				holds.append(None)
	with open(f"holds_{year}.js", "w") as handle:
		handle.write(f"var holds_{year} = {json.dumps(holds)}")

main("2016")
main("2017")