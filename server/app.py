from data import get_data
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

normalized_data = get_data()


@app.route("/songs", methods=["GET"])
def get_songs():
    page = int(request.args.get("page", default=1))
    per_page = int(request.args.get("per_page", default=10))

    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_table = normalized_data.iloc[start_index:end_index]
    songs = paginated_table.to_dict("index")
    return list(songs.values())


@app.route("/allSongs", methods=["GET"])
def get_all_songs():
    songs = normalized_data.to_dict("index")
    return list(songs.values())


@app.route("/songs/<title>", methods=["GET"])
def get_song_by_title(title):
    song = normalized_data[normalized_data["title"] == title].to_dict("index")
    if len(song) > 0:
        return list(song.values())

    return jsonify({"message": "Song not found"}), 404


@app.route("/songs/<title>/rate", methods=["POST"])
def rate_song(title):
    song = normalized_data[normalized_data["title"] == title].index

    if len(song) < 1:
        return jsonify({"message": "Song not found"}), 404

    star_rating = int(request.json.get("star_rating", 0))

    if not star_rating:
        return jsonify({"message": "Rating not found"}), 404

    if 0 < star_rating < 6:
        normalized_data.loc[song, "star_rating"] = star_rating
        temp = normalized_data.to_dict("index")
        return list(temp.values())

    return (
        jsonify({"message": "Invalid star rating. Must be between 1 and 5."}),
        404,
    )
