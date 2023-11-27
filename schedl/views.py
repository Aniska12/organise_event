from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector
from datetime import datetime, timedelta
# Create your views here.



db_config = {
        'host': "organise-db.cbcelvacwhjp.us-east-1.rds.amazonaws.com",
        'user': 'root',
        'password': '12345678',
        'database': 'aws_organise',
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

def home(request):
    return render(request,'home.html')

def schedu(request):        
    if request.method=='POST':
        d=request.POST
        a=[]
        for i,j in d.items():
            a.append(str(j))
        cursor.execute("SELECT MAX(event_id) from events;")
        k=cursor.fetchall()
        if(k[0][0]==None):
            k=[[1]]
        query = """INSERT INTO events VALUES('{}','{}','{}','{}','{}','{}');""".format(k[0][0]+1,a[2],a[3],a[4],a[1],a[5])
        cursor.execute(query)
        connection.commit()
    return render(request,'schedule.html')


def upcoming(request):
    if request.method=='POST':
        d=request.POST
        email_id = request.POST.get('email_id')
        event_id = request.POST.get('event_id')
        cursor.execute("INSERT IGNORE INTO participants values({},'{}')".format(event_id,email_id))
        connection.commit()
    
    query = """
    SELECT e.*,u.name FROM events e, user u
    where e.host_id=u.user_id AND e.event_date>=CURDATE() AND e.event_time>=CURTIME() ORDER BY event_date;
    """
    cursor.execute(query)
    data=cursor.fetchall()
    a=[]
    for i in data:
        d={}
        d["id"]=str(i[0])
        d["name"]=str(i[1])
        d["date"]=str(i[2])
        t_obj = datetime.strptime( str(i[3]), '%H:%M:%S')
        d["time"]=str(t_obj.strftime("%I:%M %p"))
        cursor.execute("select count(*) from participants where event_id={}".format(i[0]))
        x=cursor.fetchall()[0][0]
        d["registered"]=str(x)
        d["host"]=i[6]
        d["details"]=str(i[5])
        a.append(d)
    context={"data":a}

    
    return render(request,"upcoming.html",context)


def past(request):
    query = """
    SELECT e.*,u.name FROM events e, user u
    where e.host_id=u.user_id AND e.event_date<=CURDATE() AND e.event_time<=CURTIME() ORDER BY event_date DESC;
    """
    cursor.execute(query)
    data=cursor.fetchall()
    a=[]
    for i in data:
        d={}
        d["id"]=str(i[0])
        d["name"]=str(i[1])
        d["date"]=str(i[2])
        t_obj = datetime.strptime( str(i[3]), '%H:%M:%S')
        d["time"]=str(t_obj.strftime("%I:%M %p"))
        d["host"]=i[6]
        d["details"]=str(i[5])
        a.append(d)
    context={"data":a}
    
    return render(request,"past.html",context)

def get_list_based_on_id(request, item_id):
    query = f"""SELECT email_id FROM participants where event_id={item_id};"""
    cursor.execute(query)
    data=cursor.fetchall()
    ans=[]
    for i in data:
        ans.append(str(i[0]))
    return (JsonResponse({'data_list':ans}))
