# software_design
[![Build Status](https://travis-ci.org/slampy97/software_design.svg?branch=task1-dev)](https://travis-ci.org/slampy97/software_design)

Project sructure:
.
├── Makefile
├── proj
│   ├── app.py
│   ├── Commands
│   │   ├── cat.py
│   │   ├── Commands_fabric.py
│   │   ├── echo.py
│   │   ├── exit.py
│   │   ├── pwd.py
│   │   └── wc.py
│   ├── executor.py
│   ├── lexer.py
│   ├── main.py
│   ├── parser.py
│   ├── token_dir
│   │   ├── token_double_quote.py
│   │   ├── token_fabric.py
│   │   ├── token_pipe.py
│   │   ├── token_single_quote.py
│   │   ├── token_word.py
│   │   └── toke_space.py
│   ├── token_split.py
│   └── utility_class
│       └── kind.py
├── README.md
└── tests
    ├── file1.txt
    ├── file2.txt
    └── test.py

to tun test manually: python -m unittest tests/test.py

supported command:

cat[file]: concat data from all files or stdin

echo [args]: print agrs split by ' '

wc[files]: count number f lines, words and bytes

exit: terminate process

pwd: return path to project

and all bash commands can be called

