# Słownik związków chemicznych wraz z ich charakterem, typem i specyfikacją
zwiazki_chemiczne = {
    # Pierwiastki
    "Be": ("beryl","neutralny","metal"),
    "Na": ("sód", "neutralny", "metal"),
    "K": ("potas", "neutralny", "metal"),
    "Mg": ("magnez", "neutralny", "metal"),
    "Ca": ("wapń", "neutralny", "metal"),
    "Fe": ("żelazo", "neutralny", "metal"),
    "Zn": ("cynk", "amfoteryczny", "metal"),
    "Al": ("glin", "neutralny", "metal"),
    "Ag": ("srebro", "neutralny", "metal"),
    "Cu": ("miedź", "neutralny", "metal"),
    "O": ("tlen", "neutralny", "niemetal"),
    "H": ("wodór", "neutralny", "niemetal"),
    "C": ("węgiel", "neutralny", "niemetal"),
    "N": ("azot", "neutralny", "niemetal"),
    "S": ("siarka", "neutralny", "niemetal"),
    "Si": ("krzem", "neutralny", "niemetal"),
    "Mn": ("mangan", "neutralny", "metal"),
    "Cr": ("chrom", "neutralny", "metal"),
    "As": ("arsen", "neutralny", "niemetal"),
    "B": ("bor", "neutralny", "niemetal"),
    "P": ("fosfor", "neutralny", "niemetal"),
    "F": ("fluor", "neutralny", "niemetal"),
    "I": ("jod", "neutralny", "niemetal"),
    "Cl": ("chlor", "neutralny", "niemetal"),
    "Br": ("brom", "neutralny", "niemetal"),
    "Au": ("złoto","neutralny","metal"),
    "Ag": ("srebro","neutralne","metal"),
    "Hg": ("rtęć","neutralny","metal"),
    "Pb": ("ołów","neutralne","metal"),
    
    # Cząsteczki
    "H2": ("cząsteczka wodoru", "neutralny", "cząsteczka"),
    "O2": ("cząsteczka tlenu", "neutralny", "cząsteczka"),
    "F2": ("cząsteczka fluoru", "neutralny", "cząsteczka"),
    "Cl2": ("cząsteczka chloru", "neutralny", "cząsteczka"),
    "I2": ("cząsteczka jodu", "neutralny", "cząsteczka"),
    "Br2": ("cząsteczka bromu", "neutralny", "cząsteczka"),
    
    # Tlenki zasadowe
    "Na2O": ("tlenek sodu", "zasadowy", "tlenek"),
    "MgO": ("tlenek magnezu", "zasadowy", "tlenek"),
    "K2O": ("tlenek potasu", "zasadowy", "tlenek"),
    "CaO": ("tlenek wapnia", "zasadowy", "tlenek"),
    "CrO": ("tlenek chromu (II)", "zasadowy", "tlenek"),
    "MnO": ("tlenek manganu (II)", "zasadowy", "tlenek"),
    "Mn2O3": ("tlenek manganu (III)","zasadowy","tlenek"),
    
    # Tlenki kwasowe
    "CO2": ("tlenek węgla (IV)", "kwasowy", "tlenek"),
    "N2O3": ("tlenek azotu (III)", "kwasowy", "tlenek"),
    "N2O5": ("tlenek azotu (V)", "kwasowy", "tlenek"),
    "NO2": ("tlenek azotu (IV)", "kwasowy", "tlenek"),
    "SO2": ("tlenek siarki (IV)", "kwasowy", "tlenek"),
    "SO3": ("tlenek siarki (VI)", "kwasowy", "tlenek"),
    "B2O3": ("tlenek boru (III)", "kwasowy", "tlenek"),
    "P4O6": ("tlenek fosforu (III)", "kwasowy", "tlenek"),
    "P4O10": ("tlenek fosforu (V)", "kwasowy", "tlenek"),
    "Cl2O": ("tlenek chloru (I)", "kwasowy", "tlenek"),
    "Cl2O3": ("tlenek chloru (III)", "kwasowy", "tlenek"),
    "Cl2O5": ("tlenek chloru (V)", "kwasowy", "tlenek"),
    "Cl2O7": ("tlenek chloru (VII)", "kwasowy", "tlenek"),
    "CrO3": ("tlenek chromu (VI)", "kwasowy", "tlenek"),
    "Mn2O7": ("tlenek manganu (VII)", "kwasowy", "tlenek"),
    "MnO3": ("tlenek manganu (VI)", "kwasowy", "tlenek"),
    "SiO2": ("tlenek krzemu (IV)", "kwasowy", "tlenek"),
    "As2O5": ("tlenek arsenu (V)", "kwasowy", "tlenek"),
    
    # Tlenki amfoteryczne
    "BeO":("tlenek berylu","amfoteryczny","tlenek"),
    "ZnO": ("tlenek cynku", "amfoteryczny", "tlenek"),
    "Cr2O3": ("tlenek chromu (III)", "amfoteryczny", "tlenek"),
    "MnO2": ("tlenek manganu (IV)", "amfoteryczny", "tlenek"),
    "Al2O3": ("tlenek glinu", "amfoteryczny", "tlenek"),
    "H2O": ("woda", "amfoteryczny", "tlenek"),
    "As2O3": ("tlenek arsenu (III)", "amfoteryczny", "tlenek"),
    "CuO": ("tlenek miedzi (II)", "amfoteryczny", "tlenek"),
    "Fe2O3": ("tlenek żelaza (III)", "amfoteryczny", "tlenek"),
    "FeO": ("tlenek żelaza (II)", "amfoteryczny", "tlenek"),
    "Cu2O": ("tlenek miedzi (I)", "amfoteryczny", "tlenek"),
    
    # Tlenki obojętne
    "NO": ("tlenek azotu (II)", "obojętny", "tlenek"),
    "CO": ("tlenek węgla (II)", "obojętny", "tlenek"),
    "SiO": ("tlenek krzemu (II)", "obojętny", "tlenek"),
    "N2O": ("tlenek azotu (I)", "obojętny", "tlenek"),
    
    # Wodorotlenki zasadowe
    "LiOH" : ("wodorotlenek litu","zasadowy","wodorotlenek"),
    "NaOH": ("wodorotlenek sodu", "zasadowy", "wodorotlenek"),
    "KOH": ("wodorotlenek potasu", "zasadowy", "wodorotlenek"),
    "NH3*H2O": ("zasada amonowa", "zasadowy", "wodorotlenek"),
    "Ca(OH)2": ("wodorotlenek wapnia", "zasadowy", "wodorotlenek"),
    "Mg(OH)2": ("wodorotlenek magnezu", "zasadowy", "wodorotlenek"),
    "Cr(OH)2": ("wodorotlenek chromu (II)", "zasadowy", "wodorotlenek"),
    "Mn(OH)2": ("wodorotlenek manganu (II)", "zasadowy", "wodorotlenek"),
    
    # Wodorotlenki amfoteryczne
    "Be(OH)2":("wodorotlenek berylu","amfoteryczny","wodorotlenek"),
    "Al(OH)3": ("wodorotlenek glinu", "amfoteryczny", "wodorotlenek"),
    "Cu(OH)2": ("wodorotlenek miedzi (II)", "amfoteryczny", "wodorotlenek"),
    "Fe(OH)3": ("wodorotlenek żelaza (III)", "amfoteryczny", "wodorotlenek"),
    "Fe(OH)2": ("wodorotlenek żelaza (II)", "amfoteryczny", "wodorotlenek"),
    "Cr(OH)3": ("wodorotlenek chromu (III)", "amfoteryczny", "wodorotlenek"),
    "Zn(OH)2": ("wodorotlenek cynku (II)", "amfoteryczny", "wodorotlenek"),
    "Be(OH)2": ("wodorotlenek berylu (II)","amfoteryczny", "wodorotlenek"),
    
    # Kwasy beztlenowe
    "HCl": ("kwas chlorowodorowy (solny)", "kwasowy", "kwas beztlenowy"),
    "HF": ("kwas fluorowodorowy", "kwasowy", "kwas beztlenowy"),
    "HBr": ("kwas bromowodorowy", "kwasowy", "kwas beztlenowy"),
    "HI": ("kwas jodowodorowy", "kwasowy", "kwas beztlenowy"),
    "H2S":("kwas siarkowodorowy","kwasowy","kwas beztlenowy"),
    "HCN":("kwas cyjanowodorowy (pruski)","kwasowy","kwas beztlenowy"),
    
    # Kwasy tlenowe
    "H2CO3": ("kwas węglowy ", "kwasowy", "kwas tlenowy"),
    "HOCN":("kwas cyjanowy (piorunowy)","kwasowy","kwas tlenowy"),
    "HNO2": ("kwas azotowy (III)", "kwasowy", "kwas tlenowy"),
    "HNO3": ("kwas azotowy (V)", "kwasowy", "kwas tlenowy"),
    "H2SO3": ("kwas siarkowy (IV)", "kwasowy", "kwas tlenowy"),
    "H2SO4": ("kwas siarkowy (VI)", "kwasowy", "kwas tlenowy"),
    "H2S2O3": ("kwas tiosiarkowy", "kwasowy", "kwas tlenowy"),
    "H3BO3": ("kwas borowy (III)", "kwasowy", "kwas tlenowy"),
    "H3PO3": ("kwas fosforowy (III)", "kwasowy", "kwas tlenowy"),
    "HPO3": ("kwas metafosforowy", "kwasowy", "kwas tlenowy"),
    "H3PO4": ("kwas fosforowy (V)", "kwasowy", "kwas tlenowy"),
    "H4P2O7": ("kwas pirofosforowy", "kwasowy", "kwas tlenowy"),
    "HClO": ("kwas chlorowy (I)", "kwasowy", "kwas tlenowy"),
    "HClO2": ("kwas chlorowy (III)", "kwasowy", "kwas tlenowy"),
    "HClO3": ("kwas chlorowy (V)", "kwasowy", "kwas tlenowy"),
    "HClO4": ("kwas chlorowy (VII)", "kwasowy", "kwas tlenowy"),
    "H2CrO4": ("kwas chromowy (VI)", "kwasowy", "kwas tlenowy"),
    "H2Cr2O7": ("kwas dichromowy (VI)", "kwasowy", "kwas tlenowy"),
    "HMnO4": ("kwas manganowy (VII)", "kwasowy", "kwas tlenowy"),
    "H2MnO4": ("kwas manganowy (VI)", "kwasowy", "kwas tlenowy"),
    "H2SiO4": ("kwas metakrzemowy", "kwasowy", "kwas tlenowy"),
    "H4SiO4": ("kwas ortokrzemowy", "kwasowy", "kwas tlenowy"),
    "H3AsO3": ("kwas arsenowy (III)", "kwasowy", "kwas tlenowy"),
    "H3AsO4": ("kwas arsenowy (V)", "kwasowy", "kwas tlenowy"),
    "HCOOH":("kwas mrówkowy (metanowy)","kwasowy","kwas organiczny"),
    "CH3COOH":("kwas octowy (etanowy)","kwasowy","kwas organiczny"),
    
#Wodorki"
    "CH4":("metan","obojętny","wodorek"),
    "BeH2":("wodorek berylu","amfoteryczny","wodorek"),
    "PH3":("fosforowodór","kwasowy","wodorek"),
    "SiH4":("monosilan","obojętny","wodorek"),
    "BH3":("boran","kwasowy","wodorek"),
    "NH3":("amoniak","zasadowy","wodorek"),
    "HCl(g)":("chlorowodór","kwasowy","wodorek kwasowy"),
    "HF(g)":("fluorowodór","kwasowy","wodorek kwasowy"),
    "HI(g)":("jodowodór","kwasowy","wodorek kwasowy"),
    "HBr(g)":("bromowodór","kwasowy","wodorek kwasowy"),
    "H2S(g)":("siarkowodór","kwasowy","wodorek kwasowy"),
    "HCN(g)":("cyjonowodór","kwasowy","wodorek kwasowy"),
}
sole = {
    # Sole dla kwasów beztlenowych
    "LiCl" : ("chlorek litu","rozpuszczalna","sól"),
    "NaCl": ("chlorek sodu", "rozpuszczalna", "sól"),
    "KCl": ("chlorek potasu", "rozpuszczalna", "sól"),
    "NH4Cl" : ("chlorek amonu","rozpuszczalna","sól"),
    "CaCl2": ("chlorek wapnia", "rozpuszczalna", "sól"),
    "MgCl2": ("chlorek magnezu", "rozpuszczalna", "sól"),
    "FeCl2": ("chlorek żelaza (II)", "rozpuszczalna", "sól"),
    "FeCl3":("chlorek żelaza (III)","rozpuszczalna","sól"),
    "ZnCl2": ("chlorek cynku", "rozpuszczalna", "sól"),
    "AlCl3": ("chlorek glinu", "rozpuszczalna", "sól"),
    "AgCl": ("chlorek srebra", "nierozpuszczalna", "sól"),
    "CuCl": ("chlorek miedzi (I)", "nierozpuszczalna", "sól"),
    "CuCl2":("chlorek miedzi (II)","rozpuszczalna","sól"),
    "CrCl2":("chlorek chromu (II)","rozpuszczalna","sól"),
    "CrCl3": ("chlorek chromu (III)","rozpuszczalna","sól"),
    "MnCl2":("chlorek manganu (II)","rozpuszczalny","sól"),
    "BeCl2" : ("chlorek berylu","rozpuszczalny","sól"),
#sole Fluorkowe
    "NaF": ("fluorek sodu", "rozpuszczalna", "sól"),
    "LiF": ("fluorek litu","","sól"),
    "KF": ("fluorek potasu", "rozpuszczalna", "sól"),
    "NH4F":("fluorek amonu","rozpuszczalny","sól"),
    "CaF2": ("fluorek wapnia", "nierozpuszczalna", "sól"),
    "MgF2": ("fluorek magnezu", "nierozpuszczalna", "sól"),
    "FeF2": ("fluorek żelaza (II)", "nierozpuszczalna", "sól"),
    "CuF": ("fluorek miedzi (I)", "nierozpuszczalna", "sól"),
    "ZnF2": ("fluorek cynku", "nierozpuszczalna", "sól"),
    "CrF2":("fluorek chromu (II)","-","sól"),
    "MnF2":("fluorek manganu (II)","-" "sól"),
    "BeF2":("fluorek berylu","-" "sól"),
#sole Bromkowe
    "NaBr": ("bromek sodu", "rozpuszczalna", "sól"),
    "KBr": ("bromek potasu", "rozpuszczalna", "sól"),
    "CaBr2": ("bromek wapnia", "rozpuszczalna", "sól"),
    "MgBr2": ("bromek magnezu", "rozpuszczalna", "sól"),
    "FeBr2": ("bromek żelaza (II)", "rozpuszczalna", "sól"),
    "CuBr": ("bromek miedzi (I)", "nierozpuszczalna", "sól"),
#sole Jodkowe
    "NaI": ("jodek sodu", "rozpuszczalna", "sól"),
    "KI": ("jodek potasu", "rozpuszczalna", "sól"),
    "CaI2": ("jodek wapnia", "rozpuszczalna", "sól"),
    "MgI2": ("jodek magnezu", "rozpuszczalna", "sól"),
    "FeI2": ("jodek żelaza (II)", "rozpuszczalna", "sól"),
    "CuI": ("jodek miedzi (I)", "nierozpuszczalna", "sól"),
#sole siarczkowe
    "Na2S": ("siarczek sodu", "rozpuszczalna", "sól"),
    "K2S": ("siarczek potasu", "rozpuszczalna", "sól"),
    "CaS": ("siarczek wapnia", "nierozpuszczalna", "sól"),
    "MgS": ("siarczek magnezu", "mało rozpuszczalna", "sól"),
    "FeS": ("siarczek żelaza (II)", "nierozpuszczalna", "sól"),
    "Cu2S": ("siarczek miedzi (I)", "nierozpuszczalna", "sól"),

    # Sole dla kwasów tlenowych (przykłady)
    "Na2CO3": ("węglan sodu", "rozpuszczalna", "sól"),
    "(NH4)2CO3":("węglan amonu","rozpuszczalna","sól"),
    "K2CO3": ("węglan potasu", "rozpuszczalna", "sól"),
    "CaCO3": ("węglan wapnia", "nierozpuszczalna", "sól"),
    "MgCO3": ("węglan magnezu", "mało rozpuszczalna", "sól"),
    "FeCO3": ("węglan żelaza (II)", "nierozpuszczalna", "sól"),
    "Fe2(CO3)3":("węglan żelaza (III)","-","sól"),
    "Cu2CO3": ("węglan miedzi (I)", "nierozpuszczalna", "sól"),
    "CuCO3":("węglan miedzi (II)","-","sól"),
    "Ag2CO3":("węglan srebra","nierozpuszczalna","sól"),
    "Al2(CO3)3":("węglan glinu","-","sól"),
    "ZnCO3":("węglan cynku","nierozpuszczalna","sól"),

      "NaNO3": ("azotan (V) sodu", "rozpuszczalna", "sól"),
    "KNO3": ("azotan (V) potasu", "rozpuszczalna", "sól"),
    "Ca(NO3)2": ("azotan (V) wapnia", "rozpuszczalna", "sól"),
    "Mg(NO3)2": ("azotan (V) magnezu", "rozpuszczalna", "sól"),
    "Fe(NO3)2": ("azotan (V) żelaza (II)", "rozpuszczalna", "sól"),
    "Fe(NO3)3":("azotan (V) żelaza (II)","rozpuszczalna","sól"),
    "CuNO3": ("azotan (V) miedzi (I)", "rozpuszczalna", "sól"),

   # Sole dla kwasów tlenowych
    # Kwasy tlenowe - H2SO3 (kwas siarkowy IV)
    "Na2SO3": ("siarczyn sodu", "rozpuszczalna", "sól"),
    "K2SO3": ("siarczyn potasu", "rozpuszczalna", "sól"),
    "CaSO3": ("siarczyn wapnia", "mało rozpuszczalna", "sól"),
    "MgSO3": ("siarczyn magnezu", "mało rozpuszczalna", "sól"),
    "FeSO3": ("siarczyn żelaza (II)", "nierozpuszczalna", "sól"),
    "Cu2SO3": ("siarczyn miedzi (I)", "nierozpuszczalna", "sól"),

    # Kwasy tlenowe - H2SO4 (kwas siarkowy VI)
    "Na2SO4": ("siarczan (VI) sodu", "rozpuszczalna", "sól"),
    "K2SO4": ("siarczan (VI) potasu", "rozpuszczalna", "sól"),
    "CaSO4": ("siarczan (VI) wapnia", "mało rozpuszczalna", "sól"),
    "MgSO4": ("siarczan (VI) magnezu", "rozpuszczalna", "sól"),
    "FeSO4": ("siarczan (VI) żelaza (II)", "rozpuszczalna", "sól"),
    "CuSO4": ("siarczan (VI) miedzi (II)", "rozpuszczalna", "sól"),

    # Kwasy tlenowe - H3PO4 (kwas fosforowy V)
    "Na3PO4": ("fosforan (V) sodu", "rozpuszczalna", "sól"),
    "K3PO4": ("fosforan (V) potasu", "rozpuszczalna", "sól"),
    "Ca3(PO4)2": ("fosforan (V) wapnia", "nierozpuszczalna", "sól"),
    "Mg3(PO4)2": ("fosforan (V) magnezu", "nierozpuszczalna", "sól"),
    "Fe3(PO4)2": ("fosforan (V) żelaza (II)", "nierozpuszczalna", "sól"),
    "Cu3PO4": ("fosforan (V) miedzi (I)", "nierozpuszczalna", "sól"),

    # Kwasy tlenowe - HNO2 (kwas azotowy III)
    "NaNO2": ("azotan (III) sodu", "rozpuszczalna", "sól"),
    "KNO2": ("azotan (III) potasu", "rozpuszczalna", "sól"),
    "Ca(NO2)2": ("azotan (III) wapnia", "rozpuszczalna", "sól"),
    "Mg(NO2)2": ("azotan (III) magnezu", "rozpuszczalna", "sól"),
    "Fe(NO2)2": ("azotan (III) żelaza (II)", "rozpuszczalna", "sól"),
    "CuNO2": ("azotan (III) miedzi (I)", "rozpuszczalna", "sól"),

    # Kwasy tlenowe - HClO4 (kwas chlorowy VII)
    "NaClO4": ("chloran (VII) sodu", "rozpuszczalna", "sól"),
    "KClO4": ("chloran (VII) potasu", "rozpuszczalna", "sól"),
    "Ca(ClO4)2": ("chloran (VII) wapnia", "rozpuszczalna", "sól"),
    "Mg(ClO4)2": ("chloran (VII) magnezu", "rozpuszczalna", "sól"),
    "Fe(ClO4)2": ("chloran (VII) żelaza (II)", "rozpuszczalna", "sól"),
    "CuClO4": ("chloran (VII) miedzi (I)", "rozpuszczalna", "sól"),

    # Kwasy tlenowe - H2CrO4 (kwas chromowy VI)
    "Na2CrO4": ("chromian (VI) sodu", "rozpuszczalna", "sól"),
    "K2CrO4": ("chromian (VI) potasu", "rozpuszczalna", "sól"),
    "CaCrO4": ("chromian (VI) wapnia", "mało rozpuszczalna", "sól"),
    "MgCrO4": ("chromian (VI) magnezu", "rozpuszczalna", "sól"),
    "FeCrO4": ("chromian (VI) żelaza (II)", "nierozpuszczalna", "sól"),
    "Cu2CrO4": ("chromian (VI) miedzi (I)", "nierozpuszczalna", "sól"),
    "CuCrO4":("chromian (VI) miedzi (II)","nierozpuszczalna","sól"),

    # Kwasy tlenowe - H3BO3 (kwas borowy III)
    "Na3BO3": ("boran (III) sodu", "rozpuszczalna", "sól"),
    "K3BO3": ("boran (III) potasu", "rozpuszczalna", "sól"),
    "Ca(BO3)2": ("boran (III) wapnia", "nierozpuszczalna", "sól"),
    "Mg(BO3)2": ("boran (III) magnezu", "nierozpuszczalna", "sól"),
    "Fe3(BO3)2": ("boran (III) żelaza (II)", "nierozpuszczalna", "sól"),
    "Cu3BO3": ("boran (III) miedzi (I)", "nierozpuszczalna", "sól"),
    
    # Kwasy tlenowe - wodorosole
    "NaHCO3": ("wodorowęglan sodu","wodorosól","rozpuszczalna"),
    "KHCO3": ("wodorowęglan potasu","wodorosól","-"),
    "Mg(HCO3)2": ("wodorowęglan magnezu","wodorosól","-"),
    "Ca(HCO3)2": ("wodorowęglan wapnia","wodorosól","-"),
    "KH2PO4": ("diwodorofosforan potasu","wodorosól","-"),
    "K2HPO4": ("wodorofosforan potasu","wodorasól","-"),
    
}
def nazwa_i_charakter_zwiazku(wzor):
    # Najpierw sprawdzamy, czy wzór jest wśród soli
    if wzor in sole:
        nazwa, rozpuszczalnosc, typ = sole[wzor]
        return f"Substancja - {nazwa}\nRozpuszczalność - {rozpuszczalnosc}\nTyp substancji - {typ}"
    # Potem sprawdzamy inne związki (pierwiastki, tlenki, wodorotlenki, kwasy)
    zwiazek = zwiazki_chemiczne.get(wzor)
    if zwiazek:
        if len(zwiazek) == 3:
            nazwa, charakter, typ_substancji = zwiazek
            return f"Substancja - {nazwa}\nCharakter - {charakter}\nTyp substancji - {typ_substancji}"
        elif len(zwiazek) == 2:
            nazwa, typ_substancji = zwiazek
            return f"Substancja - {nazwa}\nTyp substancji - {typ_substancji}"
    return "Związek nieznany"
# Główna pętla programu
while True:
    wzor = input("Podaj wzór związku chemicznego (lub wpisz 'koniec' aby zakończyć): ")
    if wzor.lower() == "koniec":
        print("Koniec programu.")
        break
    print(nazwa_i_charakter_zwiazku(wzor))

