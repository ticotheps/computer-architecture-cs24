import sys

PRINT_BEEJ      = 1 # 0000 0001
HALT            = 2 # 0000 0010
PRINT_NUM       = 3
SAVE            = 4 # Saves a value to a register
PRINT_REGISTER  = 5
ADD             = 6

memory = [
  PRINT_BEEJ,
  SAVE,
  65,
  2,
  SAVE,
  20,
  3,
  ADD, 
  2,
  3,
  PRINT_REGISTER,
  2,
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
    pc += 1
  
  elif command == PRINT_NUM:
    num = memory[pc + 2]
    print(num)
    pc += 2
    
  elif command == HALT:
    running = False
    pc += 1
    
  elif command == SAVE:
    num = memory[pc + 1]
    reg = memory[pc + 2]
    register[reg] = num
    pc += 3
    
  elif command == ADD:
    reg_a = memory[pc + 1]
    reg_b = memory[pc + 2]
    register[reg_a] += register[reg_b]
    pc += 3
    
  elif command == PRINT_REGISTER:
    reg = memory[pc + 1]
    print(register[pc])
    pc += 1
    
  else:
    print("Error: Unknown command: {command}")
    sys.exit(1)