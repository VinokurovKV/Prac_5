from math import *

functions = {}
processed_lines = 0

while (s := input()):
  processed_lines += 1
  s = s.strip()

  if s.startswith(":"):
    parts = s[1:].split()
    func_name = parts[0]
    params = parts[1:-1]
    expression = parts[-1]
    functions[func_name] = (params, expression)
  elif s.startswith('quit'):
    parts = s.split(' ', 1)
    if len(parts) > 1:
      format_str = parts[1].strip('"')
    else:
      format_str = "{} {}"
    
    result = format_str.format(len(functions) + 1, processed_lines)
    print(result)
    break
  else:
    parts = s.split()
    func_name = parts[0]
    args = parts[1:]

    if func_name in functions:
      params, expression = functions[func_name]

      if len(params) == 1 and len(args) > 1:
        args = [' '.join(args)]

      context = {}
      for i, param in enumerate(params):
        if i < len(args):
          if args[i].replace('.', '').replace('-', '').isdigit():
            context[param] = float(args[i])
          else:
            context[param] = args[i].strip('"')
        else:
          context[param] = None
      
      result = eval(expression, globals(), context)
      print(result)