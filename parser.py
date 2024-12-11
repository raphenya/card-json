import json
import os


def read_card_json(path_to_card_json):
    j = ""
    try:
        with open(os.path.join(path_to_card_json), 'r') as jfile:
            j = json.load(jfile)
    except Exception as e:
        print(e)
        exit()

    # show keys
    for i in j:
        # 1. show all keys
        # print(j.keys())
        if i.isdigit():
            # 2. show models
            # print("MODEL-IDS: ", i)
            # 3. show keys per model
            # print(j[i].keys())
            # 4. selecting for Antibiotics
            # print(j[i]["ARO_category"].keys())
            # for c in j[i]["ARO_category"]:
            #     if j[i]["ARO_category"][c]["category_aro_class_name"] == "Antibiotic":
            #         print(j[i]["ARO_category"][c]["category_aro_class_name"])
            #         print(j[i]["ARO_category"][c]["category_aro_name"])
            exit("DEBUG-1")
        else:
            # 5. show other keys
            # print("OTHER: ", i)
            exit("DEBUG-2")
    return j


read_card_json("card.json")
