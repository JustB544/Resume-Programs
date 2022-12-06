import random
#program completed for a python class
class Superhero:
	def __init__(self, name  = "", Morality = 0, power = ""):
		self.name = name
		self.Morality = Morality
		self.power = power
		
	def addMorality(self, points):
		self.Morality = self.Morality + points
def main():
	name = input("What is your superhero's name? ")
	morality = input("What is your superhero's morality number? (positive = hero; negative = villain) ")
	power = input("What is your superhero's power? ")
	newSuperhero = Superhero(name, int(morality), power.lower())
	text = ""
	if newSuperhero.Morality < 0:
		text = "There was once a villain who towered over the land, and was willing to attack anyone that stood in their way. Their name was " + newSuperhero.name + ". They used their power of " + newSuperhero.power + " to conquer the land. On one particular occasion, " + newSuperhero.name + " was changed forever. "
	else:
		text = "There was once a hero who towered over the land, and was willing to attack any villain that stood in the way of justice. Their name was " + newSuperhero.name + ". They used their power of " + newSuperhero.power + " to protect the land. On one particular occasion, " + newSuperhero.name + " was changed forever. "
	oldMorality = newSuperhero.Morality
	newSuperhero.addMorality(random.randint(-2*abs(newSuperhero.Morality), 2*abs(newSuperhero.Morality)))
	if newSuperhero.Morality >= oldMorality and oldMorality < 0:
		text = text + "They felt different, less evil than before, "
		if newSuperhero.Morality >= 0:
			text = text + "some might say that they felt a new passion to protect, rather than to conquer. So from that day forward, " + newSuperhero.name + " vowed never to hurt another soul, and vowed to fix all their wrong doing. \n~The End~"
		else:
			text = text + "and some of their past decisions seemed to be too extreme for the new " + newSuperhero.name + ", so they decided to tone it down, and become less of villain than they were before as a result of this change. \n~The End~"
	elif newSuperhero.Morality >= oldMorality and oldMorality >= 0:
		text = text + "They felt better than before, and had gained a new passion for fighting evil, that they would end up using to do more for the world than ever before. \n~The End~"
	elif newSuperhero.Morality < oldMorality and oldMorality < 0:
		text = text + "They felt more evil than before, and began a master plan that would out surpass every other plan they had ever had in sheer evilness, and brilliance. This plan would come to fall into place, and began the new reign of terror for " + newSuperhero.name + ". \n~The End~"
	elif newSuperhero.Morality < oldMorality and oldMorality >= 0:
		text = text + "Their old actions began to seem more inconsequential"
		if newSuperhero.Morality >= 0:
			text = text + ", and what once had appeared to be a success filled future quickly fell into shambles. This led " + newSuperhero.name + " to retire early from fighting crime, and to live the rest of their life in the shadows outside of the public's view. \n~The End~"
		else:
			text = text + ", and they became sympathetic to the villains they once saw as evil and malicous. They soon began to turn on those that trusted them, and became just like the rest of the villains. " + newSuperhero.name + " had officially gone evil, and their was no turning back. \n ~The End~"
	print(text)
main()	
