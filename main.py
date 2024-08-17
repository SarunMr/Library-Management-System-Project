import subprocess
import os
import sys

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    register_page_path = os.path.join(current_dir, "Register_page.py")
    
    if not os.path.exists(register_page_path):
        print(f"Error: {register_page_path} not found.")
        sys.exit(1)
    
    try:
        subprocess.run([sys.executable, register_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Register_page.py: {e}")
    except FileNotFoundError:
        print(f"Error: Python interpreter not found. Make sure Python is installed and in your PATH.")

if __name__ == "__main__":
    main()
