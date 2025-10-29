exec(open("./utils/canales/posteriori/entropy.py").read())
exec(open("./utils/canales/posteriori/probs.py").read())


def calculateHCanal( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0

    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item*calculateI(item)

    return result
