# with open("file_1.txt", "r", encoding="utf-8") as f:
#     data = f.read().replace(" ","")
#
# print(len(data))

# my_str = "привіт. пока. права. ліво"
# mass_str = my_str.split(".")
# with open("file_1.txt", "w", encoding="utf-8") as f:
#     for i in mass_str:
#         f.write(i.strip() + "\n")
#
# words = ["каком-либо" , "мысль","носителе"]
#
#
# def read_file():
#     with open("file_1.txt", "r", encoding="utf-8") as file:
#         file_string = file.read()
#     return file_string
#
# def select_words():
#     res_lst = []
#     for w in read_file().split():
#         if w == words:
#             continue
#         else:
#             res_lst.append(w)
#     return res_lst
# def add_string():
#     return " ".join(select_words())
# def creat_file():
#     with open("new _file.txt", "w", encoding="utf-8") as file:
#         file.write(add_string())
#
# if __name__ == "__main__":
#     creat_file()

#
# t = { 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'і': 'i', 'й': 'y',
#      'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц ': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',  'ю': 'yu', 'я': 'ya', " ":" "}
# data = "Вітаю"
# # data = "vitayu"
# data1 = ""
# for let in data:
#     if let.isupper():
#         data1 += t[let.lower()].upper()
#     else:
#         data1 += t.get(let)
# print(data1)
#
# data1 = ""
# with open("file_1.txt", "r",encoding="utf-8") as f:
#     for let in f.read():
#         if let.isupper():
#             data1 += t[let.lower()].upper()
#         else:
#             data1 += t.get(let)
#
# with open("new _file.txt", "w",encoding="utf-8") as file:
#     file.write(data1)
# for i in data:
#     data1 += t.get(i)
# print(data1)

# files = []
# while True:
#     nema_file = input("name")
#     if nema_file == "q":
#         break
#     files.append(nema_file)
#
# for name in files:
#     with open(f'{name}.txt',"r", encoding="utf-8") as f:
#         print(f.read())



import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.fahrrad.de/collections/kinderraeder-24-zoll"
user = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
resource = requests.get(url,headers=user)
print(resource)
soup = BeautifulSoup(resource.text,"lxml")
all_product = soup.find('ul', class_ ="grid mb-8 md:mb-12 grid-cols-2 small-cards-mobile sm:grid-cols-3 gap-x-theme gap-y-16")
print(all_product)
product = all_product.find_all('li',claas_='js-pagination-result')
for pr in product:
    title = pr.find('p',claas_='card__title font-bold mt-1 mb-0')
    # print(title)
    price = pr.find('strong',class_='price__current')
    print(price)