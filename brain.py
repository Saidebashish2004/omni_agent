import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

class OmniBrain:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in .env! Get one from aistudio.google.com")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-lite"

    def research_task(self, task_description, retries=2, delay=3):
        prompt = """
        You are an Omni-Agent designed for both indoor (digital/software) and outdoor (physical/hardware) tasks.
        Provide a technical 'bit' of knowledge for the following request.
        
        Format your response with:
        - REQUIREMENTS: Tools or software needed.
        - LOGIC/WIRING: The core bit of how it works.
        - SAFETY/TIPS: Important warnings or efficiency notes.
        
        Task: {}
        """.format(task_description)
        
        for attempt in range(retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model_id,
                    contents=prompt
                )
                return response.text
                
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    if attempt < retries - 1:
                        print(f"[!] Rate limit on '{self.model_id}'. Retrying in {delay}s...")
                        time.sleep(delay)
                        delay *= 2
                    else:
                        print("[!] Online Brain unavailable. Switching to Local Offline Fallback.")
                        return self.offline_fallback(task_description)
                else:
                    return f"ERROR: API Communication failed: {str(e)}"

    def offline_fallback(self, task_description):
        """Pre-formatted fallback script including valid code blocks."""
        # Using a standard multiline string without string formatting inside avoids quote errors entirely.
        fallback_text = (
            "[OFFLINE FALLBACK KNOWLEDGE BIT]\n"
            "The online reasoning engine is currently rate-limited.\n"
            "Generated local stub for: {}\n\n"
            "REQUIREMENTS:\n"
            "- Python 3 setup with standard local libraries.\n\n"
            "LOGIC/WIRING:\n"
            "```python\n"
            "# Fallback Python Script\n"
            "import sys\n\n"
            "def main():\n"
            "    print('Executing offline task...')\n"
            "    print('Status: Core operations normal.')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
            "```\n\n"
            "SAFETY/TIPS:\n"
            "- This is a local fallback script. Check the code before scaling.\n"
        )
        return fallback_text.format(task_description)