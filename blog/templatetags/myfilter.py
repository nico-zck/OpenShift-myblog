from html.parser import HTMLParser

from django import template

from myblog.settings import SITE_DEFAULT_ARTICLE_IMAGE


class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    # 过滤掉UEditor的动画表情，并且gif图通常不适合做封面
                    if not attr[1].endswith('.gif'):
                        self.links.append(attr[1])


register = template.Library()


@register.filter
# 从文章内容中提取已添加图片的路径
def img_links_from_article(content):
    parser = MyParser()
    parser.feed(content)
    src_links = parser.links
    if src_links:
        return src_links[0]
    else:
        return SITE_DEFAULT_ARTICLE_IMAGE
