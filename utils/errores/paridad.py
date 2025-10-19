
def encodeParidad( char: str, par = True ) -> int:
    byte = ord(char)
    print( char + ': ' +  bin(byte) )
    bitAmount = 0
    for i in range(0,8):
        bitAmount += (byte >> i) & 1

    if not par:
        bitAmount += 1

    return (byte << 1) | (bitAmount % 2)

def detectarError( byte: int, par = True ) -> bool:
    bitAmount = 0
    for i in range(0,8):
        bitAmount += (byte >> i) & 1

    if not par:
        bitAmount += 1
        
    return (bitAmount % 2) == 0