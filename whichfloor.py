maximum_stories = 12;
work = input("On what floor of the building is your office?")
floor = int(work)
while floor > maximum_stories:
	print(str(floor)+" is greater than the amount of floors in the building. There are "+ str(maximum_stories) +" floors, please enter again.");
	work = input("On what floor of the building is your office?")
	floor = int(work);
print("Congratulations, "+str(floor)+" is a valid designation.")
