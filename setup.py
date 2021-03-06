#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

# silence pyflakes, __VERSION__ is properly assigned below...
__VERSION__ = '3.0'
PROGRAM_VERSION = __VERSION__


def datafilelist(installbase, sourcebase):
    datafileList = []
    for root, subFolders, files in os.walk(sourcebase):
        fileList = []
        for f in files:
            fileList.append(os.path.join(root, f))
        datafileList.append((root.replace(sourcebase, installbase), fileList))
    return datafileList
data_files = [
    ('{prefix}/share/applications'.format(prefix=sys.prefix), ['src/fbi.desktop']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/install.png']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/logo.png']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/create_cfg.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/end.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/error.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/fbiWindow.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/freebsd-style.css']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/install.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/installType.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/keyboard.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/language.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/partition.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/partition_handler.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/root.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/slides.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/timezone.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/use_ufs.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/use_zfs.py']),
    ('{prefix}/lib/fbi'.format(prefix=sys.prefix), ['src/addUser.py']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/detect-laptop.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/detect-nics.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/detect-sheme.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/detect-vmware.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/detect-wifi.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/disk-info.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/disk-label.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/disk-list.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/disk-part.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/enable-net.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/list-components.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/list-rsync-backups.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/list-tzones.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/query-langs.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/send-logs.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/setup-ssh-keys.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/sys-mem.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/test-live.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/test-netup.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/update-part-list.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/xkeyboard-layouts.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/xkeyboard-models.sh']),
    ('{prefix}/lib/fbi/backend-query'.format(prefix=sys.prefix), ['src/backend-query/xkeyboard-variants.sh']),
    ('{prefix}/lib/fbi/keyboard'.format(prefix=sys.prefix), ['src/keyboard/layout']),
    ('{prefix}/lib/fbi/keyboard'.format(prefix=sys.prefix), ['src/keyboard/model']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/af']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/am']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ara']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/at']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/az']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ba']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/bd']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/be']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/bg']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/br']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/brai']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/by']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ca']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ch']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/cn']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/cz']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/de']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/dk']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ee']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/epo']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/es']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/fi']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/fo']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/fr']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/gb']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ge']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/gh']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/gr']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/hr']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/hu']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ie']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/il']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/in']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/iq']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ir']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/is']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/it']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/jp']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ke']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/kg']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/kz']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/latam']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/lk']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/lt']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/lv']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ma']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/me']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/mk']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ml']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/mt']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ng']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/nl']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/no']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ph']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/pk']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/pl']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/pt']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ro']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/rs']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ru']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/se']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/si']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/sk']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/sy']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/th']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/tj']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/tm']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/tr']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/ua']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/us']),
    ('{prefix}/lib/fbi/keyboard/variant'.format(prefix=sys.prefix), ['src/keyboard/variant/uz']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/browser.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/email.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/help.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/F-logo.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/music.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/office.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/photo.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/social.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/software.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/customize.png']),
    ('{prefix}/lib/fbi/slide-images/freebsd'.format(prefix=sys.prefix), ['src/slide-images/freebsd/welcome.png']),
    ('{prefix}/lib/fbi/timezone'.format(prefix=sys.prefix), ['src/timezone/continent']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Africa']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/America']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Antarctica']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Arctic']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Asia']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Atlantic']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Australia']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Europe']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Indian']),
    ('{prefix}/lib/fbi/timezone/city'.format(prefix=sys.prefix), ['src/timezone/city/Pacific']),
]
data_files.extend(datafilelist('{prefix}/share/locale'.format(prefix=sys.prefix), 'build/mo'))


setup(name="fbi",
      version=PROGRAM_VERSION,
      description="FBI is the FreeBSD front end user interface for pc-sysinstall",
      license='BSD',
      author='Eric Turgeon',
      url='https://github/wallisonalves/fbi/',
      package_dir={'': '.'},
      data_files=data_files,
      # install_requires = [ 'setuptools', ],
      scripts=['fbi'],)

