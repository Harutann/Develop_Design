def execute_param_fn(args,hosei,fn):
    return fn(args,hosei)

execute_param_fn([1,2,3],4,lambda a,b:max(a)+b)
execute_param_fn([1,2,3],4,lambda a,b:min(a)-b)
