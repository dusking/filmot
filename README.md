# Filmot API Wrapper

![GitHub](https://img.shields.io/github/license/dusking/filmot)
![PyPI](https://img.shields.io/pypi/v/filmot)
![Python](https://img.shields.io/pypi/pyversions/filmot)

Filmot API Wrapper is a Python package that provides easy programmatically access to the
[Filmot.com](https://filmot.com/) search engine. It simplifies searching YouTube videos by words in subtitles,
fetching channel statistics, and historical data.

## Prerequisites

Before using the Filmot API Wrapper, you'll need a RapidAPI account and to register to the Filmot app at:
[Filmot RapidAPI](https://rapidapi.com/Jopik1/api/filmot-tube-metadata-archive/).

## Installation

You can install the package using `pip` directly from PyPI or by cloning the repository from GitHub.

**Install from PyPI:**

```bash
pip install filmot
```

**Install from GitHub (latest development version):**

```bash
pip install git+ssh://git@github.com/dusking/filmot.git --upgrade
```

## Usage

Using this wrapper is straightforward.
It follows the filmot API documentation closely and converts responses into Python objects.
Here's an example of how to use it:

```python
from filmot import Filmot

# Optional: Set your RapidAPI key in the config so you won't need to provide it in the usage.
Filmot.set_rapidapi_key("***")

# Initialize the Filmot client
filmot = Filmot()

# Search in YouTube archive
response = filmot.search("Spill The Beans", limit=3)

# Response holds the first 3 results
print(response)
[<SearchResponse "Spill The Beans"-Gct3b0yoabU>,
 <SearchResponse "Spill The Beans"-Gct3b0yoabU>,
 <SearchResponse "Spill The Beans"-ZViO1Gnp2xA>]

# Get the hit count of the first response
first_response = response[0]
print(first_response.hit_count())

# Get the query hits for first response
first_response.hits_data()
[{'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=771.92s',
  'text': "when the beans are ready we're going to Spill the Beans later on in the day okay later on in the day we're going to spill the uh"},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=11058.16s',
  'text': 'the chat right now we have a lot of gases Spill the Beans everybody can we get some Spill the Beans emojis on the chat going you know this is how we do it'},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=11060.68s',
  'text': 'gases Spill the Beans everybody can we get some Spill the Beans emojis on the chat going you know this is how we do it here on LA flights we always have to'},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=11071.96s',
  'text': "beans we have to stir the beans and once the beans are ready then we'll Spill the Beans pretty cool announcement I I think it's cool"},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=13874.88s',
  'text': "whenever we do cross 35 we're going to Spill the Beans okay and I I promise you you're not going to be disappointed at the"},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=16073.399s',
  'text': "happen and we already have the dates get ready can we get the Spill the Beans emji going can we stir the beans yeah believe it or not if you're"},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=16088.159s',
  'text': "Emoji right custom made that you can use during a live show and it says Spill the Beans okay so first part LA flights goes to New York we're going to be visiting"},
 {'link': 'https://www.youtube.com/watch?v=Gct3b0yoabU&t=16130.439s',
  'text': "else I was going to be a zombie uh let's see are we going to have The Spill the Beans emojis let's say yes we have Cheryl sending five memberships by the"}]

# Convert the response to a Python dictionary
response_dict = first_response.to_dict()
print(response_dict)

# Convert the response to JSON format
response_json = first_response.to_json()
print(response_json)
```

Here's another simple example:

```python
from filmot import Categories, Countries, Language

# Adjust the search query
response = filmot.search("Spill The Beans",
                         category=Categories.GAMING,
                         country=Countries.UNITED_STATES,
                         language=Language.ENGLISH,
                         limit=3)
```

With this wrapper, accessing Filmot.com API becomes easy and intuitive.
Happy coding!
