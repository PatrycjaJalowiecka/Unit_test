##import tmdb_client
##from unittest.mock import Mock
##from tmdb_client import call_tmdb_api

##API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTE0MWU4M2U5ODY5MWE5OGYxNGRhNjRkNjQ1NWY4OSIsInN1YiI6IjYwNGEwZjc4NDM5YmUxMDAyNjU3YjIwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WXhkUNFWW-yyFcI4GjaStAkDv64TQ6T8n19gA686OTQ"


##def call_tmdb_api(endpoint):
  ## full_url = f"https://api.themoviedb.org/3/{endpoint}"
   ##headers = {
     ##  "Authorization": f"Bearer {API_TOKEN}"
  ## }
   ##response = requests.get(full_url, headers=headers)
   ##response.raise_for_status()
   ##return response.json()

##def get_movies_list(list_type):
  ## return call_tmdb_api(f"movie/{list_type}")

