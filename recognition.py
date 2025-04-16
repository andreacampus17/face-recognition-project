import face_recognition
from PIL import Image, ImageDraw

def recognize_faces(image_path, output_image_path="output_image.jpg"):
    # Carica l'immagine
    image = face_recognition.load_image_file(image_path)

    # Trova tutte le facce nell'immagine
    face_locations = face_recognition.face_locations(image)

    print(f"Ho trovato {len(face_locations)} faccia/e nell'immagine.")

    # Converti l'immagine da numpy array a PIL Image per la modifica
    #pil_image = Image.fromarray(image)
    #draw = ImageDraw.Draw(pil_image)

    # Disegna un rettangolo intorno a ciascuna faccia
    #for (top, right, bottom, left) in face_locations:
        #draw.rectangle([left, top, right, bottom], outline="red", width=3)

    # Salva l'immagine con le facce evidenziate
    #pil_image.save(output_image_path)

    # Mostra l'immagine
    #pil_image.show()

# Questo blocco permette di eseguire il file separatamente
if __name__ == "__main__":
    recognize_faces("C:/Users/campu/Downloads/foto1.jpg")
