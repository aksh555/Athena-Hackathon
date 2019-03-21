from flask import Flask, render_template,request,redirect
import csv


app = Flask(__name__,static_url_path='')
def create_donor_database_headings():
    fieldnames = ['Name', 'Username', 'Password', 'Blood Group', 'Address', 'Phone Number', 'Email']
    with open('donor_database.csv', mode='a+') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
#create_donor_database_headings()

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


@app.route('/bb')
def signin3():
    return render_template('signin3.html')





@app.route('/signin_as_hospital')
def signin2():
    return render_template('signin2.html')

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

'''Donor '''


@app.route('/signup_as_donor')
def signup1():
    return render_template('signup1.html')


@app.route('/signup_as_donor', methods = ['POST', 'GET'])
def signupd():
    
    if request.method == 'POST' :
       name=str(request.form['Name'])
       uname=str(request.form['Username'])
       pw=str(request.form['Password'])
       bg=str(request.form['Blood Group'])
       add=str(request.form['Address'])
       pno=str(request.form['Phone Number'])
       email=str(request.form['Email'])
    
##    d={}
##    d=donorinfo
##    d=d.to_dict(flat=False)
##    print "\nDONOR DICT",d
    create_donor_database(name,uname,pw,bg,add,pno,email)
    return render_template('thank.html')

def create_donor_database(name,uname,pw,bg,add,pno,email):
    d={}
    s=""
    l=[name,uname,pw,bg,add,pno,email]
    for i in l:
        i+=" "
        s+=i
    d[uname]=s
    with open('donor_database.csv', mode='a+') as f:
        w = csv.writer(f)
        w.writerow(d.values())
   
    #show()



        
@app.route('/signin_as_donor')
def signin1():
    return render_template('signin1.html')
@app.route('/signin_as_donor', methods = ['POST', 'GET'])
def signind():
    if request.method == 'POST' :
        duname = str(request.form['uname'])
        dpass=str(request.form['pass'])
        
    if(check_donor_cred(duname,dpass)):
        return render_template('donorhomepage.html')
    else:
        return render_template('signin1.html')

def show():
    fieldnames = ['Name', 'Username', 'Password', 'Blood Group', 'Address', 'Phone Number', 'Email']
    with open('donor_database.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print "\t",row
            

def check_donor_cred(duname,dpass):                                                    
    with open('donor_database.csv', mode='r') as f:
        csv_reader = csv.reader(f)
        f=0
        for row in csv_reader:
                l=row[0].split()
                if l[1]==duname and l[2]==dpass:
                    f=1
                    break
            
            
        
##        reader_file = csv_reader(f)
##        row_count = len(list(reader_file))
##    with open('donor_database.csv', mode='r') as f:
##        i=1
##        while(i<=row_count):
##            if row['Name']==d['uname'] and row['Password']==d['pass']:
##                f=1
##                break
##            i+=1
        if(f):
            return True
        else:
            return False
        
##        
##        count =1
##        for row in csv_reader:
##            str_uname = ''.join(d['uname'])
##            str_pass = ''.join(d['pass'])
##            #uname=row['Username'].encode('ascii','ignore')
##            #password=row['Password'].encode('ascii','ignore')
##            uname=str(row['Username'])
##            password=str(row['Password'])
##            print "string",str_uname,str_pass
##            print "data",row['Username'],row['Password']
##            print type(row['Username']),type(d['uname'])
##            if count!=1 and (row['Username']==str_uname) and (row['Password']==str_pass):
##                f=1
##                print"HIIIIII"
##                break
##            count+=1
##        
'''hospital'''

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
   
                
def create_hospital_database(d):
    with open('hospital_database.csv', mode='a+') as csv_file:
        fieldnames = ['Name','Password','Address', 'Phone Number','Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
        #show(fieldnames)            
            
    



@app.route('/donor_dash')
def banklist():
    return render_template('donorhomepage.html')




if __name__ == '__main__':
    app.run(debug=True)
