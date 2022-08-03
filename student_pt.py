
from flask import Flask,request,jsonify


student_collection = [
    {"id":1,"name":"John", "age":"23", "city":"Agra"},
    {"id":2,"name":"Steve", "age":"28", "city":"Delhi"},
    {"id":3,"name":"Peter", "age":"32", "city":"Chennai"},
    {"id":4,"name":"Chaitanya", "age":"28", "city":"Bangalore"}
]

app=Flask(__name__)

@app.route('/addfilm',methods=['post'])
def add_student():
    try:
        val=request.get_json()
        student_collection.append(val)

        return jsonify({"Student_collection": student_collection})

    except Exception as e:
        print("error accures :" +str(e))
        return "failed to add"


@app.route('/delete',methods=['get','delete'])
def delete_student():
    try:
        val=request.get_json('id')
        for i in student_collection:
            if i['id']==val['id']:
                index_i=student_collection.index(i)
                print(index_i)
                del student_collection[index_i]
    
            return jsonify({"Students":student_collection})

    except Exception as e:
        print("Error on updating :" +str(e))


@app.route('/view',methods=['get'])
def view_student():
    try:       
        
        return jsonify({"Students":student_collection})

    except Exception as e:
        print("Error on updating :" +str(e))

if __name__=='__main__':
   app.run(debug=True)