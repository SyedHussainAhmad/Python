import openai
openai.api_key  = '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'

# Helper Function:
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# text = input()
text = "My name is hussain and i am a studetn at pucit."

prompt = f"""
Summarize the text delimited by triple backticks 
into a single sentence.
```{text}```
"""


response = get_completion(prompt)
print(response)