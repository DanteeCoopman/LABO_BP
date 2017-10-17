naam = input("Geef uw naam op: ")
voornaam = input("Geef uw voornaam op: ")
geboortedatum = input("Geef uw geboortedatum op (dd-mm-yyyy): ")

def genereer_paswoord(naam,voornaam,geboortedatum):
    naamformat = ''.join(naam.split()).lower()
    voornaamformat = ''.join(voornaam.split()).upper()
    geboortedatumformat = geboortedatum.replace("-","")
    naamdeel = naamformat[:3]
    voornaamdeel = voornaamformat[:2]
    geboortedatumdeel = geboortedatumformat[2:4] + geboortedatumformat[6:8]
    print(naamdeel + voornaamdeel + geboortedatumdeel)

genereer_paswoord(naam,voornaam,geboortedatum)
