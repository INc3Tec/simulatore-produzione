import tkinter as tk
from tkinter import Toplevel, Label, Button
import random
import math

def simula_bicchieri_carta():
    num_lotti = random.randint(5, 360)
    numero_pezzi = num_lotti * 2700

    macchine_possibili = ['M1', 'M2', 'M3', 'M4']
    macchine_attive = random.sample(macchine_possibili, random.randint(1, 4))
    velocita_macchine = sum(120 if m == 'M4' else 60 for m in macchine_attive)

    personalizzato = random.choice(["Generico", "Personalizzato"])
    umidita = random.randint(20, 100)
    operatore = random.choice(["Esperto", "Avanzato", "Intermedio", "Stagista"])
    efficienza_percentuale = random.randint(70, 95)
    efficienza = efficienza_percentuale / 100.0

    # Nuovi parametri
    cambio_bobina = random.randint(0, 2)
    extra_cambio_bobina = cambio_bobina * 10

    qualita_carta = random.choices(["Alta", "Media", "Bassa"], weights=[3, 5, 2])[0]
    temperatura_ambiente = random.randint(10, 40)

    if temperatura_ambiente >= 30:
        bagnatura = random.choices(["Ottima", "Eccessiva", "Insufficiente"], weights=[2, 2, 6])[0]
    else:
        bagnatura = random.choice(["Ottima", "Eccessiva", "Insufficiente"])

    tempo_perfetto = numero_pezzi / velocita_macchine
    tempo_effettivo = tempo_perfetto

    inceppamenti = math.floor(tempo_effettivo / 10) if 'M4' in macchine_attive else 0
    tempo_effettivo += inceppamenti

    extra_personalizzazione = 30 if personalizzato == "Personalizzato" else 0
    tempo_effettivo += extra_personalizzazione

    extra_umidita = (numero_pezzi // 2700) * 5 if umidita > 60 else 0
    tempo_effettivo += extra_umidita

    tempo_effettivo += extra_cambio_bobina

    modificatore_operatore = {
        "Esperto": 0.8,
        "Avanzato": 0.9,
        "Intermedio": 1.0,
        "Stagista": 1.2
    }
    descrizione_operatore = {
        "Esperto": "velocizza del 20%",
        "Avanzato": "velocizza del 10%",
        "Intermedio": "nessuna modifica",
        "Stagista": "rallenta del 20%"
    }
    tempo_effettivo *= modificatore_operatore[operatore]

    if qualita_carta == "Alta":
        tempo_effettivo *= 0.9
    elif qualita_carta == "Bassa":
        tempo_effettivo *= 1.2

    if bagnatura in ["Eccessiva", "Insufficiente"]:
        tempo_effettivo *= 1.1

    tempo_finale = tempo_effettivo / efficienza

    def minuti_a_ore_minuti(minuti):
        ore = int(minuti // 60)
        min_restanti = int(minuti % 60)
        return f"{ore}h {min_restanti}min"

    finestra = Toplevel(root)
    finestra.title("Dettagli Simulazione")
    finestra.geometry("600x560")
    finestra.resizable(False, False)

    Label(finestra, text="Simulazione: Bicchieri di carta 80 ml", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    righe = [
        ("Numero pezzi", f"{numero_pezzi}"),
        ("Macchine attive", ", ".join(macchine_attive)),
        ("Velocità totale", f"{velocita_macchine} unità/min"),
        ("Tipo", f"{personalizzato} (+{extra_personalizzazione} min)" if personalizzato == "Personalizzato" else "Generico"),
        ("Umidità", f"{umidita}% (+{extra_umidita} min)" if umidita > 60 else f"{umidita}%"),
        ("Temperatura ambiente", f"{temperatura_ambiente} °C"),
        ("Operatore", f"{operatore} ({descrizione_operatore[operatore]})"),
        ("Inceppamenti", f"{inceppamenti} min" if inceppamenti > 0 else "Nessuno"),
        ("Cambio bobina", f"{cambio_bobina} (+{extra_cambio_bobina} min)"),
        ("Qualità carta", f"{qualita_carta}"),
        ("Bagnatura carta", f"{bagnatura} ({'+10%' if bagnatura != 'Ottima' else 'nessun effetto'})"),
        ("Efficienza simulata", f"{efficienza_percentuale}%"),
        ("Tempo ideale", minuti_a_ore_minuti(tempo_perfetto)),
        ("Tempo reale di produzione", minuti_a_ore_minuti(tempo_finale))
    ]

    for i, (etichetta, valore) in enumerate(righe, start=1):
        Label(finestra, text=etichetta, anchor='w', width=28, font=("Arial", 10)).grid(row=i, column=0, padx=10, sticky='w')
        Label(finestra, text=valore, anchor='w', width=35, font=("Arial", 10, "bold")).grid(row=i, column=1, sticky='w')

    Button(finestra, text="Chiudi", command=finestra.destroy).grid(row=len(righe)+1, column=0, columnspan=2, pady=20)

# Interfaccia principale
root = tk.Tk()
root.title("Simulatore Produzione")
root.geometry("400x300")

tk.Label(root, text="Seleziona un prodotto per avviare la simulazione", font=("Arial", 12)).pack(pady=20)
tk.Button(root, text="Bicchieri di carta 80 ml", command=simula_bicchieri_carta, width=30, height=2).pack(pady=5)
tk.Button(root, text="Carta stampata per bicchieri", state='disabled', width=30, height=2).pack(pady=5)
tk.Button(root, text="Palettine caffè in legno", state='disabled', width=30, height=2).pack(pady=5)
tk.Button(root, text="Palettine caffè in plastica", state='disabled', width=30, height=2).pack(pady=5)

root.mainloop()
