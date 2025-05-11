from openai import OpenAI

client = OpenAI()  # Automatically uses your API key from env

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": f"""
        Summarize this tender document into:
        1. Key Requirements
        2. Technical Specifications
        3. Compliance Needs
        
        Document Text: {text[:15000]}
        """
    }]
)
report = response.choices[0].message.content
