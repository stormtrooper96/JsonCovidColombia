import datetime
import shutil
import sys
import sqlite3
from time import sleep

import pandas as pd
from pandas.io import sql
import os
from sodapy import Socrata
from datetime import timedelta




def conectToClient():
    client = Socrata("www.datos.gov.co", app_token="EfDNMV8on55zqlVMUyK3CzUW4")
    return client


def getJsoncasesactive(start_datepar,enddate_datepar):
    client = conectToClient()
    formatDateQuery = "%Y-%m-%d"
    start_date = datetime.datetime.strptime(start_datepar, formatDateQuery)
    end_date = datetime.datetime.strptime(enddate_datepar, formatDateQuery)
    day_count = (end_date - start_date).days + 1

    for single_date in (start_date + timedelta(n) for n in range(day_count)):
        count = 0
        printProgressBar(count, day_count, "blah")
        monthF = str(single_date.month) + "/"
        dayF = str(single_date.day) + "/"
        yearf = str(single_date.year) + " "
        fechaparsed = (dayF + monthF + yearf + "0:00:00")


        results = client.get("gt2j-8ykr", fecha_reporte_web=fechaparsed)
        results_df = pd.DataFrame.from_records(results)

        filepath = "foldercases/"
        filepath += (str(single_date.date()) + ".csv")

        if count == 0:
            if not results_df.empty:
                results_df.to_csv(path_or_buf=filepath, mode="w", index=False)
                count += 1
                #sendRecordsTodb(results_df, "db.sqlite", "casos")
        else:
            if not results_df.empty:
                results_df.to_csv(path_or_buf=filepath, mode="w", index=False, header=None)
                count += 1




def printProgressBar(i,max,postText):
    n_bar =10 #size of progress bar
    j= i/max
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {int(100 * j)}%  {postText}")
    sys.stdout.flush()


def cleanfiles(path):
    shutil.rmtree(path)
    os.makedirs(path)

def mergefiles(path):


    all_files = os.listdir(path)
    if len(all_files)>0:

        allfiles2 = []
        for a in all_files:
            allfiles2.append(path + "/" + a)

        df_from_each_file = (pd.read_csv(f, sep=',') for f in allfiles2)
        df_merged = pd.concat(df_from_each_file, ignore_index=True)
        df_merged.to_csv("dbfile"+"/merged.csv")


def  sendRecordsTodb(dataframe,db,table):
    DB=db
    conn = sqlite3.connect(DB)

    datraframeProccesed=pd.DataFrame(dataframe)
    datraframeProccesed.to_sql(name=table, con=conn,if_exists="append")
    conn.close()