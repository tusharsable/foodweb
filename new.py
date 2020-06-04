import requests
import pandas as pd

def excelfinal(data):
    data=pd.DataFrame(data.json())
    print(data)
    return 'excel'

def dateMatch(date1):
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
        result = dateMatch(date1)


@app.route('/excel', methods=['GET'])
def excelreturn():

    result = excelfinal(resp)

   
    return result
if __name__ == '__main__':
    app.run()

