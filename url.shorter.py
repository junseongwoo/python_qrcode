import pyshorteners

url = input("줄이고 싶은 URL을 입력해주세요 : ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print("줄여진 URL : ", short_url)