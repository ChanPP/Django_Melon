from bs4 import BeautifulSoup
import requests
import lxml


class artist_crawler:

    def __init__(self, img_profile, name, real_name,
                 nationality, birth_date, constellation,
                 blood_type, intro):
        self.img_profile = img_profile
        self.name = name
        self.real_name = real_name
        self.nationality = nationality
        self.birth_date = birth_date
        self.constellation = constellation
        self.blood_type = blood_type
        self.intro = intro

    # def melon_artist_crawler(name):
        # url = f"https://www.melon.com/search/total/index.htm?q={name}&section=&ipath=srch_form"
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "lxml")
        # artist_id = soup.find("div", {"class": "info_01"}).input['value']

        '''
        위쪽은 이름으로 검색하는법
        위쪽 주석처리하고
        def melon_artist_crawler(artist_id):
        추가하면 artist_id로 검색함
        '''
    def melon_artist_crawler(artist_id):
        url = f"https://www.melon.com/artist/detail.htm?artistId={artist_id}"
        response = requests.get(url)
        source = response.text
        soup = BeautifulSoup(source, "lxml")
        div_list = soup.find("div", {"id": "conts"})
        dl_list = soup.find("div", {"class": "section_atistinfo04"}).find("dl")
        dd_list = soup.find("div", {"class": "section_atistinfo04"}).findAll("dd")
        dt_list = soup.find("div", {"class": "section_atistinfo04"}).findAll("dt")
        img_profile = div_list.find("span", {"id": "artistImgArea"}).img['src'][:-70]
        name = div_list.find("div", {"class": "wrap_atist_info"}).p.text[5:].split()

        #가수명 뒤에 본명 날림
        if len(name) == 1:
            name = name[0]
        elif len(name) == 2:
            name = name[0]
        elif len(name) == 3:
            name = name[0] + " " + name[1]
        else:
            name = name[0] + " " + name[1] + " " + name[2]

        intro = soup.find("div", {"id": "d_artist_intro"}).text
        result = {}
        k = len(dd_list)
        result["name"] = name
        result['img_profile'] = img_profile
        for i in range(k):
            result[dt_list[i].text] = dd_list[i].text
        result['intro1'] = intro

        #django model과 이름맞춤
        if not result.get("본명"):
            pass
        else:
            result['real_name'] = result["본명"]
            del result["본명"]

        if not result.get("키/몸무게"):
            pass
        else:
            del result["키/몸무게"]

        if not result.get("별명"):
            pass
        else:
            del result["별명"]

        if not result.get("국적"):
            pass
        else:
            result['nationality'] = result["국적"]
            del result["국적"]

        if not result.get("생일"):
            pass
        else:
            result['birth_date'] = result["생일"]
            del result["생일"]

        if not result.get("별자리"):
            pass
        else:
            result['constellation'] = result["별자리"]
            del result["별자리"]

        if not result.get("혈액형"):
            pass
        else:
            result["blood_type"] = result["혈액형"]
            del result["혈액형"]

        if not result.get("intro1"):
            pass
        else:
            result["intro"] = result["intro1"]
            del result["intro1"]

        return result


'''
데이터가 리스트의 dict처럼 나옴
'''
# n = 0
# result = []
# while True:
#     result.append({
#         dt_list[n].text: dd_list[n].text
#     })
#     n += 1
#     if len(dd_list) == n:
#         break
# print(result)


'''
dd_list6개 아닐경우 에러남
'''
# nationality = dd_list[1].text
# birth_date = dd_list[2].text
# constellation = dd_list[4].text
# blood_type = dd_list[5].text
# intro = soup.find("div", {"id": "d_artist_intro"}).text.strip()
# result = {
#     "name": name,
#     "img_profile": img_profile,
#     "real_name": real_name,
#     "nationality": nationality,
#     "birth_date": birth_date,
#     "constellation": constellation,
#     "blood_type": blood_type,
#     "intro": intro,
#     }
# return result


if __name__ == "__main__":
    name = input("이름을 입력하세요")
    # name = "박효신"
    ac = artist_crawler.melon_artist_crawler(name)
    print(ac)
