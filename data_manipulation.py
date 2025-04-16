
#If the similarity score is lesser than the threshold it gives 0 else it gives one
def bool_similarity(results,threshold):
    bool_results = {}
    for key, value in results.items():
        if value>=threshold:
            bool_results[key]=1
        else:
            bool_results[key]=0
    return bool_results