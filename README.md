### Description

This repository is used to demonstrate the card.json structure used for the CARD database data.

### Download the card.json from CARD website

```
wget https://card.mcmaster.ca/latest/data && tar xvf data card.json && rm data
```

### Create environment and install jq

```
mamba create -c conda-forge -c bioconda -n card-json conda jq
```

### Activate the environment

```
conda activate card-json
```

### To deactivate an active environment, use

```
conda deactivate
```

### Format card.json using jq

```
cat card.json | jq . > card-formatted.json
```
### Get a model using only the model_id, e.g NDM-1 model

```
jq '."783"' card-formatted.json > model-783.json
```

### Get a model using only the model_id, e.g Mycobacterium tuberculosis intrinsic murA conferring resistance to fosfomycin model

```
jq '."2290"' card-formatted.json > model-2290.json
```

### See output

```
cat model-783.json
```

### Select using key and values

```
cat model-783.json | jq '.ARO_category | to_entries[] | select(.value.category_aro_class_name == "Antibiotic")'

cat card-formatted.json | jq '.[] | .ARO_category | to_entries[] | select(.value.category_aro_class_name == "Antibiotic")'
```

### Use the python script template to check key-value pairs

Note: Use print and exits statements as you write your python parser for the card.json file.

```
python parser.py
```