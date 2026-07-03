import PI

def encrypt(text: str, key: str = "12345678") -> str :
    ascii_list = [ord(character) for character in text]
    
    bin_list = sum([bin(val) for val in ascii_list], [])

    pi_digits = [int(digit) for digit in PI.digits(num_digits=len(bin_list))]

    pi_added = [(pi + bin) for pi, bin in zip(pi_digits, bin_list)]

    
    
def decrypt(text: str, key: str = "12345678") -> str :
    ...

def bin(number: int) -> list[int] :
    bits = []
    tmp = number
    while len(bits) < 8 :
        bits.append(0 if tmp % 2 == 0 else 1)
        tmp //= 2

    return bits[::-1]

if __name__ == "__main__":
    print(bin(4))