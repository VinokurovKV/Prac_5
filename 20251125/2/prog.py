import math
import operator
import sys

def execute_assembler(program):
    lines = [line.strip() for line in program.split('\n') if line.strip()]
    
    labels = {}
    commands = []
    
    for line in lines:
        if ':' in line:
            label_part, rest = line.split(':', 1)
            label = label_part.strip()
            if label:
                labels[label] = len(commands)
            line = rest.strip()
        
        if line:
            parts = line.split()
            if len(parts) >= 1:
                commands.append(parts)
    
    for cmd in commands:
        if cmd[0].startswith('if') and len(cmd) == 4 and cmd[3] not in labels:
            return
    
    vars = {}
    pc = 0
    
    def get_val(x):
        if x in vars:
            return vars[x]
        try:
            return float(x)
        except:
            return 0.0
    
    while 0 <= pc < len(commands):
        cmd = commands[pc]
        op = cmd[0]
        
        if op == 'stop':
            break
            
        elif op == 'store':
            vars[cmd[2]] = get_val(cmd[1])
            pc += 1
            
        elif op == 'out':
            print(get_val(cmd[1]))
            pc += 1
            
        elif op in ['add', 'sub', 'mul', 'div']:
            a, b = get_val(cmd[1]), get_val(cmd[2])
            try:
                if op == 'add': result = a + b
                elif op == 'sub': result = a - b
                elif op == 'mul': result = a * b
                elif op == 'div': result = a / b
                vars[cmd[3]] = result
            except:
                vars[cmd[3]] = math.inf
            pc += 1
            
        elif op.startswith('if'):
            a, b = get_val(cmd[1]), get_val(cmd[2])
            cond = {
                'ifeq': operator.eq, 'ifne': operator.ne,
                'ifgt': operator.gt, 'ifge': operator.ge, 
                'iflt': operator.lt, 'ifle': operator.le
            }[op]
            
            if cond(a, b):
                pc = labels[cmd[3]]
            else:
                pc += 1
                
        else:
            pc += 1


program = sys.stdin.read()
execute_assembler(program)