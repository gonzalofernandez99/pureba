from RPA.Robocorp.WorkItems import WorkItems
import os
from RPA.Excel.Files import Files
from RPA.Tables import Tables

def minimal_task():
    
    ws = Files()
    tables = Tables()
    artifacts_dir = os.path.join(os.getcwd(), 'output')
    Excel = os.path.join(artifacts_dir, 'prueba.xlsx')
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
        
    headers = ["title", "date", "description", "name_file", "number_of_phrases", "contains_money"]
    Data = ("title2", "d2ate", "desc2ription", "name_f2ile", "number_2of_phrases", "conta2ins_money")
    
    table = tables.create_table(data=Data, columns=headers)
    ws.create_workbook(path=Excel,sheet_name="hoja1",fmt="xlsx")
    ws.append_rows_to_worksheet(content=table,name="hoja1",header=True)
    ws.save_workbook()
    
    wi = WorkItems()
    wi.get_input_work_item()
    customers = wi.get_work_item_variable("customers")
    print(customers)
    
    
    
if __name__ == "__main__":
    minimal_task()
