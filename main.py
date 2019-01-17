import vk_api 
import time 
import random 
import datetime 
 
login, passw = "", "" 

def main(t): 
 lm,rm,cm = 0, 0, 0 
 lx,rx,cx = 0, 0, 0 
 k, k1 = 0, 0 
 session = vk_api.VkApi(login, passw) 
 session.auth(token_only = True) 
 vk = session.get_api() 
 data = vk.wall.get(owner_id=-44235988, count=50) 
 for i in data['items']: 
 for j in i['text'].split('#'): 
 if (j == '25shot_per_sec'): 
 lm += i['likes']['count'] 
 rm += i['reposts']['count'] 
 cm += i['comments']['count'] 
 k += 1 
 if (j == 'media_мидии'): 
 lx += i['likes']['count'] 
 rx += i['reposts']['count'] 
 cx += i['comments']['count'] 
 k1 += 1 
 txt = "Подсчёт #"+str(t)+"<br>" 
 txt += "МОРСКОЙ (МЫ)<br>" 
 txt += "Постов: "+str(k)+"<br>" 
 txt += ("Лайков = "+str(lm))+"<br>" 
 txt += ("Репостов = "+str(rm))+"<br>" 
 txt += ("Комментариев = "+str(cm))+"<br>" 
 txt += ("ХРУСТАЛЬНЫЙ")+"<br>" 
 txt += "Постов: "+str(k)+"<br>" 
 txt += ("Лайков = "+str(lx))+"<br>" 
 txt += ("Репостов = "+str(rx))+"<br>" 
 txt += ("Комментариев = "+str(cx))+"<br>" 
 txt += "Время подсчёта: "+str(datetime.datetime.now()) 
 random.seed() 
 vk.messages.send(peer_id=2000000000+190,message=txt,random_id=random.randint(1,99999)) 
 
t = 0 
while(True): 
 main(t) 
 t += 1 
 time.sleep(300)
