from flask import request
import json
import re
import os
import sys
import tabula
import warnings
import tqdm
import sys
import pickle


class invoiceProcessing:

    def __init__(self, invoice_file_path=None):
     
        if not invoice_file_path:
            self.invoice_file_path = request.args.get('invoice_file_path')


        self.invoices_pdf_path = '/data/pdf'
        self.invoices_csv_path = '/data/csv'
        self.raw_path = '/data/raw'

        self.invoice_cols = {
                '0':'cci',
                '1':'descricao',
                '2':'leitura_anterior',
                '3':'leitura_atual',
                '4':'registrado_kw-kwh-kvarh',
                '5':'faturado_kw-kwh-kvarh',
                '6':'tarifa_com_icms',
                '7':'base_icms',
                '8':'aliq_icms',
                '9':'icms',
                '10':'valor',
                '11':'tarifa_sem_impostos',
                }
        
        self.scanning_invoice = self.getDataFrame()
        self.os_getcwd = os.getcwd()
        #self.pattern = pattern - TO DO, a pattern ex: Enel-v1

        

    @classmethod
    def get_path_to_project_dir(cls):
        '''
        get the major project dirpath to model 

        '''

        req = r"\w*.{0,100}invoice_digitizer"
        path = re.findall(req, str(os.getcwd()))
        return path[0]
 
    
    def save_object(self, obj, filename):

        files_path = self.get_path_to_project_dir()
        files_path += self.raw_path
        os.chdir(files_path)

        with open(filename, 'wb') as output:
            pickle.dump(obj, output)


    def read_object(self, filename):

        files_path = self.get_path_to_project_dir()
        files_path += self.raw_path
        os.chdir(files_path)

        with open(filename, 'rb') as f:
            obj = pickle.load(f)

        return obj

    def change_col_name(self, df):
        if df.shape[1] == 12:
            df.columns = list(self.invoice_cols.values())
        return df


    def getDataFrame(self, save_obj=False):
        '''
        return a list of invoice dfs.
        '''


        
        # read 1 invoice
        
        file_path = self.get_path_to_project_dir()
        file_path += self.invoices_pdf_path
        #file_path += self.invoice_file_path

        os.chdir(file_path)
        df = tabula.read_pdf(self.invoice_file_path, pages=1, pandas_options={'header':None})[2]
        
        # apply change name
        df = self.change_col_name(df) 


        self.save_object(df, 'df_digitalized_invoice.pkl')

        return {"invoice": df.to_dict()}
        #return {"invoice": ['asd','asd']}

        #list_df2 = [self.change_col_name(df) for df in list_df]

       # # READ ALL DATAFRAMES #########################################33

       # files_path = self.get_path_to_project_dir()
       # files_path += self.invoices_pdf_path
       # os.chdir(files_path)
       # all_filenames = list(os.listdir())
       # 
       # #list_df = [tabula.read_pdf(f, pages=1, pandas_options={'header':None})[2] for f in all_filenames]
       # 
       # # printing how df is digitalazing
       # list_df = []

       # for f in all_filenames:
       #     print(f"Passando para pandas dataframe o arquivo:{f}")
       #     try:
       #         list_df.append(tabula.read_pdf(f, pages=1, pandas_options={'header':None})[2])
       #     except Exception:
       #         print(f"\nErro no arquivo: {f}")
       #         pass  # or you could use 'continue'


       # # apply change name
       # list_df2 = [self.change_col_name(df) for df in list_df]

       # # save obj as required
       # self.save_object(list_df2, 'list_df2.pkl')
       # return list_df2

    def process_invoice(self, invoice_file_path= None):

        if not invoice_file_path:

            invoice_file_path = request.args.get('invoice_file_path')

        invoice_data = {
            "provider": "placeholder",
            "invoiceCost": 35000,
            "path": invoice_file_path
        }

        return invoice_data        
