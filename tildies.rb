#!/usr/bin/env ruby

f = open("tilde_words")
words = f.readlines
f.close()

words.map! { |x| x.chop }  # Remove newlines
words.shuffle!  # Randomise word order

vowels = %w{a e i o u A E I O U}
tilde_vowels = %w{á é í ó ú Á É Í Ó Ú}
to_tilde = Hash[vowels.collect{|v| [v, tilde_vowels[vowels.index(v)]]}]
from_tilde = Hash[tilde_vowels.collect{|v| [v, vowels[tilde_vowels.index(v)]]}]

puts "Welcome to Nay's spanish tilde test!"
puts "####################################"
print "How many words would you like to attempt? "
count = gets.chomp.to_i
puts "Great! Let's go:"
puts

correct_answers = 0

1.upto(count) do |i|
  word = words[i]
  index = nil
  helper_string = String.new
  vowel_index = 0  # The index in vowels
  found = false
  word.chars.each_with_index do |c,idx|
    if vowels.push(tilde_vowels).flatten.include? c
      helper_string += "↓"
      vowel_index += 1 unless found
    else
      helper_string += " "
    end
    if tilde_vowels.include? c
      found = true
      vowel_index = vowel_index
      index = idx
    end
  end
  neutered_word = word.chars.map { |c| from_tilde[c] || c }.join

  puts "------------------------ (#{i})"
  puts helper_string
  puts "#{neutered_word}"
  print "Which # of verb contains the stress? "
  answer = gets.chomp.to_i
  if answer == vowel_index
    puts "Correct! The word was #{word}"
    correct_answers += 1
  else
    puts "Sorry, the stress was on vowel #{vowel_index} and the word was #{word}"
  end
  puts
end

puts
puts "You scored #{correct_answers} out of #{count}, or #{((correct_answers.to_f/count)*100).round}%"
