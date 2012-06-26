from com.process.KeywordHyperlinkProcess import *
from com.process.VersionHyperlinkProcess import *
from com.process.ProvisionHyperlinkProcess import *
from com.process.AbbreviationHyperlinkProcess import *


if __name__=='__main__':
	khp=KeywordHyperlinkProcess.KeywordHyperlinkProcess()
	vhp=VersionHyperlinkProcess.VersionHyperlinkProcess()
	phprocess=ProvisionHyperlinkProcess.ProvisionHyperlinkProcess()
	ahp=AbbreviationHyperlinkProcess()
	
	i=1
	for queueItem in khp.queueDao.getAll():
		if i>1:break
		i+=1
		khp.begin(queueItem)
		article=khp.getArticle(queueItem)
		if article:
			khp.log.info("Processing article type:%s id:%s" % (queueItem.contentType,queueItem.targetId))
			article=khp.process(article)
			article=vhp.process(article)
			article=ahp.process(article)
			article=phprocess.process(article)
			khp.updateArticle(article)
		else:
			khp.log.warning("Article type:%s id:%s was not found" %(queueItem.contentType,queueItem.targetId))
		khp.end(queueItem)
	
	for queueItem in khp.queueDao.getByContentTypeStatus(Article.CONTENT_TYPE_LAW,Article.STATUS_WAIT_UPLOAD):
		article=phprocess.getArticle(queueItem)
		if article:
			article.content=phprocess.removeProvisionRelativeArticleLink(article.content)
			phprocess.addProvisionRelativeArticleLink(article)
		else:
			khp.log.warning("Article type:%s id:%s was not found" %(queueItem.contentType,queueItem.targetId))
