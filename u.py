from lixlib import linked
import random
#facebook
abc='qwertyuiopasdfghjlkmnbvcxz18639207'
while True:
  e=str(''.join((random.choice(abc) for l in range(3))))
  i=str(e)+"@yopmail.com"
  link = linked.tiktok(i)
  if "UnLinked" in str(link):
    print("f")
  else:
    print(link+'      tiktok')
  ik=linked.facebook(i)
  if "UnLinked" in str(link):
    print("f")
  else:
    print(ik+'      facebook')
