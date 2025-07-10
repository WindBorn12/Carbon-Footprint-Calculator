elektrikpara = int(input("aylik elektrik faturasi: "))
elektrikkwh = 0
if elektrikpara <= 620:
    elektrikkwh = elektrikpara/2.59
else:
    elektrikkwh = elektrikpara/3.89
elektrik_karbon = elektrikkwh*0.475

gaz_m3 = int(input("bir ayda kullandiginiz dogal gaz miktari: "))
gaz_karbon = gaz_m3*2.0

su_ton = int(input("aylik kullanilan su miktari: "))
su_karbon = su_ton * 0.3


