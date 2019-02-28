# Dan eldad Is the best gever

# Sanity check:
# 1. Lines of presentation match the first line
# 2. each photo apears only once
# 3. each row has 1 or two numbers
# 4. there are rows with two numbers


photos = set()

with open ("final.sol", 'r') as file:
	number = int(file.readline())
	counter = 0
	found_verticals = False
	for line in file.readlines():
		cur_line = line.split()
		line_len = len(cur_line)
		if line_len > 2:
			print ("found line with {0} numbers (line number: {1})".format(line_len, counter))

		if line_len == 2:
			found_verticals = True

		for photo in cur_line:
			if photo in photos:
				print("found duplicated picture {0}".format(photo))
			else:
				photos.add(photo)
		counter += 1

	if counter != number:
		print("number of photos do not match {0} != {1}".format(number, counter))