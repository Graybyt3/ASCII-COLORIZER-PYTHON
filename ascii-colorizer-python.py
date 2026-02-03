from colorama import Fore, Style, init
import sys
import os
from datetime import datetime

init(autoreset=True)

COLOR_NAMES = ["Fore.RED", "Fore.GREEN", "Fore.YELLOW", "Fore.GREEN", "Fore.RED", "Fore.CYAN"]
ACTUAL_COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.GREEN, Fore.MAGENTA, Fore.CYAN]
#ADD MORE COLORS IF YOU ARE GAY-PAPPU AND LIKE RAINBOWS
def print_header():
    print("\n\n")
    print(f"{Fore.YELLOW}{'═' * 100}{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}                     ꉂ(˵˃ ᗜ ˂˵) {Style.RESET_ALL}{Fore.YELLOW}GRAYBYTE ASCII COLORIZER V 1.0{Style.RESET_ALL}{Fore.GREEN} ✌︎㋡{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 100}{Style.RESET_ALL}\n")

def main():
    print_header()

    lines = []
    empty_count = 0
    print(f"{Fore.YELLOW}📑PASTE PLAIN ASCII ART AND PRESS 'END' OR DOUBLE ENTER.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🔽INPUT:{Style.RESET_ALL}")
    while True:
        try:
            line = input().rstrip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}🤷‍♂️CANCELLED...............{Style.RESET_ALL}")
            sys.exit(0)

        if line.strip().upper() == "END":
            break
        if not line.strip():
            empty_count += 1
            if empty_count >= 2 and lines:
                break
        else:
            empty_count = 0
            lines.append(line)

    if not lines or not any(l.strip() for l in lines):
        print(f"\n{Fore.RED}🤷‍♂️NO FUCKING ART PROVIDED.DON'T BE A FUCKING PAPPU {Style.RESET_ALL}\n")
        return

    print(f"\n{Fore.GREEN}🖼️LIVE PREVIEW ART:{Style.RESET_ALL}\n")
    code_lines = []
    preview_lines = []

    for i, raw_line in enumerate(lines):
        if not raw_line.strip():
            code_lines.append('    ""')
            preview_lines.append("")
            continue

        parts = raw_line.split()
        preview_str = ""
        code_str = ""

        for j, part in enumerate(parts):
            name = COLOR_NAMES[j % len(COLOR_NAMES)]
            color = ACTUAL_COLORS[j % len(ACTUAL_COLORS)]
            preview_str += f"{color}{part} "
            code_str += f"{{{name}}}{part} "

        preview_str += Style.RESET_ALL
        code_str += "{Style.RESET_ALL}"

        
        if i == 0:
            prefix = "\\n\\n"
        else:
            prefix = ""

        if i == len(lines) - 1:
            suffix = "\\n\\n"
        else:
            suffix = "\\n"

        full_inner = prefix + code_str + suffix
        code_line = f'    f"{full_inner}"'
        code_lines.append(code_line)

        
        if i == 0:
            print("\n" + preview_str)
        else:
            print(preview_str)

    
    print(f"\n{Fore.YELLOW}💁READYMADE CODE-BLOCK:{Style.RESET_ALL}\n")
    print("ascii_art = (")
    for cl in code_lines:
        print(cl)
    print(")")
    print("print(ascii_art)")

    filename = "gray_colored_ascii_code.py"
    full_file_content = f'''from colorama import Fore, Style, init
init(autoreset=True)

ascii_art = (
'''
    full_file_content += "\n".join(code_lines)
    full_file_content += '''
)
print(ascii_art)
'''

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_file_content)
        print(f"\n\n{Fore.GREEN}🗃 SAVED AS: {filename}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⏩RUN TO CHECK WITH: python {filename}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}💁FAILED TO SAVE: {e}{Style.RESET_ALL}")

    print(f"{Fore.MAGENTA}💁DONE. COPY THE BLOCK ABOVE OR USE THE SAVED FILE...{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
