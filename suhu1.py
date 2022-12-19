print("Program Conversi Suhu")

input_celcius=input("masukkan suhu celcius : ")

if(type(input_celcius) == str):
    print("tolong masukkan inputan berupa angka")
else:
 hasil_farenheit =int(input_celcius)*9/5+32
 print("hsasilnya adalah", hasil_farenheit)
