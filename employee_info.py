import pandas as pd
import sqlparse
from connect_oracle import DatabaseConnectionManager
import xlsxwriter #as xslx
# from xlsxwriter import Workbook


class EmployeeInfo:
    def __init__(self,dbmanager):
        self.dbmanager = dbmanager

    def get_highest_paid_emps(self):
        sql = """Select emp.employee_id,emp.first_name, emp.last_name from employees emp inner join
                        (select max(salary) as maxSalary,   department_id from employees group by department_id)  dep 
                        ON emp.department_id = dep.department_id 
                        and emp.salary = dep.maxsalary """
        return self.dbmanager.run_sql(sql)

    def get_lowest_paid_emps(self):
        print('inside get_lowest_paid_emps')
        sql = """Select emp.employee_id,emp.first_name, emp.last_name, emp.salary from employees emp inner join
                        (select min(salary) as maxSalary,   department_id from employees group by department_id)  dep 
                        ON emp.department_id = dep.department_id 
                        and emp.salary = dep.maxsalary """
        salary_report_df = pd.read_sql(sql,con=self.dbmanager.conn)
        return salary_report_df

    def salary_increament_report(self,increment):
        print(increment)
        df = self.get_lowest_paid_emps()
        df['INCREAMENTED_SALARY'] = df['SALARY']+  (df['SALARY']/increment)
        writer = pd.ExcelWriter('salary_increament_report.xlsx',engine= 'xlsxwriter')
        df.to_excel(writer,sheet_name='report',index=False,)
        writer._save()


    # def salary_increament_report(self,increment):
    #     print(increment)
    #     workbook = xlsxwriter.Workbook('salary_increament_report.xlsx')
    #     worksheet = workbook.add_worksheet('report')
    #
    #     for r, row in enumerate(self.get_lowest_paid_emps()):
    #         for c, col in enumerate(row):
    #             worksheet.write(r,c,col)
    #     workbook.close()

    #def salary_increament_report(self, increment):







