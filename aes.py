#!/usr/bin/python

from Crypto.Cipher import AES
import base64
import os

def get_keys():
  try:
    f = open('aeskey.pem','r')
    key = f.readline()
    f.close()
    return key
  except:
    return False

def enc_msg(key,message):
  encrypted_string = ''
  ciphertext = ''
  key_length = len(key)
  msg_length = len(message)
  if key_length < 16:
    print 'Key is too short, must be at least 16 chars'
    return False
  elif key_length < 24 and key_length > 15:
    key = key[:16] 
  elif key_length < 32 and key_length > 23:
    key = key[:24]
  elif key_length > 32:
    key = key[:32]
  try:
    iv = 'This is an IV456'
    obj = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(message)
    encrypted_string = base64.encodestring(ciphertext)
    return encrypted_string
  except:
    return False
  return False

# decrypt message
def dec_msg(key,message):
  decrypted_string = ''
  raw_string = ''
  key_length = len(key)
  msg_length = len(message)
  if key_length < 16:
    print 'Key is too short, must be at least 16 chars'
    return False
  elif key_length < 24 and key_length > 15:
    key = key[:16]
  elif key_length < 32 and key_length > 23:
    key = key[:24]
  elif key_length > 32:
    key = key[:32]
  try:
    iv = 'This is an IV456'
    obj = AES.new(key, AES.MODE_CFB, iv)
    raw_string = base64.b64decode(message)
    decrypted_string = obj.decrypt(raw_string)
    return decrypted_string
  except:
    return False
  return False


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
