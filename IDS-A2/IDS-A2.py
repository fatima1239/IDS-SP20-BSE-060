

# 29-09-2023
# CSC461 – Assignment2 – Regular Expressions
# Fatima Kazmi
# SP20-BSE-060
# In this Assignment we use regular expressions to perform different tasks on the text provided.

import re


text = """
The outlook wasn't brilliant for the Mudville nine that day; 
The score stood four to two, with but one inning more to play,
And then when Cooney died at first, and Barrows did the same,
A pall-like silence fell upon the patrons of the game. 

A straggling few got up to go in deep despair. The rest
Clung to that hope which springs eternal in the human breast;
They thought, "If only Casey could but get a whack at that--
We'd put up even money now, with Casey at the bat." 

But Flynn preceded Casey, as did also Jimmy Blake,
And the former was a lulu, while the latter was a cake;
So upon that stricken multitude grim melancholy sat,
For there seemed but little chance of Casey getting to the bat.

But Flynn let drive a single, to the wonderment of all,
And Blake, the much despised, tore the cover off the ball;
And when the dust had lifted, and men saw what had occurred,
There was Jimmy safe at second and Flynn a-hugging third. 

Then from five thousand throats and more there rose a lusty yell;
It rumbled through the valley, it rattled in the dell;
It pounded on the mountain and recoiled upon the flat,
For Casey, mighty Casey, was advancing to the bat. 

There was ease in Casey's manner as he stepped into his place;
There was pride in Casey's bearing and a smile lit Casey's face.
And when, responding to the cheers, he lightly doffed his hat,
No stranger in the crowd could doubt 'twas Casey at the bat. 

Ten thousand eyes were on him as he rubbed his hands with dirt;
Five thousand tongues applauded when he wiped them on his shirt;
Then while the writhing pitcher ground the ball into his hip,
Defiance flashed in Casey's eye, a sneer curled Casey's lip. 

And now the leather-covered sphere came hurtling through the air,
And Casey stood a-watching it in haughty grandeur there.
Close by the sturdy batsman the ball unheeded sped--
"That ain't my style," said Casey. "Strike one!" the umpire said. 

From the benches, black with people, there went up a muffled roar,
Like the beating of the storm-waves on a stern and distant shore;
"Kill him! Kill the umpire!" shouted some one on the stand;
And it's likely they'd have killed him had not Casey raised his hand. 

With a smile of Christian charity great Casey's visage shone;
He stilled the rising tumult; he bade the game go on;
He signaled to the pitcher, and once more the dun sphere flew;
But Casey still ignored it, and the umpire said, "Strike two!" 

"Fraud!" cried the maddened thousands, and echo answered "Fraud!"
But one scornful look from Casey and the audience was awed.
They saw his face grow stern and cold, they saw his muscles strain,
And they knew that Casey wouldn't let that ball go by again. 

The sneer has fled from Casey's lip, his teeth are clenched in hate;
He pounds with cruel violence his bat upon the plate.
And now the pitcher holds the ball, and now he lets it go.
And now the air is shattered by the force of Casey's blow. 

Oh, somewhere in this favored land the sun is shining bright;
The band is playing somewhere, and somewhere hearts are light,
And somewhere men are laughing, and little children shout;
But there is no joy in Mudville--great Casey has struck out
"""

# 1. Extract list of all words
words = re.findall(r'\b\w+\b', text)

# 2. Extract list of all words starting with a capital letter
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)

# 3. Extract list of all words of length 5
five_letter_words = re.findall(r'\b\w{5}\b', text)

# 4. Extract list of all words inside double quotes
quoted_words = re.findall(r'"([^"]*)"', text)

# 5. Extract list of all vowels
vowels = re.findall(r'[aeiouAEIOU]', text)

# 6. Extract list of 3 letter words ending with letter 'e'
three_letter_e_words = re.findall(r'\b\w{3}e\b', text)

# 7. Extract list of all words starting and ending with letter 'b'
b_words = re.findall(r'\bb\w*b\b', text)

# 8. Remove all the punctuation marks from the text
text_without_punctuation = re.sub(r'[^\w\s]', '', text)

# 9. Replace all words ending 'n't' to their full form 'not'
text_replaced_nt = re.sub(r'\b(\w+)n\'t\b', r'\1 not', text)

# 10. Replace all new lines with a single space
text_single_space = re.sub(r'\n', ' ', text)

# Print the results
print("List of all words:", words)
print("List of words starting with a capital letter:", capital_words)
print("List of words of length 5:", five_letter_words)
print("List of words inside double quotes:", quoted_words)
print("List of vowels:", vowels)
print("List of 3-letter words ending with 'e':", three_letter_e_words)
print("List of words starting and ending with 'b':", b_words)
print("Text without punctuation:", text_without_punctuation)
print("Text with 'n't' replaced with 'not':", text_replaced_nt)
print("Text with new lines replaced by a single space:", text_single_space)
