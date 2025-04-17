# Face Recognition and Analysis Project

Questo progetto utilizza tecniche di riconoscimento facciale e calcolo delle somiglianze per analizzare immagini e valutarne le performance tramite metriche statistiche e visualizzazioni. Ogni componente è stato attentamente progettato per offrire accuratezza e flessibilità.

## Contenuto del Progetto

### 1. `comparing.py`
- Contiene la funzione `compare_faces`, che calcola la similarità tra due codifiche facciali usando il coseno di similarità.
- È il modulo base per confrontare immagini e determinare quanto sono simili.

### 2. `data_manipulation.py`
- Fornisce la funzione `bool_similarity`, che converte i risultati di similarità in valori booleani (`1` o `0`) sulla base di una soglia specificata.
- Questa funzione è utile per classificare i confronti come corrispondenze accettate o rifiutate.

### 3. `data_verification.py`
- Include diverse funzioni per calcolare metriche chiave, tra cui:
  - **True Positives** (`true_positives`) e **False Positives** (`false_positives`).
  - **True Negatives** (`true_negatives`) e **False Negatives** (`false_negatives`).
  - Tassi di errore come **TPR**, **FPR** e **FNR**.
- Queste metriche aiutano a valutare la performance complessiva del sistema.

### 4. `main.py`
- Il cuore del progetto. Esegue il flusso completo:
  - Caricamento delle immagini da cartelle specifiche (gallery e probe).
  - Calcolo della similarità tra le immagini.
  - Valutazione della performance con diverse soglie e calcolo delle metriche.
  - Generazione e visualizzazione di grafici ROC, distribuzioni di similarità, e altro.
- Fornisce un'interfaccia diretta per eseguire il sistema.

### 5. `plots.py`
- Modulo dedicato alla visualizzazione dei dati:
  - **Curva ROC**: Mostra il compromesso tra tasso di falsi positivi e veri positivi.
  - **Distribuzioni di Similarità**: Confronta genuine e impostori.
  - **Curva CMC**: Illustra il tasso di riconoscimento cumulativo.
  - **Curva DET**: Visualizza l'equilibrio tra FPR e FNR.

### 6. `recognition.py`
- Fornisce una funzione di rilevamento facciale (`recognize_faces`) utilizzando la libreria `face_recognition`.
- Trova e individua tutte le facce in un'immagine, con la possibilità di salvarle evidenziate visivamente.

## Requisiti

- **Librerie richieste**:
  - Python 3.8+
  - `face_recognition`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`
  - `Pillow`
- **Dati richiesti**:
  - Cartelle contenenti immagini di gallery e probe.

## Istruzioni per l'Uso

1. Clona il repository:
   ```bash
   git clone https://github.com/andreacampus17/face-recognition-project.git
