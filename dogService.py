import dogModel


def getDogInformation(searchProperties):
    kailis = searchProperties[0]
    spalva = searchProperties[1]
    ugis = searchProperties[2]
    amzius = searchProperties[3]
    sterilizacija = searchProperties[4]

    results = dogModel.findDogInformation(kailis, spalva, ugis, amzius, sterilizacija)
    return results
