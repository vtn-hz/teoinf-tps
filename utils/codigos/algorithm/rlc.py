
def rlc(message: str) -> list[tuple]:
    if not message:
        return []

    result = []
    symbol = message[0]
    amount = 1

    for ch in message[1:]:
        if ch == symbol:
            amount += 1
        else:
            result.append((symbol, amount))
            symbol = ch
            amount = 1

    result.append((symbol, amount))
    return result
