class Post:
	def __init__(self, post_id = '', subreder = '', timestamp = '', author_id = '', title = '', content = '', is_textpost = True):
		self.post_id = post_id
		self.subreder = subreder
		self.author_id = author_id
		self.timestamp = timestamp
		self.title = title
		self.content = content
		self.is_textpost = is_textpost