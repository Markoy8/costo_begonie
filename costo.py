import streamlit as st

# Titolo dell'applicazione
st.title("Calcolo dei Costi di Rifacimento Condominiale")

# Personalizzazione della checkbox tramite CSS
st.markdown("""
    <style>
    .checkbox {
        display: flex;
        align-items: center;
    }
    .checkbox .stCheckbox {
        margin-right: 10px;
        transform: scale(1.5);
    }
    .checkbox label {
        font-size: 1.2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Funzione per ottenere il valore da slider o casella di testo
def get_input(label, slider_min, slider_max, step, key_slider, key_text):
    col1, col2 = st.columns([2, 1])
    with col1:
        slider_value = st.slider(label, min_value=slider_min, max_value=slider_max, step=step, key=key_slider)
    with col2:
        text_value = st.text_input("Oppure inserisci un valore", value=str(slider_value), key=key_text)
    
    try:
        value = float(text_value)
    except ValueError:
        value = slider_value
    
    return value

# Input per il costo del rifacimento della facciata
st.header("Inserisci i costi di rifacimento:")
costo_facciata = get_input("Costo del rifacimento della facciata (€)", 0.0, 100000.0, 100.0, "slider_facciata", "text_facciata")

# Input per il costo del rifacimento del terrazzo
costo_terrazzo = get_input("Costo del rifacimento del terrazzo (€)", 0.0, 100000.0, 100.0, "slider_terrazzo", "text_terrazzo")

# Input per i millesimi del condomino
st.header("Inserisci i millesimi del condomino:")
millesimi = get_input("Millesimi del condomino", 0.0, 1000.0, 1.0, "slider_millesimi", "text_millesimi")

# Checkbox per indicare se l'appartamento è un attico
st.header("Seleziona le opzioni aggiuntive:")
is_attico = st.checkbox("L'appartamento è un attico")

# Calcolo del costo per la facciata
costo_facciata_condomino = costo_facciata * millesimi / 1000

# Calcolo del costo per il terrazzo
costo_terrazzo_condomino = costo_terrazzo * (2/3) * millesimi / 1000

# Se l'appartamento è un attico, aggiungere 1/3 del costo del terrazzo
if is_attico:
    costo_terrazzo_condomino += costo_terrazzo * (1/3) * millesimi / 1000

# Calcolo del costo totale da sostenere
costo_totale = costo_facciata_condomino + costo_terrazzo_condomino

# Visualizzazione dei risultati
st.header("Risultati del calcolo:")
st.write(f"Costo per il rifacimento della facciata: **€{costo_facciata_condomino:.2f}**")
st.write(f"Costo per il rifacimento del terrazzo: **€{costo_terrazzo_condomino:.2f}**")
st.write(f"Costo totale da sostenere: **€{costo_totale:.2f}**")
