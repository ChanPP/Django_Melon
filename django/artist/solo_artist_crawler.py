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
        dt_list = soup.find("div", {"class": "section_atistinfo04"}).findAll("dt")
        img_profile = div_list.find("span", {"id": "artistImgArea"}).img['src']
        name = div_list.find("div", {"class": "wrap_atist_info"}).p.text[5:].split()

        if len(name) == 1:
            name = name[0]
        elif len(name) == 2:
            name = name[0]
        elif len(name) == 3:
            name = name[0] + name[1]
        else:
            name = name[0] + name[1] + name[2]
        real_name = dl_list[0].text
        if dt_list[0].text == "본명":
            real_name = real_name
        else:
            real_name = ""

        nationality = dl_list[1].text
        birth_date = dl_list[2].text
        constellation = dl_list[4].text
        blood_type = dl_list[5].text
        intro = soup.find("div", {"id": "d_artist_intro"}).text.strip()
        result = {
            "name": name,
            "img_profile": img_profile,
            "real_name": real_name,
            "nationality": nationality,
            "birth_date": birth_date,
            "constellation": constellation,
            "blood_type": blood_type,
            "intro": intro,
        }
        print(result)


if __name__ == "__main__":
    artist_id = 1191
    # artist_id = 160816
    ac = artist_crawler
    ac.melon_artist_crawler(artist_id)
