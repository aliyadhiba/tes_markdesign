def can_form_word(array, target):
    # Membuat dictionary untuk menyimpan frekuensi huruf
    letter_count = {}
    
    # Menghitung frekuensi huruf dalam array
    for letter in array:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    # Memeriksa setiap huruf dalam target
    for letter in target:
        if letter in letter_count and letter_count[letter] > 0:
            letter_count[letter] -= 1  # Mengurangi jumlah huruf yang tersedia
        else:
            return False  # Huruf tidak cukup atau tidak ada
    
    return True  # Semua huruf dalam target dapat dibentuk

# Contoh penggunaan
input_array1 = ['e', 'd', 'o', 'c', 't']
target1 = "code"
output1 = can_form_word(input_array1, target1)
print(output1)  # Output: True

input_array2 = ['e', 'e', 'o', 'c']
target2 = "code"
output2 = can_form_word(input_array2, target2)
print(output2)  # Output: False
