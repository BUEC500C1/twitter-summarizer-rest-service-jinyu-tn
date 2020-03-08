#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:37:32 2020

@author: taimaame
"""

from PIL import Image  
from PIL import ImageDraw  
import getwordtwitter2
from PIL import ImageFont  

def draw_test(username,keyword):  
    

    
    
    list_word = getwordtwitter2.get_all_tweets(username,keyword)
    
    address = '../'+username+'/'+username+'_images/'
    
    #build a white background 
    #image.show()  
    for i in range(0,len(list_word)):
        font = ImageFont.truetype('./ComingSoon.ttf', 15)
        word = list_word[i].encode('ascii', 'ignore').decode('ascii')
        #word = list_word[i]
        image = Image.new('RGB', (800, 500), color = (255, 192, 203))  
        draw = ImageDraw.Draw(image)  
        draw.text((5, 200), word, fill = (0,0,0), font=font)  
        j = str(i+1)
        image.save('../'+username+'/'+username+'_images/'+j+'.jpg',dpi=(300.0,300.0))

    
    return  address
