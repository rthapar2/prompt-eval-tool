import anthropic

client = anthropic.Anthropic()


def ask_claude(question):
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ],
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


test_questions = [
    "Say hello, and tell me one interesting fact about Python in one sentence.",
    "What does the word 'variable' mean in programming, in one sentence?",
    "Name one thing a for loop is good for, in one sentence.",
]

expected_keywords = ["Python", "variable", "loop"]

for question, keyword in zip(test_questions, expected_keywords):
    answer = ask_claude(question)
    print(f"Q: {question}")
    print(f"A: {answer}")
    if keyword.lower() in answer.lower():
        print("PASS")
    else:
        print("FAIL")
    print()
