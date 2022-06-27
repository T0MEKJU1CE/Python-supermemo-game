import random
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

"""Plik w którym mają być słówka musi wyglądać tak:
słowo polskie-słowo niemieckie
np
artysta-der Kunstler
robić-machen
"""

słownik = {}
przystanek = "-"
klucz_wartość_czysty = ""
with open("Czysty słownik.txt", encoding='utf-8') as file:
    for line in file:
        for string in line:
            litera = string
            if litera != przystanek:
                klucz_wartość_czysty += litera
            else:
                klucz_czysty = klucz_wartość_czysty
                klucz_wartość_czysty = ""
        wartość_czysty = klucz_wartość_czysty.rstrip("\n") # czyszczenie z \n po wartościach
        słownik[klucz_czysty] = wartość_czysty
        klucz_wartość_czysty = ""

lista_kluczy = list(słownik)
random.shuffle(lista_kluczy)  #""" Jeśli się zrobi ostatnie źle to przy powtórce nie działa 🥴 """


class Application(Frame):
    """ Aplikacja do powtarzania słówek : - DDD"""
    licznik_słów = 0
    ilość_tłumaczenie = 0
    ilość_dalej = 0
    dobrze = 0
    średnio = 0
    źle = 0
    długość = len(lista_kluczy)
    ilość_słów_w_sesji = len(lista_kluczy)
    powtórka = False

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Widżety text button text button"""
        # kolumna 1


        self.row1 = Label(self, text=" ", width=1, height=1)
        self.row1.grid(row=1, column=0, sticky=W)

        self.row3 = Label(self, text=" ", width=30, height=5)
        self.row3.grid(row=3, column=0, sticky=W)

        self.dalej_tekst = Text(self, width=20, height=1, wrap=WORD)
        self.dalej_tekst.grid(row=0, column=1, sticky=W)

        self.pokaż_odp_tekst = Text(self, width=20, height=1, wrap=WORD)
        self.pokaż_odp_tekst.grid(row=2, column=1, sticky=W)

        self.dalej_bttn = ttk.Button(self, text="Nauka", command=self.dalej)
        self.dalej_bttn.grid(row=3, column=0, sticky=W)

        self.pokaż_odp_bttn = ttk.Button(self, text="Pokaż odpowiedź", command=self.pokaż_odp)
        self.pokaż_odp_bttn.grid(row=3, column=0, sticky=E)
        self.pokaż_odp_bttn["state"] = DISABLED

        self.licznik_label = Label(self, text="Słowo {}/{}".format(self.ilość_dalej, len(słownik)), width=9, height=1)
        self.licznik_label.grid(row=5, column=0, sticky=W)

        self.dobrze_bttn = ttk.Button(self, text="Dobrze", command=self.dobrze_odp, state=DISABLED)
        self.dobrze_bttn.grid(row=3, column=3, sticky=W)

        self.średnio_bttn = ttk.Button(self, text="Średnio", command=self.średnio_odp,state=DISABLED)
        self.średnio_bttn.grid(row=3, column=4,)

        self.źle_bttn = ttk.Button(self, text="Źle", command=self.źle_odp,state=DISABLED)
        self.źle_bttn.grid(row=3, column=5, sticky=W)

        self.licznik_dśź_label = ttk.Label(self, text="Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle))
        self.licznik_dśź_label.grid(row=6, column=0, sticky=W)

        # canvas
        self.progress_height = 20
        self.progress_width = 150
        self.progress_bar = Canvas(self, width=self.progress_width, height=self.progress_height, bg='white')
        self.progress_bar.grid(row=7, column=0, sticky=W)
        # self.progress_bar.create_rectangle(x1, y1, x2, y2, fill='blue')

    def dalej(self):
        self.pokaż_odp_tekst.delete(0.0, END)
        if self.licznik_słów < self.ilość_słów_w_sesji:
            słowo = lista_kluczy[self.ilość_dalej]
        elif not lista_kluczy:
            self.dalej_tekst.delete(0.0, END)
            koniec = tkinter.messagebox.showinfo("Koniec", "Koniec nauki!")
            root.destroy()
        elif self.powtórka == 'yes':
            self.dalej_tekst.delete(0.0, END)
            self.powtarzanie_dalej()
            return
        else:
            self.powtórka = True
            self.dalej_tekst.delete(0.0, END)
            self.pytanie_powtórka()
            return

        self.dalej_tekst.delete(0.0, END)
        self.dalej_tekst.insert(0.0, słowo)
        self.ilość_dalej += 1
        self.licznik_słów += 1
        self.dalej_bttn["text"] = "Dalej"
        self.licznik_label["text"] = "Słowo {}/{}".format(self.licznik_słów, self.ilość_słów_w_sesji)
        # wyłączenie przycisku dalej
        self.dalej_bttn["state"] = DISABLED
        # włączenie przycisku tłumaczącego
        self.pokaż_odp_bttn["state"] = NORMAL
        # wyłączenie przycisków dobrze średnio źle
        self.dobrze_bttn["state"] = DISABLED
        self.średnio_bttn["state"] = DISABLED
        self.źle_bttn["state"] = DISABLED
        # zawsze sprawdzenie długości
        self.długość = len(lista_kluczy)
        """
        print("Słownik: {}".format(słownik))
        print("Lista kluczy: {}".format(lista_kluczy))
        print("self.ilość_dalej: {}".format(self.ilość_dalej))
        print("self.ilość_tłumaczenie: {}".format(self.ilość_tłumaczenie))
        """

    def pokaż_odp(self):
        """ """
        """
        print("Na pokaż odp")
        print("Słownik: {}".format(słownik))
        print("Lista kluczy: {}".format(lista_kluczy))
        print("self.ilość_dalej: {}".format(self.ilość_dalej))
        print("self.ilość_tłumaczenie: {}".format(self.ilość_tłumaczenie))
        print(słownik[lista_kluczy[self.ilość_tłumaczenie]])
        """
        sorted(słownik.items(), key=lambda pair: lista_kluczy.index(pair[0]))
        słowo = słownik[lista_kluczy[self.ilość_tłumaczenie]]
        self.pokaż_odp_tekst.delete(0.0, END)
        self.pokaż_odp_tekst.insert(0.0, słowo)
        self.ilość_tłumaczenie += 1
        self.pokaż_odp_bttn["text"] = "Pokaż odpowiedź"
        # wyłączenie przycisku tłumaczącego
        self.pokaż_odp_bttn["state"] = DISABLED
        # włączenie przycisków dobrze średnio źle
        self.dobrze_bttn["state"] = NORMAL
        self.średnio_bttn["state"] = NORMAL
        self.źle_bttn["state"] = NORMAL

    def dobrze_odp(self):
        self.dobrze_bttn["state"] = DISABLED
        self.średnio_bttn["state"] = DISABLED
        self.źle_bttn["state"] = DISABLED
        self.dobrze += 1
        self.licznik_dśź_label["text"] = "Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle)
        del słownik[lista_kluczy[self.ilość_tłumaczenie - 1]]  # usunięcie dobrze powiedzianego słowa z późniejszych powtórek
                                                                     # - 1 bo self.i.t jest już zwiększone o 1 przez funckję pokaż_odp
        lista_kluczy.pop(self.ilość_tłumaczenie - 1)
        self.ilość_dalej -= 1
        self.ilość_tłumaczenie -= 1
        # włączenie przycisku dalej
        self.dalej_bttn["state"] = NORMAL
        # zawsze sprawdzenie długości
        self.długość = len(lista_kluczy)
        # canvas
        self.progress_bar.create_rectangle((self.dobrze - 1) * self.progress_width / self.ilość_słów_w_sesji, 0,
                                           (self.dobrze) * self.progress_width / self.ilość_słów_w_sesji,
                                           self.progress_height,
                                           fill='#0000c7', outline='#0000c7')
        for i in range(0, self.średnio + self.źle):
            self.progress_bar.create_rectangle((self.dobrze + i) * self.progress_width / self.ilość_słów_w_sesji,
                                               0,
                                               (self.dobrze + i + 1) * self.progress_width / self.ilość_słów_w_sesji,
                                               self.progress_height,
                                               fill='#f70000', outline='#f70000')

    def średnio_odp(self):
        self.dobrze_bttn["state"] = DISABLED
        self.średnio_bttn["state"] = DISABLED
        self.źle_bttn["state"] = DISABLED
        self.średnio += 1
        self.licznik_dśź_label["text"] = "Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle)
        self.dalej_bttn["state"] = NORMAL
        # canvas
        for i in range(0, self.średnio + self.źle):
            self.progress_bar.create_rectangle((self.dobrze + i) * self.progress_width / self.ilość_słów_w_sesji,
                                               0,
                                               (self.dobrze + i + 1) * self.progress_width / self.ilość_słów_w_sesji,
                                               self.progress_height,
                                               fill='#f70000', outline='#f70000')

    def źle_odp(self):
        self.dobrze_bttn["state"] = DISABLED
        self.średnio_bttn["state"] = DISABLED
        self.źle_bttn["state"] = DISABLED
        self.źle += 1
        self.licznik_dśź_label["text"] = "Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle)
        self.dalej_bttn["state"] = NORMAL
        # canvas
        for i in range(0, self.średnio + self.źle):
            self.progress_bar.create_rectangle((self.dobrze + i) * self.progress_width / self.ilość_słów_w_sesji,
                                               0,
                                               (self.dobrze + i + 1) * self.progress_width / self.ilość_słów_w_sesji,
                                               self.progress_height,
                                               fill='#f70000', outline='#f70000')

    def pytanie_powtórka(self):
        self.powtórka = tkinter.messagebox.askquestion(title="Niemiecki słówka" , message="Czy chcesz powtarzać dalej?")
        if self.powtórka == 'yes':
            self.powtarzanie_dalej()
        elif self.powtórka == 'no':
            root.destroy()


    def powtarzanie_dalej(self):
        self.licznik_słów = 1
        self.ilość_dalej = 0
        self.ilość_tłumaczenie = 0
        self.dobrze = 0
        self.średnio = 0
        self.źle = 0
        lista_kluczy = list(słownik)
        self.długość = len(lista_kluczy)
        self.ilość_słów_w_sesji = len(lista_kluczy)
        self.licznik_label["text"] = "Słowo {}/{}".format(self.licznik_słów, self.ilość_słów_w_sesji)
        # wyłączenie dalej i włączenie pokaż_odp
        self.dalej_bttn["state"] = DISABLED
        self.pokaż_odp_bttn["state"] = NORMAL
        # canva clear
        self.progress_bar.delete('all')

        # sortowanie żeby słownik był zgodny z listą_kluczy
        sorted(słownik.items(), key=lambda pair: lista_kluczy.index(pair[0]))

        # to co robi normalnie funkcja dalej() ale nie jest teraz wywoływana
        słowo = lista_kluczy[self.ilość_dalej]
        self.dalej_tekst.delete(0.0, END)
        self.dalej_tekst.insert(0.0, słowo)
        self.ilość_dalej += 1
        self.dalej_bttn["text"] = "Dalej"
        self.licznik_label["text"] = "Słowo {}/{}".format(self.licznik_słów, self.ilość_słów_w_sesji)
        self.licznik_dśź_label["text"] = "Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle)

        # zmiana dobrze() na dobrze_powtórka()
        self.dobrze_bttn["command"] = self.dobrze_powtórka
        self.pokaż_odp_bttn["command"] = self.ostatnie_źle

        print("Słownik: {}".format(słownik))
        print("Lista kluczy: {}".format(lista_kluczy))
        print("self.ilość_dalej: {}".format(self.ilość_dalej))
        print("self.ilość_tłumaczenie: {}".format(self.ilość_tłumaczenie))
        print(słownik[lista_kluczy[self.ilość_tłumaczenie]])


    # robię nowe funkcje dobrze do powtórek
    def dobrze_powtórka(self):
        self.dobrze_bttn["state"] = DISABLED
        self.średnio_bttn["state"] = DISABLED
        self.źle_bttn["state"] = DISABLED
        self.dobrze += 1
        self.licznik_dśź_label["text"] = "Dobrze {} Średnio {} Źle {}".format(self.dobrze, self.średnio, self.źle)
        del słownik[lista_kluczy[self.ilość_tłumaczenie - 1]]
        lista_kluczy.pop(self.ilość_tłumaczenie - 1)
        self.ilość_dalej -= 1
        self.ilość_tłumaczenie -= 1
        # włączenie przycisku dalej
        self.dalej_bttn["state"] = NORMAL
        # zawsze sprawdzenie długości
        self.długość = len(lista_kluczy)
        # canvas
        self.progress_bar.create_rectangle((self.dobrze - 1) * self.progress_width / self.ilość_słów_w_sesji, 0,
                                           (self.dobrze) * self.progress_width / self.ilość_słów_w_sesji,
                                           self.progress_height,
                                           fill='#0000c7', outline='#0000c7')
        for i in range(0, self.średnio + self.źle):
            self.progress_bar.create_rectangle((self.dobrze + i) * self.progress_width / self.ilość_słów_w_sesji,
                                               0,
                                               (self.dobrze + i + 1) * self.progress_width / self.ilość_słów_w_sesji,
                                               self.progress_height,
                                               fill='#f70000', outline='#f70000')

    def ostatnie_źle(self): # funkcja bo coś się zjebało przy pierwszym słowie w powtórce jeśli ostatnie normalne jest zaznaczone jako źle
        słowo = next(iter(słownik.values()))
        self.pokaż_odp_tekst.delete(0.0, END)
        self.pokaż_odp_tekst.insert(0.0, słowo)
        self.ilość_tłumaczenie += 1
        self.pokaż_odp_bttn["text"] = "Pokaż odpowiedź"
        # wyłączenie przycisku tłumaczącego
        self.pokaż_odp_bttn["state"] = DISABLED
        # włączenie przycisków dobrze średnio źle
        self.dobrze_bttn["state"] = NORMAL
        self.średnio_bttn["state"] = NORMAL
        self.źle_bttn["state"] = NORMAL
        self.pokaż_odp_bttn["command"] = self.pokaż_odp


# main
root = Tk()
root.title("Program do słówek : - DDD")
root.geometry("600x300")
root.iconbitmap(r'oj_byczku.ico')

app = Application(root)
root.mainloop()

"""Można dodać:
1 - przyciski które mowią czy dobrze średnio czy źle 
2 - losowe słowa z kończącą się listą i potem od nowa
3 - te co są dobrze są usuwane z listy wszystkich a te złe i średnio zostają i potem do powtarzania drugi raz
4 - pasek postępu i na niebiesko czerwono i żółto dobre i złe no i ilość wszystkich liczbowo i które teraz
5 - jakieś dopracowania, elementy graficzne, logo może czy coś"
"""
# źle jeden indeks przy powtarzaniu nie wiadomo czemu skoro self.ilość_tłumaczenie jest 0 i powinno być dobrze (przy naciskaniu pokaż odp)
