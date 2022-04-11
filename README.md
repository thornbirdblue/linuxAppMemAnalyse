# linuxAppMemAnalyse

1.strace mmap file format:

strace: Process 928 attached with 59 threads
[pid   971] 10:32:01.568993 mmap(NULL, 1040384, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x7080a02000

2.Catch cmd:

set pid=928
set reg="brk,mmap,munmap"
set filename="%date:~5,2%-%date:~8,2%_%time:~0,2%_%time:~3,2%_%time:~6,2%"

adb shell strace -tt -f -p %pid% -e %reg% 2>%filename%_info.txt
