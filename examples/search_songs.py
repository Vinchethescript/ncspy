import ncs

client = ncs.Client()


async def main():
    query = "a"  # the song you are looking for
    genre = ""  # the song's genre
    mood = ""  # the song's mood
    artists = []  # the song's artists
    page = 1  # the search's page
    results = await client.search(
        query, genre=genre, mood=mood, artists=artists, page=page
    )
    print(f'Search results for "{query}":')
    for result in results.items:
        print(f"{result.name}:")
        print("Artists:", ", ".join(result.artists))
        # time is always at midnight because
        # NCS does not provide time with date
        print("Release date:", result.release_date)
        print()


client.loop.run_until_complete(main())
