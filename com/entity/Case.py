from com.core.entity.Article import * 

class Case(Article):
	def __init__(self):
		Article.__init__(self)
		self.content_type='C'