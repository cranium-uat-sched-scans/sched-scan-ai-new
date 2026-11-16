import openai

client = openai.OpenAI()


def classify(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Classify the sentiment of: {text}"}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(classify("Scheduled scans picked up this repo on their own."))
