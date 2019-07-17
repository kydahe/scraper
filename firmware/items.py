from scrapy.item import Item, Field
#保存爬取数据的容器
class FirmwareImage(Item):
    product = Field(default=None)
    vendor = Field()#制造商

    description = Field(default=None)#描述
    version = Field(default=None)#版本
    build = Field(default=None)#
    date = Field(default=None)#日期

    mib = Field(default=None)
    sdk = Field(default=None)
    url = Field()

    # used by FilesPipeline
    files = Field()
    file_urls = Field()
