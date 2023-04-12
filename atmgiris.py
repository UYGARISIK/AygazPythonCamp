kullanici_adi = "uygar"
parola = "4149"

input_data_username = input("Lütfen Kullanici adinizi giriniz : ")
input_data_password = input("Lütfen şifrenizi giriniz : ")

if kullanici_adi != input_data_username and parola == input_data_password:
    print ("Kullanici adiniz hatali,lütfen tekrar deneyiniz.")
elif kullanici_adi == input_data_username and parola != input_data_password:
    print ("şifreniz hatali,lütfen tekrar deneyiniz. ")
elif kullanici_adi != input_data_username and parola != input_data_password:
    print("Kullanici adiniz ve parolaniz hatali,lütfen tekrar deneyiniz")
else:
    print("Bankamiza hoşgeldiniz...")
