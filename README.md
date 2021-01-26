# Ike's Number Guessing Game
train, test = train_test_split(data, test_size=0.2, random_state=1 )

if "training" not in os.listdir():
    os.mkdir("./training")

if "models" not in os.listdir():
    os.mkdir("./models")
if "outputs" not in os.listdir():
    os.mkdir("./outputs")

train.to_csv("training/train_data.csv", index = False)

data_store = ws.get_default_datastore()
data_store.upload(src_dir = "./training", target_path = 'udacity-project', overwrite = True,  show_progress = True)

Part 2
train_data = Dataset.Tabular.from_delimited_files(path=data_store.path("udacity-project/train_data.csv"))
# train=TabularDatasetFactory.from_delimited_files([(data_store, 'training/train_data.csv')])

import joblib
os.makedirs('outputs', exist_ok = True)
joblib.dump(fitted_model, 'outputs/fitted_model.joblib')
