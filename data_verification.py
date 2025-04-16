import matplotlib.pyplot as plt

def false_negatives(similarity_results):
    false_n=0
    false_negatives_coll={}
    for key, value in similarity_results.items():
        probe_fl = key[0]
        gallery_fl = key[1]
        probe_first=probe_fl.split('_')[0]
        gallery_first = gallery_fl.split('_')[0]
        #Confronto le due stringhe
        if probe_first == gallery_first and similarity_results[key]==0 :
            false_n+=1
    return false_n

def false_positives(bool_similarity_results,similarity_results,false_p_coll):
    false_p=0

    for key, value in bool_similarity_results.items():
        probe_fl = key[0]
        gallery_fl = key[1]
        probe_first=probe_fl.split('_')[0]
        gallery_first = gallery_fl.split('_')[0]
        #Confronto le due stringhe
        if probe_first != gallery_first and bool_similarity_results[key]==1 :
            false_p+=1
            false_p_coll[key]=similarity_results[key]
    return false_p

def true_positives(bool_similarity_results,similarity_results,true_p_coll):
    true_p = 0
    for key, value in bool_similarity_results.items():
        probe_fl = key[0]
        gallery_fl = key[1]
        probe_first = probe_fl.split('_')[0]
        gallery_first = gallery_fl.split('_')[0]
        # Confronto le due stringhe
        if probe_first == gallery_first and bool_similarity_results[key] == 1:
            true_p_coll[key]=similarity_results[key]
            true_p += 1
    return true_p

def true_negatives(similarity_results):
    true_n = 0
    false_negatives_coll = {}
    for key, value in similarity_results.items():
        probe_fl = key[0]
        gallery_fl = key[1]
        probe_first = probe_fl.split('_')[0]
        gallery_first = gallery_fl.split('_')[0]
        # Confronto le due stringhe
        if probe_first != gallery_first and similarity_results[key] == 0:
            true_n+=1

    return true_n



def true_positive_rate(true_p, false_n):
    if true_p + false_n == 0:
        return 0
    return true_p / (true_p + false_n)

def false_positive_rate(false_p, true_n):
    if false_p + true_n == 0:
        return 0
    return false_p / (false_p + true_n)

def false_negatives_rate(false_n,true_p):
    if false_n + true_p == 0:
        return 0
    else:
        return false_n / (false_n + true_p)


def recognized_probes_per_images(bool_similarity_results,gallery_filenames):
    recognized_probes_per_img={}
    for gallery_fl in gallery_filenames:
        recognized_probes_per_img[gallery_fl] = 0

    for (probe_filename, gallery_filename), value in bool_similarity_results.items():
        probe_first = probe_filename.split('_')[0]
        gallery_first = gallery_filename.split('_')[0]
        if gallery_first == probe_first and value ==1 :
            recognized_probes_per_img[gallery_filename]+=1
    return recognized_probes_per_img