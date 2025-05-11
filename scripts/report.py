import os
from openai import OpenAI
from docx import Document  # New dependency

client = OpenAI()

def generate_reports():
    if not os.path.exists("outputs"):
        print("Error: No 'outputs/' folder found. Run ocr.py first.")
        return

    print("Generating Word reports from OCR text:")
    for filename in os.listdir("outputs"):
        if filename.endswith(".txt"):
            try:
                with open(f"outputs/{filename}", "r") as f:
                    text = f.read()

                # Generate report content
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{
                        "role": "system",
                        "content": "Create a professional tender report in structured format."
                    }, {
                        "role": "user",
                        "content": f"""
                        Generate a comprehensive tender report with:
                        1. Project Overview (Heading 1 style)
                        2. Technical Requirements (Heading 2 style)
                        3. Methodology (Heading 2 style)
                        4. Compliance Checklist (Bullet points)
                        
                        Text: {text[:15000]}
                        """
                    }]
                )
                
                # Create Word document
                doc = Document()
                doc.add_heading('Tender Report', 0)
                
                # Format AI response
                for line in response.choices[0].message.content.split('\n'):
                    if line.startswith('1.') or "Overview" in line:
                        doc.add_heading(line, level=1)
                    elif line.startswith(('2.', '3.')) or "Requirements" in line or "Methodology" in line:
                        doc.add_heading(line, level=2)
                    elif line.startswith('-'):
                        doc.add_paragraph(line, style='List Bullet')
                    else:
                        doc.add_paragraph(line)
                
                # Save as .docx
                output_name = filename.replace('.txt', '_report.docx')
                doc.save(f"outputs/{output_name}")
                print(f"✓ Generated: {output_name}")
                
            except Exception as e:
                print(f"✗ Error: {str(e)}")

if __name__ == "__main__":
    generate_reports()
