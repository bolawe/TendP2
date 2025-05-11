import openai
import os

print("Generating AI report...")

# Read extracted text
for filename in os.listdir("outputs"):
    if filename.endswith(".txt"):
        with open(f"outputs/{filename}", "r") as f:
            text = f.read()
        
        # Generate report (modify prompt as needed)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": f"""
                Create a professional tender report with:
                1. Key requirements summary
                2. Technical methodology
                3. Compliance checklist
                
                Based on this text: {text}
                """
            }]
        )
        
        # Save AI output
        report = response.choices[0].message.content
        with open(f"outputs/{filename.replace('.txt', '_report.pdf')}", "w") as f:
            f.write(report)

print("AI report generated!")
