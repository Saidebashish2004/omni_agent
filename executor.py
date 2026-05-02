import subprocess
import sys

class OmniExecutor:
    @staticmethod
    def run_python_file(filename):
        """
        Runs the generated Python file and captures its output or error.
        """
        print(f"\n[Execution] Testing file: {filename}...")
        try:
            result = subprocess.run(
                [sys.executable, filename],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print("[Execution Success] Output:")
                print(result.stdout)
                return {"success": True, "output": result.stdout}
            else:
                print("[Execution Failed] Error found:")
                print(result.stderr)
                return {"success": False, "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            print("[Execution Failed] The script took too long to respond.")
            return {"success": False, "error": "TimeoutExpired: Script exceeded 10 seconds."}
        except Exception as e:
            print(f"[Execution Failed] Process error: {str(e)}")
            return {"success": False, "error": str(e)}