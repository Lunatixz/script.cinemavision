from lib.kodijsonrpc import rpc


def getTrailers():
    for m in rpc.VideoLibrary.GetMovies(properties=['trailer', 'mpaa', 'genre'])['movies']:
        trailer = m.get('trailer')

        if not trailer:
            continue

        yield {
            'ID': m['movieid'],
            'url': trailer,
            'rating': m['mpaa'],
            'genres': m['genre'],
            'title': m['label']
        }
