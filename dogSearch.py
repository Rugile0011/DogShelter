import tkinter
from tkinter import *
import webbrowser
import dogService

root = tkinter.Tk()
root.title("Tavo draugas")
root.geometry("700x600")
root.config(background="#065569")
root.resizable(0, 0)

questions = [
    "Kailio tipas?",
    "Pagrindinė kailio spalva?",
    "Ūgio kategorija?",
    "Amžius?",
    "Sterilizacija/kastracija?",
]

answers_choice = [
    ["Trumpaplaukis", "Vidutinio ilgumo plaukas", "Nesvarbu"],
    ["Juoda/Ruda", "Pilka", "Juoda/Balta"],
    ["iki 30cm", "30-60cm", "daugiau nei 60cm"],
    ["iki 1 metų", "1-3 metai", "4-8 metai"],
    ["Atlikta", "Neatlikta", "Nesvarbu"],
]

questionNumber = 0
selectedData = []


def selected():
    global radiovar, r1, r2, r3, questionNumber, selectedData
    selectedValue = radiovar.get()
    selectedData.append(selectedValue)
    questionNumber += 1

    if questionNumber < 5:
        destroyPreviousQuestion()
        showQuestion()
    else:
        showAnswer(selectedData)


def destroyPreviousQuestion():
    global r1, r2, r3, labelQuestion
    r1.destroy()
    r2.destroy()
    r3.destroy()
    labelQuestion.destroy()


def Exit():
    Exit2["text"] = "Iki, geros dienos!"
    root.after(3000, lambda: root.destroy())


Exit2 = Label(root, text="", bg="#065569", fg="white", font=("Brush Script MT", 20))
Exit = Button(root, text="Iseiti", fg="white", bg="red", command=Exit)
Exit2.place(x=280, y=450)
Exit.place(x=340, y=500)


def showAnswer(selectedData):
    dogResults = dogService.getDogInformation(selectedData)
    r1.destroy()
    r2.destroy()
    r3.destroy()
    labelQuestion.destroy()

    if len(dogResults) != 0:
        ResultLabel = Label(root, text="JŪSŲ PASIRINKIMAS: ", bg="#065569", fg="white", font=("Consolas", 12))
        ResultLabel.pack(pady=(100, 30))

        for row in dogResults:
            name, link = row
            lbl = Label(root, text=name, bg="#065569", fg="white", font=("Consolas", 12))
            lbl.pack(pady=(10, 10))
            lbl.bind("<Button-1>", lambda e, url=link: webbrowser.open_new(url))
    else:
        ResultLabel2 = Label(root, text="Dėja, šiuo metu tokio pasirinkimo nėra, lauksime jūsų kitą kartą!",
                             bg="#065569", fg="white", font=("Consolas", 11))
        ResultLabel2.pack(pady=(100, 30))
        root.after(3000, lambda: root.destroy())


def startquiz():
    showQuestion()


def showQuestion():
    global labelQuestion, r1, r2, r3, radiovar
    labelQuestion = Label(
        root,
        text=questions[questionNumber],
        font=("Consolas", 15),
        width=500,
        justify="center",
        wraplength=400,
        background="#065569",
        fg="white"
    )
    labelQuestion.pack(pady=(100, 30))

    radiovar = StringVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[questionNumber][0],
        font=("Consolas", 10),
        value=answers_choice[questionNumber][0],
        variable=radiovar,
        command=selected,
        background="#065569",
        fg="white"
    )
    r1.pack(pady=3)

    r2 = Radiobutton(
        root,
        text=answers_choice[questionNumber][1],
        font=("Consolas", 10),
        value=answers_choice[questionNumber][1],
        variable=radiovar,
        command=selected,
        background="#065569",
        fg="white",
    )

    r2.pack(pady=3)

    r3 = Radiobutton(
        root,
        text=answers_choice[questionNumber][2],
        font=("Consolas", 10),
        value=answers_choice[questionNumber][2],
        variable=radiovar,
        command=selected,
        background="#065569",
        fg="white",
    )
    r3.pack(pady=3)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    startquiz()


img1 = PhotoImage(file="nuotrauka1.png")

labelimage = Label(
    root,
    image=img1,
    background="#065569",
)

labelimage.pack(pady=(70, 0))

labeltext = Label(
    root,
    text="SVEIKI!",
    bg="#065569",
    fg="white",
    font=("Adobe Arabic", 15)
)

labeltext.pack()

img2 = PhotoImage(file="Start-button3.png")
btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    bg="#065569",
    command=startIspressed
)

btnStart.pack(pady=(0, 75))

lblInstruction = Label(
    root,
    text="Tautmilės prieglauda - organizacija, kuri gelbėja beglobius gyvūnus, \njuos gydo, ieško mažyliams atsakingų ir mylinčių šeimininkų.",
    bg="#065569",
    fg="white",
    justify="center"
)

lblInstruction.pack(pady=(0, 20))

lblRules = Label(
    root,
    text="Programa sukurta tam, kad palengvintume jūsų paiešką rasti savo geriausią draugą!",
    width=100,
    bg="#065569",
    fg="white",
    font=("Adobe Arabic", 10),
    foreground="#008B8B",
    background="#8EE5EE"
)

lblRules.pack()

root.mainloop()
