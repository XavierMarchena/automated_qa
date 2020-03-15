from inspect import getmembers, isfunction

def getTestNames(module):
    functions_list = [o for o in getmembers(module) if isfunction(o[1])]
    functions_names_list = []
    for f in functions_list:
        if f[0].startswith("test"):
            functions_names_list.append(f[0])
    return functions_names_list