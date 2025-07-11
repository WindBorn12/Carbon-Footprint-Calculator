def elektrikCo2(elektrikpara):
    elektrikkwh = 0
    if elektrikpara <= 620:
        elektrikkwh = elektrikpara/2.59
    else:
        elektrikkwh = elektrikpara/3.89
    elektrik_karbon = elektrikkwh*0.475
    return elektrik_karbon
def gazCo2(gaz_m3):
    gaz_karbon = gaz_m3*2.0
    return gaz_karbon
def suCo2(su_ton):
    su_karbon = su_ton * 0.3
    return su_karbon
def arabaCo2(arabakm,araba_cesit):
    araba_karbon = 0

    if araba_cesit == "Benzinli":
        araba_karbon = arabakm*0.239
    elif araba_cesit == "Dizel":
        araba_karbon = arabakm*0.270
    elif araba_cesit == "LPG":
        araba_karbon = arabakm*0.220
    return araba_karbon
def kirmiziEtCo2(kirmizi_et):
    kirmizi_et_karbon = kirmizi_et * 27
    return kirmizi_et_karbon
def beyazEtCo2(beyaz_et):
    beyaz_et_karbon = beyaz_et * 6.9
    return beyaz_et_karbon
def kiyafetCo2(kiyafet):
    kiyafet_karbon = kiyafet*25
    return kiyafet_karbon



def ToplamCo2(elektrik,gaz,su,araba,kirmizi_et,beyaz_et,kiyafet):
    toplam_karbon_kg = elektrik + gaz + su + araba + kirmizi_et + beyaz_et + kiyafet

    ton_CO2_yillik = toplam_karbon_kg * 12 / 1000
    return ton_CO2_yillik