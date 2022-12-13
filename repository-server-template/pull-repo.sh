#!/usr/bin/env bash
service nginx start && service cron start
cd /var/www/html && git clone https://github.com/VMFJ-org/repository.git
echo '*/5 * * * * www-data cd /var/www/html && git clone https://github.com/VMFJ-org/repository.git' >> /etc/crontab
tail -f /dev/null