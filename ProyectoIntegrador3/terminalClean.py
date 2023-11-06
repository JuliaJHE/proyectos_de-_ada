import os

def clear_terminal():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0
    while number <= 50:
        clear_terminal()  
        print(f'Número: {number}')
        try:
            
            user_input = input("Presiona 'n' para continuar o 'q' para salir: ")
            if user_input.lower() == 'q':
                break
            number += 1
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
