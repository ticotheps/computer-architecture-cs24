import sys

PRINT_BEEJ = 1
HALT = 2

memory = [
  PRINT_BEEJ,
  PRINT_BEEJ,
  PRINT_BEEJ,
  PRINT_BEEJ, 
  HALT
]

pc = 0
running = True

while running:
  # Execute instructions in memory
  
  command = memory[pc]
  
  if command == PRINT_BEEJ:
    print("Beej!")
    
  elif command == HALT:
    running = False
    
  else:
    print("Error: Unknown command: {command}")
    sys.exit(1)
    
  pc += 1
    