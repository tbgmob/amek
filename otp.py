#!/usr/bin/python

import onetimepad
import base64
import os

def get_keys():
  try:
    f = open('otpkey.pem','r')
    key = f.readline()
    f.close()
    return key
  except:
    return False

# encrypt message
def enc_msg(key_store,message_buffer):
  cipher =""
  try:
    cipher = onetimepad.encrypt(message_buffer,key_store)
  except:
    cipher =""
  return cipher

# encrypt message
def dec_msg(key_store,message_buffer):
  txt_msg = ""
  try:
    txt_msg = onetimepad.decrypt(message_buffer,key_store)
  except:
    txt_msg = ""
  return txt_msg

# get key(s)
key = get_keys()
if not key:
  print 'failed to fetch keys'

# enter secret message
my_msg = raw_input('Enter message: ')

# encrypt or decrypt?
msg_str = ''
answer = raw_input('(E)ncrypt or (D)ecrypt?: ')
if answer == 'e' or answer == 'E':
  msg_str = enc_msg(key,my_msg)
elif answer == 'd' or answer == 'D':
  msg_str = dec_msg(key,my_msg)

print msg_str
