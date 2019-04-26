#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Andreas Schmidl <ferraith@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# this is a windows documentation stub. actual code lives in the .ps1
# file of the same name

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: win_archive
version_added: "2.7"
short_description: Creates a compressed archive of one directory
description:
  - Compresses a directory into an archive.
  - Supports .zip files natively.
options:
  path:
    description:
      - Remote absolute path directory to compress or archive.
    required: true
    type: path
  format:
    description:
      - The type of compression to use.
    choices: [ zip ]
    default: zip
    type: str
  dest:
    description:
      - The file name of the destination archive.
    default: <path>.<format>
    type: path
  compression_level
    description:
      - One of the values that indicates whether to emphasize speed or compression effectiveness
        when creating the archive.
    default: optimal
    choices: [ optimal, fastest, no_compression ]
    type: str
notes:
  - For non-Windows targets, use the M(archive) module instead.
author:
- Andreas Schmidl (@ferraith)
'''

EXAMPLES = r'''
- name: Compress directory C:\path\to\foo into C:\path\to\foo.zip
  archive:
    path: C:\path\to\foo
    dest: C:\path\to\foo.zip

- name: Create a zip archive of C:\path\to\foo
  archive:
    path: C:\path\to\foo
    format: zip

- name: Create a zip archive of C:\path\to\foo without compression
  archive:
    path: C:\path\to\foo
    format: zip
    compression_level: no_compression
'''

RETURN = r'''
dest:
    description: The destination file/path.
    returned: always
    type: string
    sample: C:\path\to\foo.zip
src:
    description: The provided source path.
    returned: always
    type: string
    sample: C:\path\to\foo
'''
