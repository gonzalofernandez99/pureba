from RPA.Robocorp.WorkItems import WorkItems

def minimal_task():
    
    wi = WorkItems()
    wi.get_input_work_item()
    customers = wi.get_work_item_variable("customers")
    print(customers)

if __name__ == "__main__":
    minimal_task()
