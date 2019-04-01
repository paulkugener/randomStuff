import random, time

# https://www.wikiwand.com/en/Birthday_problem

class Group(object):
	def __init__(self, n):
		self.listOfBirthdays = list()
		for _ in range(n):
			self.listOfBirthdays.append(random.randint(1, 366))

	def sort(self):
		self.listOfBirthdays.sort()

	def print(self):
		print(*self.listOfBirthdays, sep = ", ")

	def has_duplicates(self):
		return len(self.listOfBirthdays) != len(set(self.listOfBirthdays))

	def print_duplicates(self):
		if self.has_duplicates() == False:
			print("no duplicates")
			return False
		listOfDuplicates = list()
		setOfBirthdays = set()
		for item in self.listOfBirthdays:
			if item in setOfBirthdays:
				listOfDuplicates.append(item)
				break
			else:
				setOfBirthdays.add(item)
		print(*listOfDuplicates, sep = ", ")


def main():
    # g = Group(23)
    # g.sort()
    # g.print()
    # g.has_duplicates()
    # g.print_duplicates()

    # do tests and print number of occasions with duplicates
    startTime = time.time()
    numberOfTests = 1_000_000
    numberOfPos = 0

    print("running {:,} tests...".format(numberOfTests))

    for _ in range(numberOfTests):
    	g = Group(23)
    	if g.has_duplicates():
    		numberOfPos = numberOfPos + 1

    print("numberOfPos = {:,}".format(numberOfPos))
    print("numberOfPos / {:,} = {:.4f}".format(numberOfTests, numberOfPos / numberOfTests))
    print("elapsed time = {:.2f} sec".format(time.time() - startTime))


if __name__ == '__main__':
    main()
