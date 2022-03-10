def shell_sort(my_list, list_len):
    
   interval = list_len // 2
   while interval > 0:
      for i in range(interval, list_len):
         temp = my_list[i]
         j = i
         while j >= interval and my_list[j - interval] > temp:
            my_list[j] = my_list[j - interval]
            j -= interval
         my_list[j] = temp
      interval //= 2

txt = input("Masukkan kalimat: ").lower()
my_list = txt.split()
list_len = len(my_list)

print ("\nsebelum melakukan shell sorting: ")
for i in my_list:
   print(i, end=' ')

print()

shell_sort(my_list, list_len)
print ("\nsetelah melakukan shell sorting: ")
for i in my_list:
   print(i, end=' ')

# Sebuah fungsi bernama 'shell_sort' didefinisikan, yang mengambil list, dan panjang list sebagai argumen.
# Variabel 'interval' didefinisikan, variabel ini mengambil panjang list dan membagi dengan 2
# Variabel 'interval' menggunakan floor division yang membulatkan bilangannya ke bilangan bulat terdekat ke bawah
# Melakukan looping kepada list dan membuat variabel sementara 'temp'
# Variabel 'interval' dibandingkan dengan setiap indeks list, dan setiap elemen dalam list dibandingkan dengan variabel sementara 'temp'.
# Variabel 'interval' sekali lagi digunakan untuk melakukan floor division.
# Fungsi dipanggil dengan memasukkan list dan panjang list sebagai parameter
# Output ditampilkan

# Sumber : https://www.tutorialspoint.com/python-program-to-implement-shell-sort