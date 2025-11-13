# parte 1

titolo_libro="Il Signore degli Anelli"
copie=10
prezzo=22.50
disponibile=True

print(f"Titolo: {titolo_libro}\nnumero di volumi: {copie}\nprezzo: {prezzo}\ndisponibile per L'acquisto: {disponibile}\n")

#parte 2

vetrina=["Il Signore degli Anelli","Harry Potter","Amleto","La Divina Commedia","Don Chisciotte"]
presenti={}
for x in vetrina:
    presenti.setdefault(x,copie)
utenti={"Martina","Luca","Carlotta","Lorenzo","Alessio","Ettore"}

#parte 3

class libro:
    def __init__(self,titolo,autore,anno,copie_disponibili):
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
        self.copie_disponibili=copie_disponibili
    def info(self):
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno: {self.anno}\nCopie disponibili: {self.copie_disponibili}\n"

print("--------------------------\n")

Signore_Anelli=libro("Il Signore degli Anelli","J.R.R.Tolkien",1954,presenti["Il Signore degli Anelli"])
print(Signore_Anelli.info())

class utente:
    def __init__(self,nome,età,id_utente):
        self.nome=nome
        self.età=età
        self.id_utente=id_utente
    def scheda(self):
        print(f"Nome: {self.nome}\nEtà: {self.età}\nId utente: {self.id_utente}\n")

print("--------------------------\n")

Luca=utente("Luca",25,"RSSLCU00G18P482S")
Luca.scheda()

class prestito(utente,libro):
    def __init__(self,utente,libro,giorni):
        self.utente=utente
        self.libro=libro
        self.giorni=giorni
    def dettagli(self):
        print(f"{self.libro.titolo}, prestato a {self.utente.nome} per un totale di {self.giorni} giorni\n")

print("--------------------------\n")

prestito1=prestito(Luca,Signore_Anelli,4)
prestito1.dettagli()

# parte 4

print("--------------------------\n")

class PrestitoImpossibile(Exception):
    pass


def presta_libro(utente,libro,giorni):
    if libro.titolo in presenti and presenti[libro.titolo]>0:
        presenti[libro.titolo]-=1
        libro.copie_disponibili-=1
        x=prestito(utente,libro,giorni)
        prestito.dettagli(x)
        print(f"Se ti interessa, possiedo anche:\n{presenti}\n")
    else:
        raise PrestitoImpossibile(f"Spiacente, non possiedo {libro.titolo}")

presenti["La Divina Commedia"]=0                    # per ottenere un messaggio di errore

presta_libro(Luca,Signore_Anelli,4)

Alessio=utente("Alessio",20,"VRDLSS05D24H501H")
Amleto=libro("Amleto","William Shakespeare",1600,presenti["Amleto"])
presta_libro(Alessio,Amleto,12)

Martina=utente("Martina",23,"PSSMRT02C71P408F")
Divina_Commedia=libro("La Divina Commedia","Dante Alighieri",1321,presenti["La Divina Commedia"])
presta_libro(Martina,Divina_Commedia,50)