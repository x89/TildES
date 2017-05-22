#!/usr/bin/env ruby

class String
  def remove_tildes
    '''Removes every instance of a tilde with a non-tilde equiv'''

  end
end

f = open("tilde_words")
words = f.readlines
f.close()

words.map! { |x| x.chop }  # Remove newlines
words.shuffle!  # Randomise word order

vowels = "aeiouAEIOU".split('')
tilde_vowels = "áéíóúÁÉÍÓÚ".split('')
h = Hash[vowels.collect{ |v| [v, tilde_vowels[vowels.index(v)]] }]

count = 5

1.upto(count) do |i|
  word = words[i]
  word.chars.each_with_index do |c,idx|
    if tilde_vowels.include? c
      index = idx
      puts "#{word} #{c} #{idx+1}"
    end
  end
end
