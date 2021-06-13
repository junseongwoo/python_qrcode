from googlesearch import search 

query = input("무엇을 검색하고 싶으신가요? : ")

print(search(query)) # generator 형태로 나옴 : 계속 반복되는 형태 

for i in search(query, start=0, stop=10): 
    print(i)