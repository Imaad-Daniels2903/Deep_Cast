import PI

def encrypt(text: str, key: str = "12345678") -> str :
    magic_key = [int(digit) for digit in list(key)]
    print("magic key  :", magic_key, "->", len(magic_key))
    print("sum        :", sum(magic_key))
    
    ascii_list = [ord(character) for character in text]
    print("ascii list :", ascii_list, "->", len(ascii_list))
    
    bin_list = sum([[a + b for a, b in zip(magic_key, bin(val))] for val in ascii_list], [])
    print("bin list   :", bin_list, "->", len(bin_list))

    pi_digits = [fib_list()[int(digit)] + int(digit) for digit in PI.digits(num_digits=len(bin_list))] 
    print("π          :", pi_digits, "->", len(pi_digits))

    pi_added = [(pi + bin) for pi, bin in zip(pi_digits, bin_list)]
    print("π added    :", pi_added, "->", len(pi_added))
    
    sum_magic = [chr((sum(magic_key) + digit) + 60) for digit in pi_added]
    print("sum magic  :", sum_magic, "->", len(sum_magic))
    
    return "".join([str(val) for val in sum_magic])

    
    
def decrypt(text: str, key: str = "12345678") -> str :      
    ...

def bin(number: int) -> list[int] :
    bits = []
    tmp = number
    while len(bits) < 8 :
        bits.append(0 if tmp % 2 == 0 else 1)
        tmp //= 2

    return bits[::-1]

def fib_list(n: int = 10) -> list[int] :
    sequence = [0, 1]
    while len(sequence) != n:
        sequence.append(sequence[-1] + sequence[-2])
        
    return sequence

if __name__ == "__main__":
    text = "Imaad"
    magic_key = "03291001"
    print("text:", text)
    encrypted_text = encrypt(text=text, key=magic_key)
    print(encrypted_text)
    