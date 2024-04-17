# Bandit Game

## Level 0

We simply connected to the ssh server with the given address, user and port.

## Level 0 -> 1

We used the `ls` command to list the home directory files, then `cat readme` to read the contents of the readme file.

## Level 1 -> 2

We again used the `ls` command to find the files in the home directory, then `cat ./-` to read the contents of the - file.

> Note: we coulnd't just use `cat -` because the `-` char is used to pass flags to linux commands.

## Level 2 -> 3

Once again, the `ls` command. Then `cat ./spaces\ in\ this\ filename`.

> Note: the whitespace character must be escaped with \.

## Level 3 -> 4

We changed directory with `cd inhere` command, then we listed ALL of the directory contents (included the hidden files) with `ls -la`. When then got the password from the `.hidden` file with `cat .hidden`.

## Level 4 -> 5

We changed dir to `inhere` with `cd inhere`, then we listed all the directory contents with `ls`.

To print all the contents of the files, we used `cat ./-file0*`.

> Note: `cat *` couldn't be used because all of the files begin with -.

## Level 5 -> 6

We use a pretty convoluted command to find the password in this stage, to avoid having to "cd ls cd .. cat" everything...

We first use the `man du` to check if there are any options to see both all of the files in the directory tree and to list its size in bytes (`du -ba`).

We then pipe the output into an `awk` command to check if the first element printed (the bites in size) is equal to 1033. Then we printed the file contents with the `cat` command.

`du -ab | awk '{if ($1 == 1033) print}'

## Level 6 -> 7

We  `cd ../..` to go in the server base dir, then `find -group bandit6 -user bandit7` to list all the files owned by user bandit7 and group bandit6, finding only one file.

## Level 7 -> 8

We use the `cat data.txt` to list the contents of the file, then we pipe the output to an awk function that prints the line only if the first element is "millionth".

`cat data.txt | awk '{ if ($1 == "millionth") print}'`

## Level 8 -> 9

We pipe the output of the `cat` command to `sort`, then to `uniq -c` (to also print the count). The password is the only line that appears once.

`cat data.xt | sort | uniq -c`

## Level 9 -> 10

We use the `strings data.txt` to list all the lines that contain human readable chars, then we pipe the output to `grep "===*"` to only print lines that have at least 2 equal signs.

`strings data.txt | grep "===*"`

 (the pass for the next level is G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s but i dont know if we have to do it)


