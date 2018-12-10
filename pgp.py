#!/usr/bin/python

from Crypto.PublicKey import RSA
import binascii
import base64
import os

def gen_keys():
  try:
    key = RSA.generate(2048)
    binPrivKey = key.exportKey('DER')
    binPubKey =  key.publickey().exportKey('DER')
    f = open('prikey.pem','w')
    f.write(binascii.b2a_base64(binPrivKey))
    f.close()
    f = open('pubkey.pem','w')
    f.write(binascii.b2a_base64(binPubKey))
    f.close()
    return True
  except:
    return False

def get_keys():
  try:
    f = open('prikey.pem','r')
    b64prikey = f.readline()
    f.close()
    binPrivKey = binascii.a2b_base64(b64prikey)
    f = open('pubkey.pem','r')
    b64pubkey = f.readline()
    f.close()
    binPubKey = binascii.a2b_base64(b64pubkey)
    privKeyObj = RSA.importKey(binPrivKey)
    pubKeyObj =  RSA.importKey(binPubKey)
    return(privKeyObj,pubKeyObj)
  except:
    return False

def enc_msg(key,msg):
  emsg = key.encrypt(msg, 'x')[0]
  msg_str = binascii.b2a_base64(emsg)
  return msg_str

# encrypt message
def dec_msg(key,msg):
  dmsg = key.decrypt(binascii.a2b_base64(msg))
  return dmsg


# get key(s)
(key,pubkey) = get_keys()
if not key:
  print 'failed to fetch keys'

# enter secret message
my_msg = raw_input('Enter message: ')

# encrypt or decrypt?
msg_str = ''
answer = raw_input('(E)ncrypt or (D)ecrypt?: ')
if answer == 'e' or answer == 'E':
  msg_str = enc_msg(pubkey,my_msg)
elif answer == 'd' or answer == 'D':
  msg_str = dec_msg(key,my_msg)

print msg_str
