import re
import ncs

client = ncs.Client()


async def main():
    id = "Destiny"
    result = await client.get_song(id)
    if not result:
        print("No songs were found.")
        return

    print(f'Details of song "{result}":')
    print("Artists:", ", ".join(result.artists))
    # time is always at midnight because
    # NCS does not provide time with date
    print("Release date:", result.release_date)


client.loop.run_until_complete(main())
