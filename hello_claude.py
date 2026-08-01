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


test_cases = [
    {
        "prompt": "Say hello, and tell me one interesting fact about Python in one sentence.",
        "expected_keyword": "Python",
    },
    {
        "prompt": "What does the word 'variable' mean in programming, in one sentence?",
        "expected_keyword": "variable",
    },
    {
        "prompt": "Name one thing a for loop is good for, in one sentence.",
        "expected_keyword": "loop",
    },
]

for case in test_cases:
    answer = ask_claude(case["prompt"])
    print(f"Q: {case['prompt']}")
    print(f"A: {answer}")
    if case["expected_keyword"].lower() in answer.lower():
        print("PASS")
    else:
        print("FAIL")
    print()
