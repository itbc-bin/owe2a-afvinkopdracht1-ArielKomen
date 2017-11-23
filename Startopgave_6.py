
# Naam: Ariel Komen
# Datum: 18-10-2017 
# Versie: 1

#"/home/cole/Downloads/GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
#"/home/cole/Documents/course 1/fasta bestanden/gallus gallus eiwit.fasta"
#"/home/cole/Documents/course 1/fasta bestanden/genoom mus mus musculus.fasta"

def main():
    bestand = "/home/cole/Documents/course 1/fasta bestanden/genoom mus mus musculus.fasta"
    enzymen_bestand = ""
    try:
        enzymen_bestand = open ("/home/cole/Documents/course 2/afvinkopdrachten 2/enzymen.txt")
    except FileNotFoundError:
        print("het enzymenbestand is niet ingevoerd. Voer het enzymenbestand in!")
        
    enzymenlijst = []
    zoekwoord = ""
    sequentie = []
    for regel in enzymen_bestand:
        enzym, seq = regel.split()            
        seq = seq.replace("^","")
        seq = seq.replace("\n","")
        enzymenlijst.append(seq)
      
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    combi, bestand_gevonden = lees_inhoud(bestand)

    fastanummer = 0 # op welke positie zit het restricie-enzym? een tellertje die dat verteld
    teller = 0 # deze teller verteld uiteindelijk het totaal aantal hits

    if bestand_gevonden == True:
        if enzymen_bestand != "":
            zoekwoord = input("Geef een zoekwoord op: ")
    
    # Ga door alle fasta elementen heen
    
    for fasta in combi:
        fastanummer +=1
        # Kijk wat we hier hebben
        header = fasta[0]
        sequentie = "".join(fasta[1:])


        # Conditie 1: is de header okee?
        if header.find(zoekwoord) < 0:
            # Het zoekwoord zit niet in de header...
            continue

        # Conditie 2: Is dit dna??
        gevonden = is_dna(sequentie)
            
        if gevonden == True:
            # YES het is dna...

            # Conditie 3: knipt dit voor een restrictie-enzym?
            enzymen = knipt(sequentie, enzymenlijst)
            
            if enzymen != "":
                try:
                    print(fastanummer, header, enzymen)
                    teller += 1
                except KeyboardInterrupt:
                    print("\nje hebt het programma onderbroken!")
                    break
 
    gevonden = is_dna(sequentie)
    if zoekwoord != "":
        if teller == 0 and gevonden == True:
            print("er zijn geen hits, probeer het opnieuw met een ander zoekwoord dan:", zoekwoord)
        elif gevonden == True:    
            print("\nAlles is verwerkt, er zijn zoveel hits:", teller)
        elif gevonden == "DNA" or gevonden == "mRNA":
            print("je probeert een functie verkeerde inhoud te laten retourneren! Verander voor gewenste resultaat.")
        elif gevonden != True:
            print("het bestand is geen DNA bestand, geef een DNA bestand als invoer")
        
def lees_inhoud(bestands_naam):
    bestand_gevonden = True      
    # headers = []
    # seqs = []
    fasta = []
    combi = []
    try:
        
        for regel in open(bestands_naam):
            gestripte_regel = regel.strip()
            if gestripte_regel.startswith(">"):
                if fasta != []:
                    combi.append(fasta)

                fasta = []

            fasta.append(gestripte_regel)

        combi.append(fasta)
        
    except FileNotFoundError:
        print("het is niet het goede bestand of er is geen bestand.")
        bestand_gevonden = False
        #raise SystemExit
    return combi, bestand_gevonden

    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
   
    
def is_dna(sequentie):
    
    lengte = 0
    A_T_C_G = 0
    for regel in sequentie:
         lengte += len(regel.strip())
         
    for regel in sequentie:
        for letter in regel:
            if letter == "A":
                A_T_C_G +=  1
            if letter == "T":
                A_T_C_G +=  1
            if letter == "C":
                A_T_C_G +=  1
            if letter == "G":
                A_T_C_G +=  1
    """    
    if lengte == A_T_C_G:
        gevonden = "DNA"
    else:
        gevonden = "mRNA"
    """
    
    if lengte == A_T_C_G:
        gevonden = True
    else:
        gevonden = False

    return gevonden
    
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(sequentie, enzymenlijst):

    
    sEnzymen = ""
    for regel in enzymenlijst:
        #kijkt of iets in de sequentie zit        
        if regel in sequentie:
            sEnzymen += regel + " "
   
    #en als er een hit is, wordt het enzym door gestuurd naar de main() functie                                        
    return sEnzymen                                 
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
       
    
main()
