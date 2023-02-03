from datetime import date
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db_drop_and_create_all, Actor, Movie, db_drop_and_create_all, database_path
from env.config import tokens


casting_assistant_auth_header = {
    "Authorization": tokens["casting_assistant"]
}

casting_director_auth_header = {
    "Authorization": tokens["casting_director"]
}

executive_producer_auth_header = {
    "Authorization": tokens["executive_producer"]
}


class CapstoneTestCase(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # ****************************************
    # /GET ACTORS
    # ****************************************

    def test_get_all_actors(self):
        """Test GET all actors."""
        res = self.client().get("/actors", headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["actors"]) > 0)

    def test_error_401_get_all_actors(self):
        """Test GET all actors w/o Authorization."""
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])

    def test_get_actor_by_id(self):
        """Test GET spesific actor."""
        res = self.client().get("/actors/1", headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_error_401_get_actor_by_id(self):
        """Test GET spesific actor that dont exist."""
        res = self.client().get("/actors/888")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
    

    # ****************************************
    # /GET MOVIES
    # ****************************************


    def test_get_all_movies(self):
        """Test GET all movies."""
        res = self.client().get("/movies", headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movies"]) > 0)

    def test_error_401_get_all_movies(self):
        """Test GET all movies w/o Authorization."""
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])

    def test_get_movie_by_id(self):
        """Test GET spesific actor."""
        res = self.client().get("/movies/1", headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_error_401_get_movie_by_id(self):
        """Test GET spesific actor that dont exist."""
        res = self.client().get("/movies/888")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])


    # ****************************************
    # /POST ACTORS
    # ****************************************

    def test_add_new_actor(self):
        new_actor = {
            "name": "test",
            "age": 5,
            "gender": "M"
        }

        res = self.client().post('/actors', json = new_actor, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_new_actor(self):
        new_actor = {
            "name": "test",
            "age": 5,
            "gender": "M"
        }

        res = self.client().post('/actors', json = new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


    # ****************************************
    # /POST MOVIES
    # ****************************************

    def test_add_new_movie(self):
        new_movie = {
            "title": "test",
            "release_date": date.today()
        }

        res = self.client().post('/movies', json = new_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_new_movie(self):
        new_movie = {
            "title": "test",
            "release_date": date.today()
        }

        res = self.client().post('/movies', json = new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    # ****************************************
    # /PATCH ACTORS
    # ****************************************

    def test_patch_actor(self):
        """Test PATCH existing actors"""
        to_update = {
            'name' : "test"
        } 
        res = self.client().patch('/actors/1', json = to_update, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_patch_actor(self):
        """Test PATCH existing actors"""
        to_update = {
            'name' : "test"
        } 
        res = self.client().patch('/actors/1', json = to_update)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


    # ****************************************
    # /PATCH MOVIES
    # ****************************************

    def test_patch_movie(self):
        """Test PATCH existing movies"""
        to_update = {
            'name' : "test"
        } 
        res = self.client().patch('/movies/1', json = to_update, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_patch_movie(self):
        """Test PATCH existing movies"""
        to_update = {
            'name' : "test"
        } 
        res = self.client().patch('/movies/1', json = to_update)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


    # ****************************************
    # /DELETE ACTORS
    # ****************************************

    def test_delete_actor(self):
        """Test DELETE existing movie"""
        res = self.client().delete('/actors/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_delete_actor(self):
        """Test DELETE existing movie"""
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


    # ****************************************
    # /DELETE MOVIES
    # ****************************************

    def test_delete_movie(self):
        """Test DELETE existing movie"""
        res = self.client().delete('/movies/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_error_401_delete_movie(self):
        """Test DELETE existing movie"""
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


if __name__ == "__main__":
    unittest.main()