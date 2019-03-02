import numpy as np 
from random import shuffle

v_s = 100
h_s = 100
#----------------------------#
# Hashcode 2019
# ItsTooLateElon #1104
#----------------------------#

class Photo(object):
  def __init__(self, ori,tags,idx):
    self.id = idx
    self.ori = ori
    self.tags = tags

  def concatTags(self,photo):
    self.tags = list(set(self.tags + photo.tags))
    self.id = str(self.id) + ' ' + str(photo.id)

def readNextLines(file):
  photos = []
  line = file.readline()
  idx = 0
  while line:
    l = line.replace('\n','')
    photoDesc = l.split(" ")
    ori = photoDesc[0]
    numTags = int(photoDesc[1])
    tags = photoDesc[2:numTags+2]
    
    p = Photo(ori,tags,idx)
    photos.append(p)

    line = file.readline()
    idx += 1

  return photos

def arrangeVertical(vertical):
  ver_2 = []

  mx_arr_idx = 0
  score_ =0 
  while len(vertical) > 0:
    
    if(len(vertical) %10 ==0):
      print(str(len(vertical)) + ' V_Left')
    idx = mx_arr_idx
    pht = vertical[idx] 
    del vertical[idx]
    ver_2.append(pht)

    mx_score = 0
    mx_arr_idx = 0
    
    for i in range(0,len(vertical)):
      score = min(len(pht.tags) - len(list(set(pht.tags).intersection(vertical[i].tags))),len(vertical[i].tags) - len(list(set(pht.tags).intersection(vertical[i].tags))));
      if score > mx_score:  
        mx_score = score
        mx_arr_idx = i
      if i > min(len(vertical),v_s):
        break

    score_ += mx_score
  return ver_2

def getScore(photo1,photo2):
  common = len(list(set(photo1.tags).intersection(photo2.tags)))
  u1 = len(photo1.tags) - common;
  u2 = len(photo2.tags) - common;
  return min(common,u1,u2)

if __name__ == '__main__':
  #file_name = "a_example"
  #file_name = "b_lovely_landscapes"
  #file_name = "c_memorable_moments"
  #file_name = "d_pet_pictures"
  file_name = "e_shiny_selfies"
  
  file = open(file_name+'.txt', "r")

  n = int(file.readline())

  photos = readNextLines(file)

  vertical = []
  horizontal = []
  for i in range(0,n):
    if photos[i].ori == 'H':
      horizontal.append(photos[i])
    else:
      vertical.append(photos[i])

  vertical = arrangeVertical(vertical)
  vertical2 = []

  for i in range(1,len(vertical),2):
    vertical[i-1].concatTags(vertical[i])
    vertical2.append(vertical[i-1])
  
  horizontal = horizontal + vertical2


  result = []

  mx_arr_idx = 0
  score_ =0 
  while len(horizontal) > 0:
    
    if(len(horizontal) %10 ==0):
      print(str(len(horizontal)) + ' Left, Points : ' + str(score_))
    idx = mx_arr_idx
    pht = horizontal[idx] 
    del horizontal[idx]
    result.append(pht)

    mx_score = 0
    mx_arr_idx = 0
    
    for i in range(0,len(horizontal)):
      score = getScore(pht,horizontal[i])
      if score > mx_score:  
        mx_score = score
        mx_arr_idx = i
      if i > min(len(horizontal),h_s):
        break

    score_ += mx_score

  print('Done')

  score = 0
  for i in range(1,len(result)):
    score += getScore(result[i-1],result[i])
  print(result[2].id)

  print(score)

  f= open(file_name+"out.txt","w+")

  f.write("%s\n" % str(len(result)))
  
  for i in range(0,len(result)):
    f.write("%s\n" % result[i].id)