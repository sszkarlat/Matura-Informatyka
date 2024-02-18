def is_palindrome(x):
    return x == x[::-1]


with open("napisy.txt") as f:
    wiersze = f.read().splitlines()

slowo = ""
for wiersz in wiersze:
    if is_palindrome(wiersz + wiersz[0]):
        slowo += (wiersz + wiersz[0])[25]
    elif is_palindrome(wiersz[-1] + wiersz):
        slowo += (wiersz[-1] + wiersz)[25]

print(slowo)
