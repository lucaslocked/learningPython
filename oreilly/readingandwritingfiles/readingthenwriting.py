f = open('oreilly/readingandwritingfiles/nameandscores.txt', 'w+')

while True:
	participant = input('Participant Name > ')
	if participant == 'quit':
		print('Work Completed')
		break
	score = input('Score for ' + participant + ' > ')
	f.write(participant + ', ' + str(score) + '\n')

particpants = {}
for line in f:
	entry = line.strip().split(", ")
	score = entry[1]
	particpants[participant] = score
	print(participant + ': ' + score)


f.close()