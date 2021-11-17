import sqlite3

conn = sqlite3.connect("prieglauda.db")
c = conn.cursor()


def findDogInformation(kailis, spalva, ugis, amzius, sterilizacija):
    kailisQueryPart = "" if "Nesvarbu" == kailis else "AND kailis= '{kailis}'".format(kailis=kailis)
    sterilizacijaQueryPart = "" if "Nesvarbu" == sterilizacija else "AND sterilizacija = '{sterilizacija}'".format(
        sterilizacija=sterilizacija)
    query = "SELECT vardas, link FROM Dog WHERE spalva='{spalva}' AND ugis='{ugis}' AND amzius='{amzius}' {kailis} {sterelizacija}".format(
        spalva=spalva, ugis=ugis, amzius=amzius, kailis=kailisQueryPart, sterelizacija=sterilizacijaQueryPart)
    c.execute(query)

    return c.fetchall()
