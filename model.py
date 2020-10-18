def obstoj_nicle(stopnje, interval): #interval je nujno zaprt interval, podan je kot seznam v nizu.
    #[a_0, a_1], [spodnja_meja, zgornja_meja]
    a = interval[0]
    b = interval[1]
    vrednost_sp_meja =  stopnje[0] + stopnje[1]*a
    vrednost_zg_meja = stopnje[0] + stopnje[1]*b
    if vrednost_sp_meja * vrednost_zg_meja <=0:
        return True #če je ničla v intervalu ali v krajjiščih intervala
    else:
        return False

def razpolovi_interval(interval):
    #vrne dva intervala
    a = interval[0]
    b = interval[1]
    c = (a+b)/2
    return [[a,c], [c,b]]

def ali_je_krajisce(stopnje, interval):
    a = interval[0]
    b = interval[1]
    if stopnje[0] + stopnje[1] * a == 0 or stopnje[0] + stopnje[1] * b == 0:
        return True
    else:
        return False

def vrni_niclo_krajisca(stopnje, interval):
    #funkcijo uporabim, ko že vem, da je krajišče ničla. Funkcija mi vrne to krajišče. 
    a = interval[0]
    b = interval[1]
    if stopnje[0] + stopnje[1] * a == 0:
        return a
    else:
        return b 

def vrni_interval_nicle(stopnje, interval):
    a = interval[0]
    b = interval[1]
    interval1 = razpolovi_interval([a,b])[0]
    interval2 = razpolovi_interval([a,b])[1]
    if obstoj_nicle(stopnje, interval1) == True:
        return interval1
    else:
        return interval2

def najdi_niclo(stopnje, interval, natancnost = 5):
    #funkcija vrne seznam intervalov, na katerih se dela bisekcija in oceno za ničlo
    seznam_intervalov= [interval]
    if obstoj_nicle(stopnje, interval) == True:
        if ali_je_krajisce(stopnje, interval):
            return [seznam_intervalov, vrni_niclo_krajisca(stopnje, interval)] #to je krajišče danega intervala in je hkrati ničla funkcije
        else:
            interval_nicle = vrni_interval_nicle(stopnje, interval)
            c = interval_nicle[0]
            d = interval_nicle[1]
            while True:
                seznam_intervalov.append([c,d])
                interval_nicle = vrni_interval_nicle(stopnje, [c,d])
                c = round(interval_nicle[0], natancnost)
                d = round(interval_nicle[1], natancnost)
                if ali_je_krajisce(stopnje, interval_nicle) == True:
                    return [seznam_intervalov, vrni_niclo_krajisca(stopnje, interval_nicle)]  


def pretvorba(niz):
    sez1 = list(niz.split(","))
    return [float(sez1[0].replace("[","")), float(sez1[1].replace("]",""))]


class Bisekcija_linearna_funkcija:
    def __init__(self,funkcija, interval, natancnost = 5):
        self.funkcija = funkcija
        self.interval = interval
        self.natancnost = natancnost

    def __repr__(self):
        return "Imamo funkcijo {0} + {1}x, za katero računamo ničle na intervalu {2} z natančnostjo {3}.".format(self.funkcija[0],self.funkcija[1], self.interval, self.natancnost)
    
    def obstaja_nicla_v_intervalu(self):
        return obstoj_nicle(self.funkcija, self.interval)

    def seznam_intervalov_bisekcije(self):
        if self.obstaja_nicla_v_intervalu() == False:
            return "V izbranem intervalu ta funkcija nima ničle."
        else:
            return najdi_niclo(self.funkcija, self.interval, self.natancnost)[0]
    
    def stevilo_korakov(self):
        return len(self.seznam_intervalov_bisekcije())

    def nicla_bisekcije(self):
        if self.obstaja_nicla_v_intervalu() == True:
            return najdi_niclo(self.funkcija, self.interval, self.natancnost)[1]
    
        
