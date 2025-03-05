import google.generativeai as genai
from api_info import api_key, model_name
genai.configure(api_key)

models = genai.list_models()
for model in models:
    print(model.name)
