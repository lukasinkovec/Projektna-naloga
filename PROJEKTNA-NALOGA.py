import tkinter as tk


RAZMERJE_MAS = {
    ("lb", "kg"): 0.453592909436,
    ("t", "kg"): 1000,
    ("kg", "kg"): 1
}

RAZMERJE_DOLZIN = {
    ("in", "m"): 0.025399986284,
    ("ft", "m"): 0.304799990246,
    ("yd", "m"): 0.914402757839,
    ("mi", "m"): 1609.344497893,
    ("mm", "m"): 0.001,
    ("cm", "m"): 0.01,
    ("km", "m"): 1000,
    ("m", "m"): 1
}

RAZMERJE_PROSTORNIN = {
    ("gal", "l"): 3.785011355034,
    ("m3", "l"): 1000,
    ("l", "l"): 1
}


class PretvornikMasa:
    
    def __init__(self):
        self.masa = 1

    def nastavi_maso(self, masa):
        self.masa = masa


class PretvornikDolzina:
    
    def __init__(self):
        self.dolzina = 1

    def nastavi_dolzino(self, dolzina):
        self.dolzina = dolzina


class PretvornikProstornina:
    
    def __init__(self):
        self.prostornina = 1

    def nastavi_prostornino(self, prostornina):
        self.prostornina = prostornina

        

###############################################################################################################################################################################################################



class PretvornikVmesnik:


    def __init__(self):
        
        self.okno = tk.Tk()
        self.zgoraj = tk.Frame(self.okno)
        self.zgoraj.pack()
        self.sredina = tk.Frame(self.okno)
        self.sredina.pack()
        self.spodaj = tk.Frame(self.okno)
        self.spodaj.pack()
        
        self.pretvornik_masa = PretvornikMasa()
        self.pretvornik_dolzina = PretvornikDolzina()
        self.pretvornik_prostornina = PretvornikProstornina()

        self.vhod = tk.Entry(self.zgoraj)
        self.vhod.grid(row=0, column=0)
        self.napisana_enota1 = tk.StringVar()
        self.napisana_enota1.set("kg")
        self.enota1 = tk.Label(self.zgoraj, textvariable=self.napisana_enota1)
        self.enota1.grid(row=0, column=1)
        self.oznaka1 = tk.Label(self.zgoraj, text=" = ")
        self.oznaka1.grid(row=0, column=2)
        self.pretvorjena_vrednost = tk.StringVar()
        self.pretvorjena_vrednost.set("0.0")
        self.izhod = tk.Label(self.zgoraj, textvariable=self.pretvorjena_vrednost)
        self.izhod.grid(row=0, column=3)
        self.napisana_enota2 = tk.StringVar()
        self.napisana_enota2.set("kg")
        self.enota2 = tk.Label(self.zgoraj, textvariable=self.napisana_enota2)
        self.enota2.grid(row=0, column=4)
        gumb_pretvori = tk.Button(self.zgoraj, command=self.pretvori_vrednosti, text="Pretvori")
        gumb_pretvori.grid(row=0, column=5)

        self.napaka = tk.StringVar()
        self.napaka.set("")
        self.oznaka2 = tk.Label(self.sredina, textvariable=self.napaka)
        self.oznaka2.grid(row=0, sticky="we")
        
        oznaka_mase = tk.Label(self.spodaj, text="MASA")
        oznaka_mase.grid(row=0, column=0, sticky="w")
        gumb_funt = tk.Button(self.spodaj, command=self.naredi_funkcijo("lb"), text="Funt (lb)")
        gumb_funt.grid(row=1, column=0, sticky="we")
        gumb_kilogram = tk.Button(self.spodaj, command=self.naredi_funkcijo("kg"), text="Kilogram (kg)")
        gumb_kilogram.grid(row=1, column=1, sticky="we")
        gumb_tona = tk.Button(self.spodaj, command=self.naredi_funkcijo("t"), text="Tona (t)")
        gumb_tona.grid(row=1, column=2, sticky="we")

        prazen_prostor1 = tk.Label(self.spodaj, text="")
        prazen_prostor1.grid(row=2)
        
        oznaka_dolzine = tk.Label(self.spodaj, text="DOLŽINA")
        oznaka_dolzine.grid(row=3, column=0, sticky="w")
        gumb_palec = tk.Button(self.spodaj, command=self.naredi_funkcijo("in"), text="Palec (in)")
        gumb_palec.grid(row=4, column=0, sticky="we")
        gumb_cevelj = tk.Button(self.spodaj, command=self.naredi_funkcijo("ft"), text="Čevelj (ft)")
        gumb_cevelj.grid(row=4, column=1, sticky="we")
        gumb_jard = tk.Button(self.spodaj, command=self.naredi_funkcijo("yd"), text="Jard (yd)")
        gumb_jard.grid(row=4, column=2, sticky="we")
        gumb_milja = tk.Button(self.spodaj, command=self.naredi_funkcijo("mi"), text="Milja (mi)")
        gumb_milja.grid(row=4, column=3, sticky="we")
        gumb_milimeter = tk.Button(self.spodaj, command=self.naredi_funkcijo("mm"), text="   Milimeter (mm)   ")
        gumb_milimeter.grid(row=5, column=0, sticky="we")
        gumb_centimeter = tk.Button(self.spodaj, command=self.naredi_funkcijo("cm"), text="   Centimeter (cm)   ")
        gumb_centimeter.grid(row=5, column=1, sticky="we")
        gumb_meter = tk.Button(self.spodaj, command=self.naredi_funkcijo("m"), text="Meter (m)")
        gumb_meter.grid(row=5, column=2, sticky="we")
        gumb_kilometer = tk.Button(self.spodaj, command=self.naredi_funkcijo("km"), text="   Kilometer (km)   ")
        gumb_kilometer.grid(row=5, column=3, sticky="we")

        prazen_prostor2 = tk.Label(self.spodaj, text="")
        prazen_prostor2.grid(row=6)
        
        oznaka_prostornine = tk.Label(self.spodaj, text="PROSTORNINA")
        oznaka_prostornine.grid(row=7, column=0, sticky="w")
        gumb_galon = tk.Button(self.spodaj, command=self.naredi_funkcijo("gal"), text="Galon (gal)")
        gumb_galon.grid(row=8, column=0, sticky="we")
        gumb_liter = tk.Button(self.spodaj, command=self.naredi_funkcijo("l"), text="Liter (l)")
        gumb_liter.grid(row=8, column=1, sticky="we")
        gumb_kubicni_meter = tk.Button(self.spodaj, command=self.naredi_funkcijo("m3"), text=" Kubični meter (m3) ")
        gumb_kubicni_meter.grid(row=8, column=2, sticky="we")

        
    def naredi_funkcijo(self, enota):
        def funkcija():
            self.napisana_enota2.set(self.napisana_enota1.get())
            self.napisana_enota1.set(enota)
            return None
        return funkcija


    def pretvori_vrednosti(self):
        if self.preveri():
            if (self.napisana_enota1.get() in ["lb","kg","t"]) and (self.napisana_enota2.get() in ["lb","kg","t"]):
                self.pretvori_mase()
                self.pretvorjena_vrednost.set(self.pretvornik_masa.masa)
                self.napaka.set("")
            elif (self.napisana_enota1.get() in ["in","ft","yd","mi","mm","cm","m","km"]) and (self.napisana_enota2.get() in ["in","ft","yd","mi","mm","cm","m","km"]):
                self.pretvori_dolzine()
                self.pretvorjena_vrednost.set(self.pretvornik_dolzina.dolzina)
                self.napaka.set("")
            elif (self.napisana_enota1.get() in ["gal","l","m3"]) and (self.napisana_enota2.get() in ["gal","l","m3"]):
                self.pretvori_prostornine()
                self.pretvorjena_vrednost.set(self.pretvornik_prostornina.prostornina)
                self.napaka.set("")
            else:
                self.napaka.set("Enoti ne pripadata isti količini!")
        else:
            self.napaka.set("Vnesena vrednost ni število!")


    def pretvori_mase(self):
        vrednost = ((float(self.vhod.get()) * RAZMERJE_MAS[(self.napisana_enota1.get(), "kg")]) * (RAZMERJE_MAS[(self.napisana_enota2.get(), "kg")] ** -1))
        self.pretvornik_masa.nastavi_maso(round(vrednost, 4))


    def pretvori_dolzine(self):
        vrednost = ((float(self.vhod.get()) * RAZMERJE_DOLZIN[(self.napisana_enota1.get(), "m")]) * (RAZMERJE_DOLZIN[(self.napisana_enota2.get(), "m")] ** -1))
        self.pretvornik_dolzina.nastavi_dolzino(round(vrednost, 4))

        
    def pretvori_prostornine(self):
        vrednost = ((float(self.vhod.get()) * RAZMERJE_PROSTORNIN[(self.napisana_enota1.get(), "l")]) * (RAZMERJE_PROSTORNIN[(self.napisana_enota2.get(), "l")] ** -1))
        self.pretvornik_prostornina.nastavi_prostornino(round(vrednost, 4))


    def preveri(self):
        stevec = [1 for znak in self.vhod.get() if znak not in "0123456789.-"]
        minus = [1 for znak in self.vhod.get() if znak == "-"]
        pika = [1 for znak in self.vhod.get() if znak == "."]
        return (self.vhod.get() != "") and (len(stevec) == 0) and (len(minus) <= 1) and (len(pika) <= 1) and (len(minus) != 1 or self.vhod.get()[0] == "-") and (len(pika) != 1 or self.vhod.get()[0] != ".")
            
            
PretvornikVmesnik()
