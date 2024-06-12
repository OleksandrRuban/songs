from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

songs = {
    1: {'artist': 'Queen', 'title': 'Bohemian Rhapsody', 'album': 'A Night at the Opera', 'year': 1975, 'duration': '5:55', 'format': 'MP3'},
    2: {'artist': 'Led Zeppelin', 'title': 'Stairway to Heaven', 'album': 'Led Zeppelin IV', 'year': 1971, 'duration': '8:02', 'format': 'MP3'},
    3: {'artist': 'The Beatles', 'title': 'Hey Jude', 'album': 'Single', 'year': 1968, 'duration': '7:11', 'format': 'MP3'}
}

class Song(Resource):
    def get(self, song_id):
        if song_id not in songs:
            return {'message': 'Song not found'}, 404
        return songs[song_id], 200

    def post(self, song_id):
        if song_id in songs:
            return {'message': 'Song already exists'}, 400
        data = request.get_json()
        songs[song_id] = data
        return data, 201

    def delete(self, song_id):
        if song_id not in songs:
            return {'message': 'Song not found'}, 404
        del songs[song_id]
        return '', 204

class SongList(Resource):
    def get(self):
        return songs, 200

api.add_resource(SongList, '/songs')
api.add_resource(Song, '/songs/<int:song_id>')

if __name__ == '__main__':
    app.run(debug=True)
