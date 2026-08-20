#
# Top level meson.build
#

project(
  'cidrtools-cffi',
  'c',
  version: files('src/version.txt'),
  meson_version: '>=1.2.0',
  default_options: [
    'c_std=c23',
    'warning_level=2', 
    'b_pie=true',
    'prefix=/usr',
    'mandir=share/man',
    ]
)

d_etc = get_option('sysconfdir')
d_lib = get_option('libdir')
d_bin = get_option('bindir')
d_man = get_option('mandir')
d_share = get_option('datadir')


#
# Python
# - Install dir will be .../site-packages/cidrtools
#
py = import('python').find_installation(pure: false)

subdir('src/cidrtools')

#
# Install
#
s_docs = 'src/data/docs'
s_man = 'src/data/man'
s_license = 'src/data/license'
manual = 'cidrtools-cffi.pdf'

install_data(
  [
    s_docs / manual,
  ],
  install_dir: d_share / 'cidrtools-cffi'
)

install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'cidrtools-cffi/License',
)

install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'licenses/cidrtools-cffi'
)

