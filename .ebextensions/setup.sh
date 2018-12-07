#!/usr/bin/env bash

db='alias db="cd /opt/python/current/app/ && source ../env && ./manage.py dbshell"'
shell='alias shell="cd /opt/python/current/app/ && source ../env && ./manage.py shell"'

grep -q "sudo -s" /home/ec2-user/.bashrc || echo -e "sudo -sn" >> /home/ec2-user/.bashrc
grep -q "alias db=" /root/.bashrc || echo -e $db >> /root/.bashrc
grep -q "alias shell=" /root/.bashrc || echo -e $shell >> /root/.bashrc