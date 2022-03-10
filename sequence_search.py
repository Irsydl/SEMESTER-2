# Program Sequence Search Python

def linearSearch(array, n, x):

    # Melewati array secara berurutan
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = input("Masukkan kalimat: ")
list_of_letters = list(array)

x = input("Enter element: ")
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)


# Mendefinisikan fungsi baru bernama linearsearch
# Fungsi Melakukan perulangan dari 0 sampai panjang inputan variabel array
# Jika inputan variabel x terdapat di inputan variabel array
# Mengembalikan nilai i ke fungsi
# Jika tidak ada maka fungsi akan bernilai -1
# Nilai fungsi dimasukkan kedalam variabel result
# Jika variabel result bernilai -1 maka akan menampilkan output "Element not found"
# Jika variabel result tidak bernilai -1 maka akan menampilkan "Element found at index", dan nilai dari fungsi

# Sumber: https://www.programiz.com/dsa/linear-search