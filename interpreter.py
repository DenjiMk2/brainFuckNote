# coding: utf-8
import sys

stack = []
memory = {}
pointer = 0
while True :
  program = input()
  program_counter = 0

  while True :
    if pointer not in memory :
      memory[pointer] = 0

    if program[program_counter] == '>' :
      pointer += 1
    elif program[program_counter] == '<' :
      pointer -= 1
    elif program[program_counter] == '+' :
      memory[pointer] += 1
    elif program[program_counter] == '-' :
      memory[pointer] -= 1
    elif program[program_counter] == '.' :
      sys.stdout.write('%c' % memory[pointer])
    elif program[program_counter] == ',' :
      memory[pointer] = ord(sys.stdin.read(1))
    elif program[program_counter] == '[' :
      if memory[pointer] :
        stack.append(program_counter)
      else :
        bracket_count = 0
        while True :
          if program[program_counter] == '[' :
            bracket_count += 1
          elif program[program_counter] == ']' :
            bracket_count -= 1
            if bracket_count == 0 :
              break
          program_counter += 1
    elif program[program_counter] == ']' :
        program_counter = stack.pop() - 1
    elif program[program_counter] == 'd':
        print(memory)
        print(pointer)
    else :
      pass
    program_counter += 1

    if program_counter == len(program) :
      break
