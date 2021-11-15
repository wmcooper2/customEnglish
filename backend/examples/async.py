"""asyncio/aiohttp example"""

# std lib
import asyncio
import time

# 3rd party
import aiohttp
import requests


async def single_async():
	start_time = time.time()
	async with aiohttp.ClientSession() as session:
		pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
		async with session.get(pokemon_url) as resp:
			pokemon = await resp.json()
			print(pokemon['name'])
	print("Single Async: --- %s seconds ---" % (time.time() - start_time))
asyncio.run(single_async())

async def many_async():
	start_time = time.time()
	async with aiohttp.ClientSession() as session:
		for number in range(1, 151):
			pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
			async with session.get(pokemon_url) as resp:
				pokemon = await resp.json()
				print(pokemon['name'], end="\r")
	print("Many Async: --- %s seconds ---" % (time.time() - start_time))
asyncio.run(many_async())


def many_sync():
	start_time = time.time()
	for number in range(1, 151):
		url = f'https://pokeapi.co/api/v2/pokemon/{number}'
		resp = requests.get(url)
		pokemon = resp.json()
		print(pokemon['name'], end="\r")
	print("Many Sync: --- %s seconds ---" % (time.time() - start_time))
many_sync()

async def many_async_futures():
	start_time = time.time()
	async def get_pokemon(session, url):
		async with session.get(url) as resp:
			pokemon = await resp.json()
			return pokemon['name']


	async def main():

		async with aiohttp.ClientSession() as session:

			tasks = []
			for number in range(1, 151):
				url = f'https://pokeapi.co/api/v2/pokemon/{number}'
				tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

			original_pokemon = await asyncio.gather(*tasks)
			for pokemon in original_pokemon:
				print(pokemon, end="\r")
	print("Many Async Futures: --- %s seconds ---" % (time.time() - start_time))
asyncio.run(many_async_futures())
