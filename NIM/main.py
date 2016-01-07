__author__ = 'Wesley'
import tkinter as tk
import random
 
class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(column = 0, row = 0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        fontSmall = ("Segoe UI Light", 14, "bold")
        fontBig = ("Segoe UI Light", 20, "bold")
        fontWin = ("Segoe UI Light", 24, "bold")

        global beurtVan
        beurtVan = random.randint(1, 2)
        global aantalOver
        aantalOver = 7

        global aantalOverLabel
        aantalOverLabel = tk.Label(self, text=str(aantalOver) + " stenen over", font=fontSmall)
        global beurtLabel
        beurtLabel = tk.Label(self, text= "Speler " + str(beurtVan)+ " is aan de beurt", font=fontSmall)
        global kannietLabel
        kannietLabel = tk.Label(self, text = "Dit is niet mogelijk", font=fontSmall)
        global gewonnenLabel
        gewonnenLabel = tk.Label(self, text= "", font=fontSmall)

        global pakEen
        pakEen = tk.Button(self, text="Pak 1 steen",command=lambda:minEen(), font=fontBig)
        global pakTwee
        pakTwee = tk.Button(self, text="Pak 2 stenen",command=lambda:minTwee(), font=fontBig)
        global nieuwPotjeButton
        nieuwPotjeButton = tk.Button(self, text="Nog een potje", command=lambda:nieuwPotje(), font=fontBig)

        beurtLabel.grid(column = 0, row = 0, columnspan = 1)
        aantalOverLabel.grid(column = 0, row = 1, columnspan = 1)
        pakEen.grid(column = 1, row = 3, sticky="W", columnspan = 2, rowspan = 2)
        pakTwee.grid(column = 3, row = 3, sticky="W", columnspan = 2, rowspan = 2)

        def minEen():
            global aantalOver
            global beurtVan
            global beurtLabel
            global kannietLabel
            global gewonnenLabel

            if(aantalOver == 0):
                pass
                kannietLabel.grid(column = 1, row = 5)

            elif(aantalOver == 1):
                aantalOver -= 1
                aantalOverLabel.configure(text = str(aantalOver) + " stenen over")
                #Messagebox gebruiker heeft gewonnen
                if(beurtVan == 1):
                    beurtVan = 2
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                    gewonnenLabel.configure(text = "SPELER 1 HEEFT GEWONNEN")
                elif(beurtVan == 2):
                    beurtVan = 1
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                    gewonnenLabel.configure(text = "SPELER 2 HEEFT GEWONNEN")
                gewonnenLabel.grid(column = 1, row = 6)
                nieuwPotjeButton.grid(column = 1, row = 7, sticky="W", columnspan = 2, rowspan = 2)


            else:
                aantalOver -= 1
                aantalOverLabel.configure(text = str(aantalOver) + " stenen over")
                #Messagebox gebruiker heeft gewonnen
                if(beurtVan == 1):
                    beurtVan = 2
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                elif(beurtVan == 2):
                    beurtVan = 1
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")


            aantalOverLabel.configure(text = str(aantalOver) + " stenen over")

        def minTwee():
            global aantalOver
            global beurtVan
            global beurtLabel
            global kannietLabel
            global gewonnenLabel

            if(aantalOver == 0):
                kannietLabel.grid(column = 1, row = 5)

            elif(aantalOver == 1):
                kannietLabel.grid(column = 1, row = 5)

            elif(aantalOver == 2):
                aantalOver -= 2

                if(beurtVan == 1):
                    beurtVan = 2
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                    gewonnenLabel.configure(text = "SPELER 2 HEEFT GEWONNEN")
                elif(beurtVan == 2):
                    beurtVan = 1
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                    gewonnenLabel.configure(text = "SPELER 2 HEEFT GEWONNEN")
                gewonnenLabel.grid(column = 1, row = 6)
                nieuwPotjeButton.grid(column = 3, row = 7, sticky="W", columnspan = 2, rowspan = 2)

                aantalOverLabel.configure(text = str(aantalOver) + " stenen over")


            else:
                aantalOver -= 2

                if(beurtVan == 1):
                    beurtVan = 2
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
                elif(beurtVan == 2):
                    beurtVan = 1
                    beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")

                aantalOverLabel.configure(text = str(aantalOver) + " stenen over")

        def nieuwPotje():
            global beurtVan
            global beurtLabel
            global aantalOver
            nieuwPotjeButton.grid_forget()
            gewonnenLabel.grid_forget()
            kannietLabel.grid_forget()

            beurtVan = random.randint(1, 2)
            beurtLabel.configure(text= "Speler " + str(beurtVan) + " is aan de beurt")
            aantalOver = 7
            aantalOverLabel.configure(text = str(aantalOver) + " stenen over")

if __name__ == "__main__":
    app = main()
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.geometry("%dx%d+0+0" % (w, h))
    app.mainloop()