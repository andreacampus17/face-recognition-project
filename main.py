from loading_gallery import encode_images_in_directory
from loading_gallery import probes_per_images
from comparing import compare_faces
from data_manipulation import bool_similarity
from data_verification import false_negatives, true_positive_rate, false_positive_rate, false_negatives_rate
from data_verification import false_positives
from data_verification import true_negatives
from data_verification import true_positives
from data_verification import recognized_probes_per_images
from plots import plot_similarity_distributions, plot_roc_curve

import numpy as np


# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    probe_list_names=[]
    gallery_list_names=[]

    f_negatives_coll=[]
    f_positives_coll=[]


    gallery_directory = 'D:/Andrea/University/Digital Security/Progetto/Recognition_Project/Probation/Gallery'  # Sostituisci con il percorso della tua directory
    # Loading gallery images
    encodings_dict_directory = encode_images_in_directory(gallery_directory)
    print(f"Stampo i nomi dei file della gallery in ordine di come vengono letti")
    print(gallery_list_names)

    probe_directory = 'D:/Andrea/University/Digital Security/Progetto/Recognition_Project/Probation/Probe'

    # Loading probe images
    encodings_dict_probe = encode_images_in_directory(probe_directory)
    print(f"Stampo i nomi dei file del probe in ordine di come vengono letti")

    # Prints the content of the gallery dictionary
    # print(probe_list_names)


    num_entries = len(encodings_dict_directory)
    print(f"Numero di immagini con volto trovate: {num_entries}")

    gallery_filenames = list(encodings_dict_directory.keys())
    probe_filenames = list(encodings_dict_probe.keys())
    if not gallery_filenames:
        print("Nessuna immagine trovata nella galleria.")
        return
    #Confronts all the probe images with all the gallery images

    #Built to count how many probes there were per images, not used
    #probes_per_img =probes_per_images(probe_filenames,gallery_filenames)

    #Prints to check the results
    #print("Numero di probes per ogni immagine: ")
    #for key, value in probes_per_img.items():
        #print(f"Immagine: {key}--> Numero probes: {value}")
    similarity_results = {}

    for probe_filename, probe_encoding in encodings_dict_probe.items():
        for gallery_filename, gallery_encoding in encodings_dict_directory.items():
            # Confronta l'encoding del probe con l'encoding della galleria
            similarity = compare_faces(gallery_encoding, probe_encoding)

            # Building a key that contains the pair probe-gallery
            key = (probe_filename, gallery_filename)

                # Storing the results
            similarity_results[key] = similarity
            # Prints to check the results
            #print(f"Confronto tra {probe_filename} e {gallery_filename}: Similarità = {similarity}")

    threshold = np.linspace(0, 1, 100)
    tpr_list = []
    fpr_list = []
    fnr_list=[]
    false_pos_coll = {}
    true_p_coll = {}
    for data in threshold:
        recognized_probes_per_img={}

        bool_similarity_results=bool_similarity(similarity_results,data)
        # Prints the similarity results
        #print(f"Ora stampiamo il numero di probes riconosciuiti per ogni immagine della gallery:")
        #print(f"Numero di elementi in similarity_results: {len(similarity_results)}")
        for key, value in bool_similarity_results.items():
            probe_fl = key[0]
            gallery_fl = key[1]
            #print(f"Probe: {probe_fl}, Gallery: {gallery_fl}, Similarity: {value}")

        #Calculating TP,TN,FP,FN
        false_neg=false_negatives(bool_similarity_results)
        false_pos=false_positives(bool_similarity_results,similarity_results,false_pos_coll)
        true_pos =true_positives(bool_similarity_results,similarity_results,true_p_coll)
        true_neg=true_negatives(bool_similarity_results)

        #Calculating TPR,FPR,FNR
        tpr=true_positive_rate(true_pos,false_neg)
        fpr=false_positive_rate(false_pos,true_neg)
        fnr=false_negatives_rate(false_neg,true_pos)


        tpr_list.append(tpr)
        fpr_list.append(fpr)
        fnr_list.append(fnr)



        #Prints he following parameters to see the performance with the varing threshold
        print(f"Numero di falsi negativi con soglia= {data} e:{false_neg}")
        print(f"Numero di falsi positivi con soglia= {data} e:{false_pos}")
        print(f"Numero di veri positivi con soglia= {data} e:{true_pos}")
        print(f"Numero di veri negativi con soglia= {data} e:{true_neg}")

        #Build to count how many probe images there were per every gallery image
        #to then confronts it with probes_per_images and after prints it
        #Not used
        #recognized_probes_per_img=recognized_probes_per_images(bool_similarity_results,gallery_filenames)
        #print(f"Numero di probes per Immagine riconosciuti con soglia= {data}: ")
        #for key, value in recognized_probes_per_img.items():
            #print(f"Immagine: {key}--> Numero probes: {value}")
        #print(f"Soglia: {data}, TPR: {tpr}, FPR: {fpr}")
    #plt.figure()
    #plot_roc_curve(fpr_list, tpr_list)
    #plot_det_curve(fnr_list,fpr_list)

    #Select a final threshold
    final_threshold=0.8

    #We look for the matchs with the final threshold
    bool_similarity_results_final = bool_similarity(similarity_results, final_threshold)
    # Prints the similarity results
    # print(f"Ora stampiamo il numero di probes riconosciuiti per ogni immagine della gallery:")
    # print(f"Numero di elementi in similarity_results: {len(similarity_results)}")
    for key, value in bool_similarity_results_final.items():
        probe_fl = key[0]
        gallery_fl = key[1]
        # print(f"Probe: {probe_fl}, Gallery: {gallery_fl}, Similarity: {value}")
    #Looking for TP and FP with the final threshold
    false_pos_coll_final={}
    true_pos_coll_final={}
    #false_neg = false_negatives(bool_similarity_results_final)
    # true_neg = true_negatives(bool_similarity_results_final)

    false_pos = false_positives(bool_similarity_results_final, similarity_results, false_pos_coll_final)
    true_pos = true_positives(bool_similarity_results_final,similarity_results,true_pos_coll_final)


    impostors=list(false_pos_coll.values())
    true=list(true_p_coll.values())
    plot_similarity_distributions(true, impostors)
    k_values = np.linspace(1, 400, 400, dtype=int)
    sim_values=list(similarity_results.values())
    #plot_cmc_curve( sim_values,bool_similarity_results_final, k_values.tolist())

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
