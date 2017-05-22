#!/usr/bin/env ruby

class String
  def vowel_indexes
    '''Array of indexes of vowels'''
    vowels = %w{a e i o u A E I O U á é í ó ú Á É Í Ó Ú}
    self.chars.each.map { |c| vowels.include? c }
  end
end

f = open("tilde_words")
words = f.readlines
f.close()

words.map! { |x| x.chop }  # Remove newlines
words.shuffle!  # Randomise word order

vowels = %w{a e i o u A E I O U}
tilde_vowels = %w{á é í ó ú Á É Í Ó Ú}
to_tilde = Hash[vowels.collect{|v| [v, tilde_vowels[vowels.index(v)]]}]
from_tilde = Hash[tilde_vowels.collect{|v| [v, vowels[tilde_vowels.index(v)]]}]

count = 5

1.upto(count) do |i|
  word = words[i]
  index = nil
  vowel_indexes = word.vowel_indexes
  helper_string = String.new
  word.chars.each_with_index do |c,idx|
    if vowels.push(tilde_vowels).flatten.include? c
      helper_string += "↓"
    else
      helper_string += " "
    end
    if tilde_vowels.include? c
      index = idx
    end
  end
  neutered_word = word.chars.map { |c| from_tilde[c] || c }.join
  puts
  puts helper_string
  puts "#{neutered_word} #{word}"
end
