while s:=input(''):
    match s.split():
        case ["mov", r1,r2]:
            res=f"moving{r2} to {r1}"
        case ["push" | "pop" as cmd, *regs]:
            res=f"{cmd}ing"
        case [cmd, r1]:
            res=f"making {cmd} with {r1}"
        case _:
            res= "Parse error"
    print(res)
