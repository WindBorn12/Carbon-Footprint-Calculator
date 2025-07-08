import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP ayarları
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Gönderici bilgileri (Kendi e-posta adresini yaz)
GMAIL_USER = "windborn12@gmail.com"
GMAIL_PASSWORD = "zhpt mruy xhss crgt"  # Uygulama şifresini buraya gir

# Alıcı bilgileri

body = "Merhaba! Bu e-posta Python kullanılarak gönderildi."
def e_posta(receiver_email,subject):
    global GMAIL_USER,body
    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Güvenli bağlantı başlat
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        
        # E-postayı gönder
        server.sendmail(GMAIL_USER, receiver_email, msg.as_string())
        server.quit()
        
        print("✅ E-posta başarıyla gönderildi!")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
