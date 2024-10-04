import google.generativeai as genai
from google.colab import userdata
import time
from IPython.display import Markdown
from google.colab import files

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Você é o Faustão, o famoso apresentador de televisão! Está no comando de um programa ao vivo, cheio de energia e com seu jeito único de interagir com o público. Responda sempre com bom humor, entusiasmo e com as famosas expressões marcantes que só o Faustão sabe usar!",
)
history = []

def converse_com_o_fausto(model, history):
  print("Olá! Sou o Faustão, o famoso apresentador de televisão! Estou aqui para bater um papo com você! Vamos lá!")
  user_input = input("Você: ")
  chat_session = model.start_chat(
  history= history)
  response = chat_session.send_message(user_input)
  model_response = response.text
  print(f"Faustão: {model_response}")
  print()
  history.append({"role":"user","parts": [user_input] })
  history.append({"role":"model","parts": [model_response] })
  return history

def reclames_do_plim_plim(generation_config):
  GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
  genai.configure(api_key=GOOGLE_API_KEY) 
  uploaded = files.upload()
  video_file_name = list(uploaded.keys())[0]

  sample_file = genai.upload_file(path=video_file_name)

  print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
  file = genai.get_file(name=sample_file.name)
  print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

  response = model.generate_content(["Você é o Faustão, o famoso apresentador de televisão. Sua tarefa é analisar a imagem apresentado e dizer os pontos importantes dela!", file])

  print(response.text)

def video_cassetadas(generation_config):
  genai.configure(api_key=GOOGLE_API_KEY)
  uploaded = files.upload()
  video_file_name = list(uploaded.keys())[0]
  print(f"Uploading file...")
  video_file = genai.upload_file(path=video_file_name)
  print(f"Completed upload: {video_file.uri}")
  
  while video_file.state.name == "PROCESSING":
      print('.', end='')
      time.sleep(10)
      video_file = genai.get_file(video_file.name)
  
  if video_file.state.name == "FAILED":
    raise ValueError(video_file.state.name)
  
    prompt = "Summarize this video. Then create a quiz with answer key based on the information in the video."
  
  model = genai.GenerativeModel(model_name="gemini-1.5-pro")
  
  prompt = "Você é o Faustão, o famoso apresentador de televisão. Sua tarefa é analisar o vídeo apresentado e dizer os pontos importantes!"
  
  print("Making LLM inference request...")
  response = model.generate_content([prompt, video_file],
                                    request_options={"timeout": 600})
  print(response.text)

print("Começando o Faustão no Chat!")
print("A - Converse com o Faustão! (Geração de Texto)")
print("B - Chamar os reclames do plim plim! (Análise de Imagens)")
print("C - Vídeo cassetadas! (Análise de Videos)")
print("D - Encerrar programa de hoje!")
while True:
  menu_input = input("Letra: ").upper()
  if menu_input == "A":
    history = converse_com_o_fausto(model, history)
  elif menu_input == "B":
    reclames_do_plim_plim(generation_config)
  elif menu_input == "C":
    video_cassetadas(generation_config)
  elif menu_input == "D":
    break
  else:
    print("ERROU!")
