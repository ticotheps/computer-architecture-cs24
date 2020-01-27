import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3

memory = [
  PRINT_BEEJ,
  PRINT_NUM,
  1,
  PRINT_NUM,
  12,
  PRINT_BEEJ, 
  PRINT_NUM,
  37,
  HALT
]

pc = 0
running = True

while running:
  # Execute instructions in memory
  
  command = memory[pc]
  
  if command == PRINT_BEEJ:
    print("Beej!")
    pc += 1
  
  elif command == PRINT_NUM:
    num = memory[pc + 2]
    print(num)
    pc += 2
    
  elif command == HALT:
    running = False
    pc += 1
    
  else:
    print("Error: Unknown command: {command}")
    sys.exit(1)