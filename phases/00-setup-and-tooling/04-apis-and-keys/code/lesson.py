import os, anthropic

client = anthropic.Antrhopic()

# first specified model, if no model specified, then claude-sonnet-5
MODEL = os.environ.get("LLM_MODEL", "claude-sonnet-5")

response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)

print(f"Response ({MODEL}): {response.content[0].text}")
