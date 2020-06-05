import requests
import pandas as pd
from datetime import datetime as dt
import xlsxwriter
from flask import Flask, send_file
from io import BytesIO

def excelfinal(data):
    df=pd.DataFrame(data.json())
    date=[]
    for dtstamp in df['DateTime']:
        date.append((dt.strptime(dtstamp,"%Y-%m-%dT%H:%M:%SZ")).date())

    output = BytesIO()
    endExcel= pd.ExcelWriter(output, engine='xlsxwriter')
    
    df['Date'] = date
    Unique_date=(df['Date'].unique())
    for x in Unique_date:
        newDf = df[df['Date']==x]
        newDf=newDf.drop(['Date'],axis=1)
        newDf.to_excel(endExcel, sheet_name=str(x), index=False)
       

    endExcel.close()
    output.seek(0)
    return output




def datefilter(date1):
    print(date1[0])
    day=date1[0]
    month=date1[1]
    year=date1[2]
   
   

    length_total=0.0
    weight_total=0.0
    quantity_total=0.0
    for record in resp.json():
        
        Rdate=((record['DateTime']).split('T'))[0]
           
        Rdate=Rdate.split('-')
        Ryear=Rdate[0]
        Rmonth=Rdate[1]
        Rday=Rdate[2]

        if ((Rday==day)and(Rmonth==month)and(Ryear==year)):

            length_total=length_total+float (record['Length'])
            weight_total=weight_total+float (record['Weight'])
            quantity_total=quantity_total+float (record['Quantity'])

    result={

        'totalWeight':weight_total,
        'totalLength':length_total,
        'totalQuantity':quantity_total
        }

    #print(result)
    return flask.jsonify(result)




resp = requests.get('https://assignment-machstatz.herokuapp.com/excel')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

import flask
app = flask.Flask(__name__)

@app.route('/')
def home():

    result = '<h1>please enter date in url</h1>'

    return result

@app.route('/<date>', methods=['GET'])
def qdate(date):

    result = ''
    date1 = date.split('-')
    if len(date1) == 3:
        result = datefilter(date1)
    return result

@app.route('/excel', methods=['GET'])
def excelreturn():

    output = excelfinal(resp)
    print(type(output))
   
    return send_file(output,attachment_filename='result.xlsx',as_attachment=True)
if __name__ == '__main__':
    app.run()

