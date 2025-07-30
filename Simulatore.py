import streamlit as st
import random
import math

st.set_page_config(page_title="Simulatore Produzione Bicchieri", layout="centered")
st.title("Simulatore Produzione - Bicchieri carta 80 ml")

if st.button("Avvia simulazione"):
    # Parametri macchina
    macchine = random.sample(['M1', 'M2', 'M3', 'M4'], random.randint(1, 4))
    velocita = sum([120 if m == 'M4' else 60 for m in macchine])

    # Numero pezzi (multipli di 2700 da 13.500 a 972.000)
    numero_pezzi = random.randint(5, 360) * 2700

    # Tempo base
    tempo_base = numero_pezzi / velocita
    tempo_effettivo = tempo_base

    # Inceppamenti (solo se M4 è presente)
    inceppamenti = math.floor(tempo_effettivo / 10) if 'M4' in macchine else 0
    tempo_effettivo += inceppamenti

    # Personalizzazione
    tipo = random.choice(["Generico", "Personalizzato"])
    extra_personalizzazione = 30 if tipo == "Personalizzato" else 0
    tempo_effettivo += extra_personalizzazione

    # Umidità
    umidita = random.randint(20, 100)
    extra_umidita = (numero_pezzi // 2700) * 5 if umidita > 60 else 0
    tempo_effettivo += extra_umidita

    # Operatore
    operatore = random.choice(["Esperto", "Avanzato", "Intermedio", "Stagista"])
    modificatore_operatore = {"Esperto": 0.8, "Avanzato": 0.9, "Intermedio": 1.0, "Stagista": 1.2}
    descrizione_operatore = {
        "Esperto": "velocizza del 20%",
        "Avanzato": "velocizza del 10%",
        "Intermedio": "nessuna modifica",
        "Stagista": "rallenta del 20%"
    }
    tempo_effettivo *= modificatore_operatore[operatore]

    # Cambio bobina
    cambio_bobina = random.randint(0, 2)
    tempo_effettivo += cambio_bobina * 10

    # Qualità carta
    qualita_carta = random.choice(["Alta", "Media", "Bassa"])
    if qualita_carta == "Alta":
        tempo_effettivo *= 0.9
    elif qualita_carta == "Bassa":
        tempo_effettivo *= 1.2

    # Temperatura e bagnatura
    temperatura = random.randint(10, 40)
    if temperatura >= 30:
        bagnatura = random.choices(["Ottima", "Eccessiva", "Insufficiente"], weights=[2, 2, 6])[0]
    else:
        bagnatura = random.choice(["Ottima", "Eccessiva", "Insufficiente"])

    if bagnatura in ["Eccessiva", "Insufficiente"]:
        tempo_effettivo *= 1.1

    # Efficienza globale
    efficienza_percentuale = random.randint(70, 95)
    tempo_finale = tempo_effettivo / (efficienza_percentuale / 100)

    def minuti_a_ore_minuti(minuti):
        ore = int(minuti // 60)
        min_restanti = int(minuti % 60)
        return f"{ore}h {min_restanti}min"

    # Visualizzazione risultati
    st.subheader("Risultati della simulazione")

    st.markdown("""
    <style>
    .st-emotion-cache-zt5igj {border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;}
    </style>
    """, unsafe_allow_html=True)

    st.write("**Numero pezzi:**", numero_pezzi)
    st.write("**Macchine attive:**", ', '.join(macchine))
    st.write("**Velocità totale:**", f"{velocita} unità/min")
    st.write("**Tipo:**", tipo, f"(+{extra_personalizzazione} min)" if tipo == "Personalizzato" else "")
    st.write("**Umidità:**", f"{umidita}%", f"(+{extra_umidita} min)" if umidita > 60 else "")
    st.write("**Operatore:**", f"{operatore} ({descrizione_operatore[operatore]})")
    st.write("**Cambio bobina:**", f"{cambio_bobina} (+{cambio_bobina * 10} min)")
    st.write("**Qualità carta:**", qualita_carta)
    st.write("**Temperatura ambiente:**", f"{temperatura} °C")
    st.write("**Bagnatura carta:**", bagnatura)
    st.write("**Efficienza linea:**", f"{efficienza_percentuale}%")

    st.markdown("---")
    st.write("**Tempo ideale (senza condizionamenti):**", minuti_a_ore_minuti(tempo_base))
    st.write("**Tempo reale di produzione:**", minuti_a_ore_minuti(tempo_finale))
