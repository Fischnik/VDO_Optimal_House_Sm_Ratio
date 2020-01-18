CONST_HOUSE_FACTOR = 15 # Hausbaukostenfaktor
CONST_SM_COST_DEFAULT = 500 # Grundkosten erste SM (ohne Rassenbonus)
CONST_MAX_VALUE = 2000 # Maximale Dorfgröße, die beachtet werden soll
CONST_HOUSE_SIZE = 5 # Größe pro Haus

class Race:
    # Rassenbonus SM-Kosten (z.B. 1.4 = +40%)
    smCost_percent = 0
    # Rassenbonus SM-Kosten (z.B. 0.7 = -30%)
    houseCost_percent = 0

    # Konstruktor
    def __init__(self, smCost_percent, houseCost_percent):
        self.smCost_percent = smCost_percent
        self.houseCost_percent = houseCost_percent

    def calculateOptimum(self):
        currentSize = 5 # aktuelle Dorfgröße
        currentSM = 0 # Aktuelle Anzahl SM

        nextSM_cost = CONST_SM_COST_DEFAULT * self.smCost_percent # Kosten der nächsten SM
        while (currentSize <= CONST_MAX_VALUE):
            nextHouse_cost = self.getCostsForNextHouse(currentSize) # Kosten für das nächste Haus
            
            newSize = 0
            moneyToSpend = nextHouse_cost 
            while (moneyToSpend < nextSM_cost): # Wie viele Häuser könnte ich mit dem Geld bauen, die eine SM kostet?
                newSize += CONST_HOUSE_SIZE # Wie viel größer wird mein Dorf
                nextHouse_cost = self.getCostsForNextHouse(currentSize + newSize) # Kosten für das nächste Haus
                moneyToSpend += nextHouse_cost
            
            newIncomeHouse = (currentSize + newSize) * ((currentSM * 10) + 100) / 100 # Einkommen berechnen, wenn ich für das Geld nur Häuser kaufe
            newIncomeSM = currentSize * (((currentSM+1) * 10) + 100) / 100 # Einkommen berechnen, wenn ich für das Geld eine SM kaufe

            if(newIncomeHouse > newIncomeSM): 
                # Der Häuserbau bringt mehr Einkommen
                currentSize += newSize # Dorfgröße aktualisieren
            else: 
                # Eine SM bringt mehr Einkommen
                currentSM += 1 # Anzahl SM hochsetzen
                nextSM_cost *= 2 # Kosten für die nächste SM hochsetzen
                print("Dorfgröße:", currentSize, " => SM:" , currentSM) 
    
    def getCostsForNextHouse(self, currentSize):
        return currentSize * CONST_HOUSE_FACTOR * self.houseCost_percent

clan = Race(0.9, 0.7)
vamp = Race(1, 1)
elras = Race(1.4, 1)

print("### Clan ###")
clan.calculateOptimum()
print()
print("### Vamp ###")
vamp.calculateOptimum()
print()
print("### Elras ###")
elras.calculateOptimum()