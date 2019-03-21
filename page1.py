from flask import Flask, render_template,request,redirect
import csv


app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return render_template('title.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/imp_info')
def impinfo():
    return render_template('ImpInfo.html')

@app.route('/signup_as_hospital')
def signup2():
    return render_template('signup2.html')



@app.route('/signup_as_hospital', methods = ['POST', 'GET'])
def signuph():
    if request.method == 'POST' :
        hospitalinfo = request.form
    d={}
    d=hospitalinfo
    d=d.to_dict(flat=False)
    print "hosp",d
    create_hospital_database(d)
    return render_template('hospitalhomepage.html')

@app.route('/bb')
def signin3():
    return render_template('signin3.html')

@app.route('/signup_as_donor')
def signup1():
    return render_template('signup1.html')


@app.route('/signup_as_donor', methods = ['POST', 'GET'])
def signupd():
    if request.method == 'POST' :
       donorinfo = request.form
    d={}
    d=donorinfo
    d=d.to_dict(flat=False)
    print "DONOR",d
    create_donor_database(d)
    return render_template('thank.html')
@app.route('/signin_as_hospital')
def signin2():
    return render_template('signin2.html')
@app.route('/signin_as_donor')
def signin1():
    return render_template('signin1.html')
@app.route('/signin_as_donor', methods = ['POST', 'GET'])
def signind():
    if request.method == 'POST' :
       donorcred = request.form
    d={}
    d=donorcred
    d=d.to_dict(flat=False)
    if(check_donor_cred(d)):
        return render_template('donorhomepage.html')
    else:
        return render_template('signin1.html')
@app.route('/confirm')
def confirm():
    return render_template('confirm.html')
    
@app.route('/signin_as_hospital', methods = ['POST', 'GET'])
def signinh():
    if request.method == 'POST' :
        hospitalinput = request.form
    return render_template('hospitalhomepage.html')
##@app.route('/signin_as_donor', methods = ['POST', 'GET'])
##def signind():
##    if request.method == 'POST' :
##        donorinput = request.form
##    return render_template('thank.html')


def create_donor_database(d):
    with open('donor_database.csv', mode='a+') as csv_file:
        fieldnames = ['Name', 'Username', 'Password', 'Blood Group', 'Address', 'Phone Number', 'Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
    #show(fieldnames)
def create_hospital_database(d):
    with open('hospital_database.csv', mode='a+') as csv_file:
        fieldnames = ['Name','Password','Address', 'Phone Number','Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
        #show(fieldnames)
def check_donor_cred(d):                                                    '''error occcurs in checking credentials'''
    with open('donor_database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
##        reader_file = csv_reader(f)
##        row_count = len(list(reader_file))
##    with open('donor_database.csv', mode='r') as f:
##        i=1
##        while(i<=row_count):
##            if row['Name']==d['uname'] and row['Password']==d['pass']:
##                f=1
##                break
##            i+=1
##        if(f):
##            return True
##        else:
##            return False
        f=0
        
        count =1
        for row in csv_reader:
            str_uname = ''.join(d['uname'])
            str_pass = ''.join(d['pass'])
            #uname=row['Username'].encode('ascii','ignore')
            #password=row['Password'].encode('ascii','ignore')
            uname=str(row['Username'])
            password=str(row['Password'])
            print "string",str_uname,str_pass
            print "data",row['Username'],row['Password']
            print type(row['Username']),type(d['uname'])
            if count!=1 and (row['Username']==str_uname) and (row['Password']==str_pass):
                f=1
                print"HIIIIII"
                break
            count+=1
        
        if(f):
            return True
        else:
            return False
                
            
            
    

def show(fieldnames):
    with open('hospital_database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                for i in fieldnames:
                    print "\t",i
                line_count += 1 
            print "\t",row['Name'], row['Password'], row['Address'], row['Phone Number'], row['Email']
            line_count += 1

@app.route('/donor_dash')
def banklist():
    return render_template('donorhomepage.html')




if __name__ == '__main__':
    app.run(debug=True)
