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

    def melon_artist_crawler(artist_id):
        url = f"https://www.melon.com/artist/detail.htm?artistId={artist_id}"
        response = requests.get(url)
        source = response.text
        soup = BeautifulSoup(source, "lxml")
        div_list = soup.find("div", {"id": "conts"})
        dl_list = soup.find("div", {"class": "section_atistinfo04"}).findAll("dd")

        img_profile = div_list.find("span", {"id": "artistImgArea"}).img['src']
        name = div_list.find("div", {"class": "wrap_atist_info"}).p.text[5:]
        """ name 본명 잘라야됌"""
        real_name = dl_list[0].text
        nationality = dl_list[1].text
        birth_date = dl_list[2].text
        constellation = dl_list[4].text
        blood_type = dl_list[5].text
        intro = soup.find("div", {"id": "d_artist_intro"}).text.strip()

        result = {
            "img_profile": img_profile,
            "name": name,
            "real_name": real_name,
            "nationality": nationality,
            "birth_date": birth_date,
            "constellation": constellation,
            "blood_type": blood_type,
            "intro": intro,
        }
        print(result)


if __name__ == "__main__":
    artist_id = 905701
    ac = artist_crawler
    ac.melon_artist_crawler(artist_id)
