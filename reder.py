from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
from typing import Optional
import random

from lib.classes import *
from lib.methods import *

# Test variables:
## These variables will be used for testing and debugging while there is not
## a database to connect to.

from SampleData import *

all_subreders = ['AK47',
				 'AR15',
			     '2Aliberals',
				 'GunPolitics']

featured_subreders = all_subreders

random_id = get_random_id()
random_ids = [get_random_id(),get_random_id(),get_random_id(),get_random_id(),get_random_id(),get_random_id()]

# End test variables

# Temporary config variables
## Config variables will be temporarily defined here until they are moved to a seperate config file.

site_name = 'Reder'
debug_mode = True

# End config variables

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")



@app.get("/")
async def home_page(request: Request):
	return templates.TemplateResponse("StandardLayout.html", {"request": request,
															  "title": site_name,
															  "featured_subs": featured_subreders,
															  "debug_mode": debug_mode})

@app.get("/r/{subreder}")
async def subreder_page(request: Request, subreder: Optional[str] = None):
	return templates.TemplateResponse("StandardLayout.html", {"request": request,
															  "title": site_name,
															  "subreder": subreder,
															  "featured_subs": featured_subreders,
															  "debug_mode": debug_mode})

@app.get("/debug")
async def debug_page(request: Request):
	return templates.TemplateResponse("StandardLayout.html", {"request": request,
															  "title": site_name,
															  "featured_subs": featured_subreders,
															  "debug_mode": debug_mode,
															  "random_ids": random_ids})