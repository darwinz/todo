

class TestTaskListResource:
    def test_get_empty_list(self, client, db):
        response = client.get('/tasks')
        assert response.status_code == 200
        assert response.get_json() == []

    def test_post_creates_task(self, client, db):
        response = client.post('/tasks', json={'name': 'Buy milk'})
        assert response.status_code == 201
        data = response.get_json()
        assert data['name'] == 'Buy milk'
        assert data['id'] is not None
        assert data['complete'] is False

    def test_post_missing_name_returns_400(self, client, db):
        response = client.post('/tasks', json={'description': 'no name here'})
        assert response.status_code == 400

    def test_get_after_post_returns_task(self, client, db):
        client.post('/tasks', json={'name': 'Buy milk'})
        response = client.get('/tasks')
        assert response.status_code == 200
        tasks = response.get_json()
        assert len(tasks) == 1
        assert tasks[0]['name'] == 'Buy milk'


class TestTaskResource:
    def _create_task(self, client, name='Test task'):
        resp = client.post('/tasks', json={'name': name})
        return resp.get_json()['id']

    def test_get_one(self, client, db):
        task_id = self._create_task(client)
        response = client.get(f'/tasks/{task_id}')
        assert response.status_code == 200
        assert response.get_json()['id'] == task_id

    def test_get_nonexistent_returns_404(self, client, db):
        response = client.get('/tasks/99999')
        assert response.status_code == 404

    def test_put_updates_fields(self, client, db):
        task_id = self._create_task(client, name='Original')
        response = client.put(f'/tasks/{task_id}', json={'name': 'Updated', 'complete': True})
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Updated'
        assert data['complete'] is True

    def test_delete_removes_task(self, client, db):
        task_id = self._create_task(client)
        del_response = client.delete(f'/tasks/{task_id}')
        assert del_response.status_code == 204
        get_response = client.get(f'/tasks/{task_id}')
        assert get_response.status_code == 404
