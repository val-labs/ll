I=$(wildcard tstdata/*.i)
O=$(I:.i=.o)
all: $(O)
clean: ; rm -fr tstdata/*.o
tstdata/%.o: tstdata/%.i
	python x.py $?
	diff $@ $@.x
