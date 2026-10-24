import subprocess
import platform


uv = subprocess.check_output(["uv", "--version"], text=True).split()[1]
python = platform.python_version()
vscode = subprocess.check_output("code --version", shell=True, text=True).splitlines()[0]
git = subprocess.check_output(["git", "--version"], text=True).split()[2]
ollama = subprocess.check_output(["ollama", "--version"], text=True).split()[-1]
claude = subprocess.check_output(["claude", "--version"], text=True).split()[0]


print("UV:", uv)
print("Python:", python) 
print("VS Code:", vscode)
print("Git:", git)
print("Ollama:", ollama)
print("Claude Code:", claude)