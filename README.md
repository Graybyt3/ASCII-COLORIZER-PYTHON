# GRAYBYTE ASCII-COLORIZER-PYTHON

**One-click tool to turn plain ASCII art into sexy colored f-string blocks**  
<br><br>
<p align="center">
  <img src="https://raw.githubusercontent.com/Graybyt3/ASCII-COLORIZER-PYTHON/refs/heads/main/ascii-color.png" alt="header banner" />
</p>
<br><br>

## What it does

1. Paste plain (monochrome) ASCII art
2. Applies color cycling per token/block  
   (RED → GREEN → YELLOW → GREEN → MAGENTA → CYAN → repeat)
3. Shows live colored preview in terminal
4. Generates **exact copy-paste ready** Python code :

```python
ascii_art = (
f"\n\n{Fore.RED}─█▀▀█ {Fore.GREEN}░█▀▀▀█ {Fore.YELLOW}░█▀▀█ {Fore.GREEN}▀█▀ {Fore.RED}▀█▀ {Fore.CYAN}░█▀▀█ {Fore.RED}░█▀▀▀█ {Fore.GREEN}░█─── {Fore.YELLOW}░█▀▀▀█ {Fore.GREEN}░█▀▀█ {Fore.RED}▀█▀ {Fore.CYAN}░█▀▀▀█ {Fore.RED}░█▀▀▀ {Fore.GREEN}░█▀▀█ {Style.RESET_ALL}\n"
f"{Fore.RED}░█▄▄█ {Fore.GREEN}─▀▀▀▄▄ {Fore.YELLOW}░█─── {Fore.GREEN}░█─ {Fore.RED}░█─ {Fore.CYAN}░█─── {Fore.RED}░█──░█ {Fore.GREEN}░█─── {Fore.YELLOW}░█──░█ {Fore.GREEN}░█▄▄▀ {Fore.RED}░█─ {Fore.CYAN}─▄▄▄▀▀ {Fore.RED}░█▀▀▀ {Fore.GREEN}░█▄▄▀ {Style.RESET_ALL}\n"
f"{Fore.RED}░█─░█ {Fore.GREEN}░█▄▄▄█ {Fore.YELLOW}░█▄▄█ {Fore.GREEN}▄█▄ {Fore.RED}▄█▄ {Fore.CYAN}░█▄▄█ {Fore.RED}░█▄▄▄█ {Fore.GREEN}░█▄▄█ {Fore.YELLOW}░█▄▄▄█ {Fore.GREEN}░█─░█ {Fore.RED}▄█▄ {Fore.CYAN}░█▄▄▄█ {Fore.RED}░█▄▄▄ {Fore.GREEN}░█─░█ {Style.RESET_ALL}\n\n"
)
print(ascii_art)


# Clone or download
git clone https://github.com/Graybyt3/ASCII-COLORIZER-PYTHON.git
cd ASCII-COLORIZER-PYTHON

# Install colorama (if not already installed)
pip install colorama

# Run
python ASCII-COLORIZER-PYTHON.py
