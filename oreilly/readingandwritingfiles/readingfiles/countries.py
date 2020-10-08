# Reading From Files
f = open("oreilly/readingandwritingfiles/readingfiles/countries.txt", "r")

countries = []

for line in f:
	line = line.strip()
	# print(line)
	countries.append(line)
# print(country_list)
print(len(countries))

for country in countries:
	if country[0] == 'T':
		print(country)


f.close()
