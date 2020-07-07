import scrapy
from scrapy.selector import Selector
from maoyanspider.items import MaoyanspiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3']

    def start_requests(self):
        cookies='__mta=121598647.1592900334837.1592964093969.1593681575945.8; uuid_n_v=v1; uuid=2C431870B52A11EA801551553EAD9849294F85D8A2FD411AB05474F6441FD1F7; mojo-uuid=dccb9dbc220cf4c092b5420e85073f49; _lxsdk_cuid=172e0423480c8-010a2afd2d26c5-c373667-384000-172e0423480c8; _lxsdk=2C431870B52A11EA801551553EAD9849294F85D8A2FD411AB05474F6441FD1F7; _csrf=7f2051d3564c8e8e85d1f3b6ae88248440d24cbfa3d75118b358dfd07e66cd33; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592900335,1592900480,1592964080,1593655409; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1594105237; __mta=121598647.1592900334837.1593681575945.1594105239204.9; _lxsdk_s=17328325586-ea3-2b5-f71%7C%7C1'
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,cookies=cookies)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            name = movie.xpath('./div/@title')[0].extract().strip()
            eles = movie.xpath(f'//div[@title="{name}"]')
            type_m = eles[1].xpath('./text()')[1].extract().strip()
            time = eles[3].xpath('./text()')[1].extract().strip()
            item = MaoyanspiderItem()

            item['name'] = name
            item['time'] = time
            item['type_m'] = type_m
            yield item
