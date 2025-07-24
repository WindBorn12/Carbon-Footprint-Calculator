from flask import Flask, request, render_template
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')  





@app.route('/hesapla', methods=['POST'])
def hesapla():
    
    elektrik = float(request.form['electricity'])
    gaz = float(request.form['gas'])
    su = float(request.form['water'])
    kirmiziet = float(request.form['redmeat'])
    beyazet = float(request.form['whitemeat'])
    kiyafet = float(request.form['cloth'])
    araba = request.form['car_type']
    arabakm = float(request.form['km'])

    elektrik_karbon = elektrikCo2(elektrikpara=elektrik)
    gaz_karbon = gazCo2(gaz_m3=gaz)
    su_karbon = suCo2(su_ton=su)
    kirmiziet_karbon = kirmiziEtCo2(kirmizi_et=kirmiziet)
    beyazet_karbon = beyazEtCo2(beyaz_et=beyazet)
    kiyafet_karbon = kiyafetCo2(kiyafet=kiyafet)
    araba_karbon = arabaCo2(araba_cesit=araba,arabakm=arabakm)

    tr_ort = {
    "Elektrik": 58,
    "Doğal Gaz": 50,
    "Su": 10,
    "Ulaşım": 112,
    "Kırmızı Et": 29,
    "Beyaz Et": 10,
    "Kıyafet": 15
    }

    emisyonlar = {
    "Elektrik": elektrik_karbon,
    "Doğal Gaz": gaz_karbon,
    "Su": su_karbon,
    "Ulaşım": araba_karbon,
    "Kırmızı Et": kirmiziet_karbon,
    "Beyaz Et": beyazet_karbon,
    "Kıyafet": kiyafet_karbon
    }

    oneriler = {
    "Elektrik": "Elektrik tüketimini azaltmak için tasarruflu cihazlar kullanabilirsin.",
    "Doğal Gaz": "Isı yalıtımı yaparak doğal gaz tüketimini azaltabilirsin.",
    "Su": "Daha az su harcamak için kısa duşlar alabilirsin.",
    "Ulaşım": "Araba yerine toplu taşıma veya bisiklet tercih edebilirsin.",
    "Kırmızı Et": "Kırmızı et yerine sebze ve baklagiller tüketebilirsin.",
    "Beyaz Et": "Haftalık et tüketimini biraz azaltmak faydalı olur.",
    "Kıyafet": "İkinci el alışverişi değerlendirebilirsin."
    }

    fark_atanlar = []
    for i in emisyonlar:
        if emisyonlar[i] > tr_ort[i]:
            fark_atanlar.append(oneriler[i])

    Toplam_karbon = ToplamCo2(elektrik=elektrik_karbon
                              ,gaz=gaz_karbon
                              ,su=su_karbon
                              ,araba=araba_karbon
                              ,kirmizi_et=kirmiziet_karbon
                              ,beyaz_et=beyazet_karbon
                              ,kiyafet=kiyafet_karbon)

    return render_template('result.html',Toplam_karbon=Toplam_karbon,
                                        elektrik_karbon=elektrik_karbon,
                                        gaz_karbon=gaz_karbon,
                                        su_karbon=su_karbon,
                                        kirmiziet_karbon=kirmiziet_karbon,
                                        beyazet_karbon=beyazet_karbon,
                                        kiyafet_karbon=kiyafet_karbon,
                                        araba_karbon=araba_karbon,
                                        oneriler=fark_atanlar)

if __name__ == '__main__':
    app.run(debug=True)