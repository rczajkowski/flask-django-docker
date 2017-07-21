import json
import unittest
from microservice import app, database, create_test_app


class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = create_test_app()
        self.client = app.test_client(self)
        database.create_all()
        self.user = json.dumps({u'username': 'testuser', u'password': 'tespassword'})
        self.headers = {'content-type': 'application/json'}

    def tearDown(self):
        database.session.remove()
        database.drop_all()

    def test_get_method_user_api(self):
        response = self.client.get('/api/user')
        self.assertEqual(response.status_code, 200)

    def test_ok_JSON(self):
        headers = {'content-type': 'application/json'}
        data = json.dumps({u'username': 'testuser', u'password': 'tespassword'})
        response = self.client.post('/api/user',
                                    data=data, headers=headers
                                    )
        self.assertEqual(response.status_code, 201)

    def test_get_user_by_id(self):
        response = self.client.post('/api/user', data=self.user, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        result = self.client.get('/api/user/1')

        self.assertEqual(result.status_code, 200)

    def test_user_edit(self):
        response = self.client.post('/api/user', data=self.user, headers=self.headers)
        self.assertEqual(response.status_code, 201)

        data = json.dumps({u'username': 'edituser'})
        response = self.client.put('/api/user/1', data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)

        result = self.client.get('/api/user/1')
        self.assertIn('edit', str(result.data))

    def test_user_delete(self):
        response = self.client.post('/api/user', data=self.user, headers=self.headers)
        self.assertEqual(response.status_code, 201)

        delete = self.client.delete('/api/user/1')
        self.assertEqual(delete.status_code, 204)

        result = self.client.get('/api/user/1')
        self.assertEqual(result.status_code, 404)

    def test_invalid_JSON(self):
        headers = {'content-type': 'application/json'}
        data = 'not json'
        response = self.client.post('/api/user', data=data, headers=headers)

        self.assertEqual(response.status_code, 400)

    def test_get_notexists_user(self):
        response = self.client.get('/api/user/100')

        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
