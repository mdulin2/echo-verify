
# Amazon Echo skill alikeness verification
Ever tried asking for Alexa to play music but then she asks for your debit card information? Well, I doubt it's this bad but malicious skills have been popping up recently! So, what is the patch for voice recognized malicious calls on the Alexa?

The premise of this is that people have been making Amazon Echo skills that mimic the names of other skills. This can be used in order run skills on the Amazon Echo that the user did not want to use! So, I have created a *proof of concept fix* for this. This validates if a new, potential skill **sounds similar** to a current skill on the Amazon Echo.

# How it works:

## Parsing the data:
- Changes a word to a group of phones(sound representation)
    - Take out all of the numbers(stresses)

## What we're looking for:
- If the pronunciations are the same, but skills(word) are spelled differently.
- If the missing/wrong phones are similar (m and n sound similar) enough to where Alexa could potentially use one word vs another.


# How to run:
1. Clone into the repo! `git clone https://github.com/mdulin2/echo-verify`

2. Assuming that Python 2.7 is installed...  
Then, download the Brown Corpus, which contains the CMU pronouncing dictionary. Download this cmudict of word into the Brown Corpus. A good guide on how to do this is [here](https://www.nltk.org/data.html).

3. Choose your current set of skills to verify against. Then, choose the phrase to check for how similar they sound.   
```
python echo_check.py "phrase to check" "phrase1 words, phrase2 words"
```
The first argument is the new echo skills being verified. The second argument is the current valid Alexa skills. My best test example is `python echo_check.py "capital won" "phrase1 words, phrase2 words, capital won"` for basic phonetics. For a similar sounding phone test try: `python echo_check.py "pat man" "bat man, phrase words, capital won"`  

Hopefully people like this! Feel free to contribute to this repo if you want also. 


## Current Issues:

There are some major issues with this. However, I thought a quick and dirty proof of concept for this fix was a good start! Anytime phonetics are involved, it's hard to get it completely correct.
- The converter from word to phones is static; non-deterministic. Not sure if there is a deterministic word to phone converter.
- The chart being used for similarity is not perfect. I'm not a master of linguistics!
- Only one pronunciation is being verified. Could be verifying all pronunciations of the word.
- Doesn't have the actual Alexa skills loaded into it.

** Made by ILY, aka Maxwell Dulin in 2018
