import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Say hello, and tell me one interesting fact about Python in one sentence."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
