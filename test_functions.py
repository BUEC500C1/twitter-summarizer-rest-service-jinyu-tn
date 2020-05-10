#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:15:48 2020

@author: taimaame
"""
import os
from getwordtwitter2 import get_all_tweets
from wordtoimage2 import draw_test
from imagestovideo import imagetovideo

def test_files():
    assert os.path.exists('ComingSoon.ttf')
    assert os.path.exists('getwordtwitter2.py')
    assert os.path.exists('imagestovideo.py')
    assert os.path.exists('queue.py')
    assert os.path.exists('wordtoimage2.py')
  

def test_get_all_tweets():
    username1 = 'user1'
    keyword1 = 'keyword1'
    assert get_all_tweets(username1,keyword1) != []
    assert os.path.exists('../'+username1+'/'+username1+'_images')

def test_draw_test():
    username2 = 'user2'
    keyword2 = 'keyword2'
    assert draw_test(username2,keyword2)=='../'+username2+'/'+username2+'_images/'
    assert os.path.exists('../'+username2+'/'+username2+'_images/1.jpg')
    
def test_imagetovideo():
    username3 = 'user3'
    keyword3 = 'keyword3'
    imagetovideo(username3,keyword3)
    assert os.path.exists('../'+username3+'/'+username3+'.avi')
    
def test_queue():
    os.system("python queue.py")
    assert os.path.exists('./test.txt')