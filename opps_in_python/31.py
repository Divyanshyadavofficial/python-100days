
import requests
import asyncio
async def function1():
    print("func 1")
    url = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(url)
    open("instagram.ico","wb").write(response.content)
    return "divyansh"
async def function2():
  print("func 2") 
  url = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(url)
  open("instagram2.jpg", "wb").write(response.content)

async def function3():
  print("func 3") 
  url = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(url)
  open("instagram3.jpg", "wb").write(response.content)
async def main():
   await function1()
   await function2()
   await function3()
asyncio.run(main())

# async def main():
#    l= await asyncio.gather(
#       function1(),
#       function2(),
#       function3(),
#    )
#    print(l)
# asyncio.run(main())