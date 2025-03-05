import google.generativeai as genai

genai.configure(api_key="AIzaSyDXm5G-lYME1ccDIgoAR-7KTJpihspqVxA")

models = genai.list_models()
for model in models:
    print(model.name)
