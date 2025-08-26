import math 

class QuadratwurzelIterator:
  
    # Die magische Methode __init__()
    # Sie setzt den Start- und den Endwert
    def __init__(self, start, ende):
        self.wert = start
        self.ende = ende
    
    # Die magische Methode __iter__()
    # Sie liefert nur self zurück
    def __iter__(self):
        return self
    
    # Die magische Methode __next__()
    # Sie liefert den nächsten berechneten Wert
    def __next__(self):
        # Prüfen, ob das Ende noch nicht erreicht ist
        if self.wert <= self.ende:
            # Die Quadratwurzel des aktuellen Werts berechnen
            ergebnis = math.sqrt(self.wert)
            # Den Wert für den nächsten Durchlauf um 1 erhöhen
            self.wert = self.wert + 1
            return ergebnis
        # Sonst wird die Ausnahme StopIteration ausgelöst, um die Schleife zu beenden
        else:
            raise StopIteration

# Anwendung des Iterators 
print("Iterator für die Quadratwurzeln von 4 bis 9:")
# Eine Instanz des Iterators erstellen
mein_iterator = QuadratwurzelIterator(4, 9)

# Mit einer for-Schleife über den Iterator laufen
for wurzel in mein_iterator:
    print(wurzel)

