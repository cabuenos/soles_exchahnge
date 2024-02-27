import json
import os

# xxx =os.path.dirname(__file__)

# www =os.listdir(path=xxx)
# print(www)


# load json files
template_files = [
    template_file for template_file in os.listdir(path=os.path.dirname(__file__)) 
    if template_file[-5:].lower()=='.json'
]

if len(template_files)>0:
    for template_file in template_files:
        with open(f'{os.path.dirname(__file__)}/{template_file}', 'r') as tmp:
            locals()[template_file[:-5]]= json.loads(tmp.read())

# def load_templates():
# with open (f'{os.path.dirname(__file__)}/app_home.json', 'r') as vw:
#     app_home = json.loads(vw.read())
