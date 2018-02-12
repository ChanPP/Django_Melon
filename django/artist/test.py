from bs4 import BeautifulSoup
import lxml
import requests


class EpisodeData:

    def __init__(self, episode_id, title, rating, created_date):
        self.episode_id = episode_id
        self.title = title
        self.rating = rating
        self.created_date = created_date

    def get_episode_list(webtoon_id, page):
        url = f"http://comic.naver.com/webtoon/list.nhn?titleId={webtoon_id}&page={page}"
        # params = {
        #     'webtoon_id': self.webtoon_id
        # }
        # print(url)
        response = requests.get(url)
        source = response.text
        soup = BeautifulSoup(source, "lxml", )
        # print(soup)
        # div_list = soup.find("div", {"id": "content"})
        div_list = soup.find("table", {"class": "viewList"}).findAll("tr")
        # url_title = div_list[2].find("td", {"class":"title"}).a.text
        # url_title = div_list[2].find("td", {"class": "title"}).a.text
        # url_thumbnail = div_list[2].findAll("td")[0].a.img['src']
        # url_rating = div_list[2].findAll("td")[2].strong.text
        # url_created_date = div_list[2].findAll("td")[3].text
        # print(url_created_data)
        print(len(div_list))
        result = []
        if len(div_list) == 12:
            k = 2
        else:
            k = 3

        for i in range(k, len(div_list)):
            title = div_list[i].find("td", {"class": "title"}).a.text
            rating = div_list[i].findAll("td")[2].strong.text
            created_date = div_list[i].findAll("td")[3].text
            thumbnail = div_list[i].findAll("td")[0].a.img['src']
            # episode_id = soup.find("div", {"class": "detail"}).h2.text.split()[0]
            episode_id = thumbnail[36:].split("/")[2]
            result.append({
                "title": title,
                "episode_id": episode_id,
                "rating": rating,
                "created_date": created_date,
                "thumbnail": thumbnail,
            })
        return result


if __name__ == '__main__':
    webtoon_id = input("웹툰 아이디를 입력하세요")
    page = input("웹툰페이지를 입력하세요")
    # webtoon_id = 675331   #13개
    # webtoon_id = 119874   #12개
    # webtoon_id = 701081
    # page = 1
    q = EpisodeData.get_episode_list(webtoon_id, page)
    for i in q:
        print(i)