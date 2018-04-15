PY = $(wildcard *.py)
OUT = $(patsubst %.py, %-output.txt, $(PY))

all: $(OUT)

%-output.txt: %.py
	./$< > $@
