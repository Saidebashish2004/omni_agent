import re
import os

class OmniActions:
    @staticmethod
    def extract_and_create_file(task_name, knowledge_text):
        """
        Parses code blocks out of a technical bit and saves the file.
        """
        print(f"[Action] Checking for executable code in '{task_name}'...")

        # We use \x60 instead of backticks to completely prevent copy-paste errors
        pattern = r"\x60\x60\x60(?:\w+)?\s*\n?(.*?)\n?\x60\x60\x60"
        code_blocks = re.findall(pattern, knowledge_text, re.DOTALL)
        
        if not code_blocks:
            print("[Action] No code blocks detected to save.")
            return None

        # Clean the extracted text
        code_content = code_blocks[0].strip()

        # Determine file extension based on content or keywords
        ext = ".py"
        text_lower = knowledge_text.lower()
        if "arduino" in text_lower or "ldr" in text_lower:
            ext = ".ino"
        elif "html" in text_lower:
            ext = ".html"
        elif "cpp" in text_lower or "c++" in text_lower:
            ext = ".cpp"

        # Sanitize task name to make a valid filename
        filename = f"{task_name.lower().replace(' ', '_').replace('-', '_')}{ext}"
        
        # Write file to the current directory
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(code_content)
            print(f"[Action Success] Created local file: {filename}")
            return filename
        except Exception as e:
            print(f"[Action Error] Failed to write file: {e}")
            return None