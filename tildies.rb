#!/usr/bin/env ruby

f = open("tilde_words")
words = f.readlines
f.close()
words.map! { |x| x.chop }
words.shuffle!
