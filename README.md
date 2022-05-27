# Data analysis
- Document here the project: deep_painting_app
- Description: App which can predict the artistic movement of portrait paintings
- Data Source:
  Portrait Painting Dataset For Different Movements
  Published: 14 January 2021
  By Jiaqi Yang
  Primary data source of this dataset from WikiArt
  https://data.mendeley.com/datasets/289kxpnp57/1

- Type of analysis: convolutional neural network classification

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for deep_painting_app in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/deep_painting_app`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "deep_painting_app"
git remote add origin git@github.com:{group}/deep_painting_app.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
deep_painting_app-run
```

# Install

Go to `https://github.com/{group}/deep_painting_app` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/deep_painting_app.git
cd deep_painting_app
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
deep_painting_app-run
```

```package
pip install -e deep_painting_app
```

Package composition:
depp_painting_app
  api
    index
    predict_movement
    predict
  data_processing
    load_and_divide_dataset
    classes_names_to_dict
    give_class_name
  explore_data
    display_paintings_and_classes
    random_painting
    number_img_per_class
  model
    initialize_baseline_model
    baseline_model_pipeline
