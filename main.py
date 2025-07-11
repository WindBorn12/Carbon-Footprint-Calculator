from flask import Flask, request, render_template

app = Flask(__name__)

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

arabakm = int(input("ayda Araba ile kac km yol yapiyorsunuz"))
araba_cesit = input("dizelse 1, benzinse 2 lpg ise 3")
araba_karbon = 0

if araba_cesit == "1":
    araba_karbon = arabakm*0.239
elif araba_cesit == "2":
    araba_karbon = arabakm*0.270
else:
    araba_karbon = arabakm*0.220

kirmizi_et = int(input("aylik kirmizi et kg"))
beyaz_et = int(input("aylik beyaz et kg"))

kirmizi_et_karbon = kirmizi_et * 27
beyaz_et_karbon = beyaz_et * 6.9

kiyafet = int(input("aylik alinan kiyafet"))
kiyafet_karbon = kiyafet*25


toplam_karbon_kg = elektrik_karbon + gaz_karbon + su_karbon + araba_karbon + kirmizi_et_karbon + beyaz_et_karbon + kiyafet_karbon
ton_CO2_yillik = toplam_karbon_kg * 12 / 1000
print(ton_CO2_yillik)