#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# vim:sw=4:ts=4:et

import argparse

from amcrest import AmcrestCamera


def main():
    parser = argparse.ArgumentParser(
        description='Command line interface for Amcrest cameras.'
    )
    parser.add_argument('-H', '--hostname',
                        dest='hostname',
                        required=True,
                        help='hostname or ip address for Amcrest camera')
    parser.add_argument('-u',
                        '--username',
                        dest='username',
                        required=True,
                        help='username for Amcrest camera')
    parser.add_argument('-p',
                        '--password',
                        dest='password',
                        required=True,
                        help='password for Amcrest camera')
    parser.add_argument('-P',
                        '--port',
                        dest='port',
                        default=80,
                        help='port to Amcrest camera. Default: 80')
    parser.add_argument('--get-current-time',
                        action='store_true',
                        help='Get camera current time')
    parser.add_argument('--motion-detection-status',
                        action='store_true',
                        help='Return motion detection status.')
    parser.add_argument('--enable-motion-detection',
                        action='store_true',
                        help='Enable motion detection.')
    parser.add_argument('--disable-motion-detection',
                        action='store_true',
                        help='Disable motion detection.')
    args = parser.parse_args()

    camera = AmcrestCamera(
        args.hostname,
        args.port,
        args.username,
        args.password
    )
    if args.get_current_time:
        print(camera.get_current_time())

    elif args.motion_detection_status:
        print(camera.is_motion_detection_enabled())

    elif args.enable_motion_detection:
        if camera.is_motion_detection_enabled():
            print("Nothing to do, motion detected, already enabled!")
            return

        camera.enable_motion_detection()

    elif args.disable_motion_detection:
        print(camera.disable_motion_detection())

    else:
        print('Error: You must specify a valid operation. See usage:')
        parser.print_usage()

if __name__ == '__main__':
    main()