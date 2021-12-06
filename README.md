# GyvunuPrieglauda
Programėlė, kuri padeda išsirinkti augintinį.
Naudojimas: atsisiųsti db failą ir įsikėlus kodą į Python pasileisti programą.
Duomenų bazėje, kurią kuriau su DB Browser for SQLite, suvestos galimos gyvūnų savybės. Kiekvienas gyvūnas turi nuorodą, kuri nukreipia į detalesnę informaciją. DogModel python failas sujungia programą su duomenų baze ir atpažįsta vartotojo pasirinkimus. Sterilizaciajos bei kailio pasirinkimas išskirtas, nes šių aspektų galima nepaisyti paspaudžiant "nesvarbu", tad programa sugeneruoja daugiau rezultatų neatsižvelgiant į sterilizaciją ar kailio tipą. 
DogService importuoju DogModel ir fiksuoju, koks buvo vartotojo pasirinkimas.
DogSearh faile kuriu grafinę dalį, pateikiu klausimus ir atsakymus, programuoju sklandų savybių pasirinkimą ir rezultato atidavimą.
