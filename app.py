import os
import sys
from flask import (
                Flask, 
                request, 
                abort, 
                jsonify
                )
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
from models import (
                  db, 
                  Actor, 
                  Movie, 
                  setup_db
                  )

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  migrate = Migrate(app, db)
  CORS(app)



  '''
***************************************
END POINTS
***************************************
  '''

  @app.route('/')
  def index():
    return jsonify({'message': 'Welcome to My api_name'})


  '''
***************************************
ACTORS END POINTS
***************************************
  '''


  @app.route("/actors", methods=["GET"])
  @requires_auth("get:actors")
  def get_all_actors(token):
    try:
      all_actors = Actor.query.all()
      if not all_actors:
        abort(404)

      actors = [actor.format() for actor in all_actors]

      return jsonify({
          "success": True, 
          "actors": actors,
          "total_actors": len(actors),
          }),200
      

    except:
      print(sys.exc_info())
      abort(402)

    finally:
      db.session.close()

  @app.route("/actors/<int:actor_id>", methods=["GET"])
  @requires_auth("get:actors")
  def get_actor_by_id(token, actor_id):
    try:
      actor = Actor.query.get(actor_id)

      if not actor:
        abort(404)

      actor = actor.format()

      return jsonify({
          "success": True, 
          "actor": actor,
          }), 200
      
    except:
      print(sys.exc_info())
      abort(402)

    finally:
      db.session.close()

  @app.route("/actors", methods=["POST"])
  @requires_auth("post:actor")
  def add_actor(token):

    try:
      body = request.get_json()

      if not body:
        print(sys.exc_info())
        abort(422)
      
      name = body.get("name")
      age = body.get("age")
      gender = body.get("gender")
      
      new_actor = Actor(
        name=name,
        age=age,
        gender=gender
      )

      # uses the insert func
      new_actor.insert()


      return jsonify({
        "success": True,
        "new_actor_id": new_actor.id
      })
    
    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()


  @app.route("/actors/<int:actor_id>", methods=["DELETE"])
  @requires_auth("delete:actor")
  def delete_actor(token,actor_id):
    try:
        # get the question by id 
        actor = Actor.query.get(actor_id)

        if not actor:
          print(sys.exc_info())
          abort(422)

        # uses the delete func
        actor.delete()

        return jsonify( {
            "success": True,
            "id": actor_id
        }),200
        

    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()


  @app.route("/actors/<int:actor_id>", methods=["PATCH"])
  @requires_auth("patch:actor")
  def patch_actor(token,actor_id):
    try:
      actor = Actor.query.get(actor_id)

      if not actor:
        abort(404)
      
      body = request.get_json()
      if not body:
        abort(422)
      
      name = body.get("name")
      age = body.get("age")
      gender = body.get("gender")

      actor.name = name
      actor.age = age
      actor.gender = gender

      # uses the update func
      actor.update()

      return jsonify({
        "success": True,
        "actor_id": actor.id
      })

    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()


  '''
  ***************************************
  MOVIES END POINTS
  ***************************************
  '''

  @app.route("/movies", methods=["GET"])
  @requires_auth("get:movies")
  def get_all_movies(token):
    try:
      all_movies = Movie.query.all()
      if not all_movies:
        abort(422)

      movies = [movie.format() for movie in all_movies]

      return jsonify({
          "success": True, 
          "movies": movies,
          "total_movies": len(movies),
          }), 200
      
    except:
      print(sys.exc_info())
      abort(402)

    finally:
      db.session.close()

  @app.route("/movies/<int:movie_id>", methods=["GET"])
  @requires_auth("get:movies")
  def get_movie_by_id(token, movie_id):
    try:
      movie = Movie.query.get(movie_id)
      if not movie:
        abort(404)

      movie = movie.format()

      return jsonify({
          "success": True, 
          "movie": movie,
          }), 200
      
    except:
      print(sys.exc_info())
      abort(402)

    finally:
      db.session.close()


  @app.route("/movies", methods=["POST"])
  @requires_auth("post:movie")
  def add_movie(token):
    try:
      body = request.get_json()

      if not body:
        print(sys.exc_info())
        abort(422)
      
      title = body.get("title")
      release_date = body.get("release_date")
      
      new_movie = Movie(
        title=title,
        release_date=release_date
      )

      # uses the insert func
      new_movie.insert()


      return jsonify({
        "success": True,
        "new_movie_id": new_movie.id
      })
    
    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()



  @app.route("/movies/<int:movie_id>", methods=["DELETE"])
  @requires_auth("delete:movie")
  def delete_movie(token, movie_id):
    try:
        # get the question by id 
        movie = Movie.query.get(movie_id)
        if not movie:
          abort(422)

        # uses the delete func
        movie.delete()

        return jsonify({
        "success": True,
        "id": movie_id
        }), 200
        

    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()

  @app.route("/movies/<int:movie_id>", methods=["PATCH"])
  @requires_auth("patch:movie")
  def patch_movie(token, movie_id):
    try:
      movie = Movie.query.get(movie_id)

      if not movie:
        abort(404)
      
      body = request.get_json()
      if not body:
        abort(422)
      
      title = body.get("title")
      release_date = body.get("release_date")

      movie.title = title
      movie.release_date = release_date

      # uses the update func
      movie.update()

      return jsonify({
        "success": True,
        "actor_id": movie.id
      })

    except:
        print(sys.exc_info())
        db.session.rollback()
        abort(500)

    finally:
        db.session.close()





  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": ("unprocessable", error)
                      }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
                      "success": False, 
                      "error": 400,
                      "message":  ("bad request", error)
                      }), 400

  @app.errorhandler(404)
  def ressource_not_found(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": ("resource not found", error)
                      }), 404

  @app.errorhandler(AuthError)
  def authentification_failed(AuthError): 
      return jsonify({
                      "success": False, 
                      "error": AuthError.status_code,
                      "message": AuthError.error['description']
                      }), AuthError.status_code

  return app

app = create_app()




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)