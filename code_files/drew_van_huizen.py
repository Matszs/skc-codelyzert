# Studiecheck HVA Drew van Huizen
import datetime

# Vragen naam en geboortejaar.
naam = str(input("Hoe heet je?\n"))
geboortejaar = int(input("Wat is je geboortejaar?\n"))

# Berekening leeftijd en venusleeftijd
x = datetime.datetime.now()
huidigeJaar = int(x.year)
leeftijd = huidigeJaar - geboortejaar
venusLeeftijd = str(leeftijd / 0.62)

# Weergeven resultaat
print("\nBeste " + naam + ", in " + str(huidigeJaar) + " is je leeftijd " + str(leeftijd) + ".")
print("En je leeftijd is dan " + venusLeeftijd + " in Venusjaren.")