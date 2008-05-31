from com.core.dao import *

class CrossRefLinkDAO(DAO):
	table='cross_ref_link'

	def __init__(self):
		DAO.__init__(self)
		self.cursor.execute('use lnc')

	def deleteBySrcId(self,srcId):
		try:
			self.cursor.execute('delete from %s where src_article_id=%s' % CrossRefLinkDAO.table)
			self.conn.commit()
		except Exception,e:
			self.log.error(e)

	def insert(self,crossRefLink):
		try:
			self.cursor.execute("INSERT INTO cross_ref_link(src_article_id,keyword_id,des_article_id,des_item_id,des_attachment_id) VALUES(%s,%s,%s,%s,%s)" % (crossRefLink.srcId,crossRefLink.kId,crossRefLink.desId,crossRefLink.desItemId,crossAttachId))
			self.conn.commit()
		except Exception,e:
			self.log.error(e) 


	def getCrossRefLinkBySrcId(self,srcId):
		"get link between article of src Id"