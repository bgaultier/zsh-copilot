from gradio_client import Client

with open('./prompt.txt', 'r') as file:
    prompt = file.read()

client = Client("ysharma/Chat_with_Meta_llama3_1_8b", verbose=False)
result = client.predict(
		message=prompt,
		temperature=0.95,
		max_new_tokens=512,
		api_name="/chat"
)
# print(result)

result = result.replace("assistant\n\n", "")

with open('result.txt', 'w') as file:
    file.write(result)
