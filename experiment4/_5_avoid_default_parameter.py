def add_task(task_name,task_list=None):
    # fix default parameter
    # only string can use"+" directly
    if task_list==None:
        task_list=[]
    task_list.append(task_name)
    return task_list
if __name__=="__main__":
    print(f"1.{add_task("for_you",["Here",1])}")
    print(f"2.{add_task("for_you")}")
