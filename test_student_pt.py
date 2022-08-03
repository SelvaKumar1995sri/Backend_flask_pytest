from email.base64mime import body_encode
from email.mime import application
from importlib.resources import contents
import pytest
import json
from student_pt import app,student_collection


@pytest.mark.get_request
def test_add_student():
    res = {"id":6,"name":"surya", "age":"23", "city":"Agra"}
    response = app.test_client().post('/addfilm',data=json.dumps(res),content_type='application/json')

    assert res['id'] == 6
    assert res['name'] == 'surya'
    assert response.status_code == 200
    
@pytest.mark.get_request
def test_view_student():
    response = app.test_client().get('/view')

    res = json.loads(response.data.decode('utf-8')).get("Students")
    assert response.status_code == 200
   

def test_delete_student():
    res = {"id":1}
    response = app.test_client().delete('/delete',data=json.dumps(res),content_type='application/json')

    assert response.status_code == 200
    