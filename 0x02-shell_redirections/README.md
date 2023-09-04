README.md

Shell I/O Redirections, Filters

0-hello_world

#!/bin/bash
echo "Hello, World"

1-confused_smiley

#!/bin/bash
echo "\"(Ôo)'"

2-hellofile

#!/bin/bash
cat /etc/passwd

3-twofiles

#!/bin/bash
cat /etc/passwd /etc/hosts

4-lastlines

#!/bin/bash
tail -n 10 /etc/passwd

5-firstlines

#!/bin/bash
head -n 10 /etc/passwd

6-third_line

#!/bin/bash
head -n 3 iacta | tail -n 1

7-file

#!/bin/bash
echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)

8-cwd_state

#!/bin/bash
ls -la > ls_cwd_content

9-duplicate_last_line

#!/bin/bash
tail -n 1 iacta >> iacta

10-no_more_js

#!/bin/bash
find . -type f -name "*.js" -delete

11-directories

#!/bin/bash
find . -type d -not -name '.' | wc -l

12-newest_files

#!/bin/bash
ls -t1 | head -n 10

13-unique

#!/bin/bash
sort | uniq -u

14-findthatword

#!/bin/bash
grep -i "root" /etc/passwd

15-countthatword

#!/bin/bash
grep -c -i "bin" /etc/passwd

16-whatsnext

#!/bin/bash
grep -i "root" -A 3 /etc/passwd

17-hidethisword

#!/bin/bash
grep -i -v "bin" /etc/passwd

18-letteronly

#!/bin/bash
grep -i "^[a-z]" /etc/ssh/sshd_config

19-AZ

#!/bin/bash
tr "A" "Z" | tr "c" "e"


21-reverse

#!/bin/bash
rev

22-users_and_homes

#!/bin/bash
cut -d ':' -f 1,6 /etc/passwd | sort

100-empty_casks

#!/bin/bash
find . -empty | rev | cut -d '/' -f 1 | rev

101-gifs

#!/bin/bash
find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f

102-acrostic

#!/bin/bash
cut -c 1 | paste -s -d ''
103-the_biggest_fan

#!/bin/bash
tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev




















