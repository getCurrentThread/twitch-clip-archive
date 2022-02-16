import os
import re
import json
import requests

"""
origin.json is used to store the twitch clips original data.
parsing from https://www.twitch.tv/${streamer_id}/clips?filter=clips&range=all

this works can cause a lot of traffic on Twitch.
so I didn't attach this source code.

please understand this part... ;(

+ If you can, I recommend parsing using Twitch API.
"""