from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
from typing import Optional

# Test variables:
## These variables will be used for testing and debugging while there is not
## a database to connect to.

featured_subreders = ['AK47',
					  'AR15',
					  '2Aliberals',
					  'GunPolitics']

# End test variables

site_name = 'Reder'

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

class Post:
	def __init__(self, post_id, subreder, timestamp, author_id, title, content, is_textpost):
		self.post_id = post_id
		self.subreder = subreder
		self.author_id = author_id
		self.timestamp = timestamp
		self.title = title
		self.content = content
		self.is_textpost = is_textpost



@app.get("/")
async def home_page(request: Request):
	return templates.TemplateResponse("StandardLayout.html", {"request": request,
															  "title": site_name,
															  "featured_subs": featured_subreders})

@app.get("/r/{subreder}")
async def subreder_page(request: Request, subreder: Optional[str] = None):
	return templates.TemplateResponse("StandardLayout.html", {"request": request,
															  "title": site_name,
															  "subreder": subreder,
															  "featured_subs": featured_subreders})