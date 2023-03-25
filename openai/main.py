import openai
import config

openai.api_key = config.api_key

# Forzamos un contexto
messages = [{
    'role': 'system', 
    'content': 'Eres un asistente de traducción de español a inglés'
}]


while True:
    content = input('¿Sobre que quieres hablar?')

    if content is 'exit':
        break

    # Agregamos el contexto de nuestras preguntas
    messages.append({'role': 'user', 'content': content })

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    response_content = response['choices'][0]['message']['content']

    # Agregamos el contexto de las respuestas
    messages.append({'role': 'assistent', 'content': response_content })

    print(response_content)