def input_for_day(day):
    input = [
        '516299281491169512719425276194596424291268712697155863651846937925928456958813624428156218468331423858422613471962165756423837756856519754524985759763747559711257977361228357678293572698839754444752898835313399815748562519958329927911861654784216355489319995566297499836295985943899373615223375271231128914745273184498915241488393761676799914385265459983923743146555465177886491979962465918888396664233693243983969412682561799628789569294374554575677368219724142536789649121758582991345537639888858113763738518511184439854223386868764189133964543721941169786274781775658991329331759679943342217578532643519615296424396487669451453728113114748217177826874953466435436129165295379157226345786756899935747336785161745487933721527239394118721517195849186676814232887413175587327214144876898248571248517121796766248817366614333915154796983612174281237846165129114988453188844745119798643314857871527757831265298846833327863781341559381238458322786192379487455671563757123534253463563421716138641611915686247343417126655317378639314168461345613427262786624689498485599942336813995725145169355942616672812792174556866436158375938988738721253664772584577384558696477546232189312287262439452141564522329987139692281984783513691857538335537553448919819545332125483128878925492334361562192621672993868479566688564752226111784486619789588318171745995253645886833872665447241245329935643883892447524286642296955354249478815116517315832179925494818748478164317669471654464867111924676961162162841232473474394739793968624974397916495667233337397241933765513777241916359166994384923869741468174653353541147616645393917694581811193977311981752554551499629219873391493426883886536219455848354426461562995284162323961773644581815633779762634745339565196798724847722781666948626231631632144371873154872575615636322965353254642186897127423352618879431499138418872356116624818733232445649188793318829748789349813295218673497291134164395739665667255443366383299669973689528188264386373591424149784473698487315316676637165317972648916116755224598519934598889627918883283534261513179931798591959489372165295',
        [
            [1224, 926, 1380, 688, 845, 109, 118, 88, 1275, 1306, 91, 796, 102, 1361, 27, 995],
            [1928, 2097, 138, 1824, 198, 117, 1532, 2000, 1478, 539, 1982, 125, 1856, 139, 475, 1338],
            [848, 202, 1116, 791, 1114, 236, 183, 186, 150, 1016, 1258, 84, 952, 1202, 988, 866],
            [946, 155, 210, 980, 896, 875, 925, 613, 209, 746, 147, 170, 577, 942, 475, 850],
            [1500, 322, 43, 95, 74, 210, 1817, 1631, 1762, 128, 181, 716, 171, 1740, 145, 1123],
            [3074, 827, 117, 2509, 161, 206, 2739, 253, 2884, 248, 3307, 2760, 2239, 1676, 1137, 3055],
            [183, 85, 143, 197, 243, 72, 291, 279, 99, 189, 30, 101, 211, 209, 77, 198],
            [175, 149, 259, 372, 140, 250, 168, 142, 146, 284, 273, 74, 162, 112, 78, 29],
            [169, 578, 97, 589, 473, 317, 123, 102, 445, 217, 144, 398, 510, 464, 247, 109],
            [3291, 216, 185, 1214, 167, 495, 1859, 194, 1030, 3456, 2021, 1622, 3511, 222, 3534, 1580],
            [2066, 2418, 2324, 93, 1073, 82, 102, 538, 1552, 962, 91, 836, 1628, 2154, 2144, 1378],
            [149, 963, 1242, 849, 726, 1158, 164, 1134, 658, 161, 1148, 336, 826, 1303, 811, 178],
            [3421, 1404, 2360, 2643, 3186, 3352, 1112, 171, 168, 177, 146, 1945, 319, 185, 2927, 2289],
            [543, 462, 111, 459, 107, 353, 2006, 116, 2528, 56, 2436, 1539, 1770, 125, 2697, 2432],
            [1356, 208, 5013, 4231, 193, 169, 3152, 2543, 4430, 4070, 4031, 145, 4433, 4187, 4394, 1754],
            [5278, 113, 4427, 569, 5167, 175, 192, 3903, 155, 1051, 4121, 5140, 2328, 203, 5653, 3233],
        ]
    ]
    return input[day - 1]

'''
--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic.
"The printer's broken! We can't print the Naughty or Nice List!" By the
time you make it to sub-basement 17, there are only a few minutes until
midnight. "We have a big problem," she says; "there must be almost fifty
bugs in this system, but nothing else can print The List. Stand in this
square, quick! There's no time to explain; if you can convince them to
pay you in stars, you'll be able to--" She pulls a lever and the world
goes blurry.

When your eyes can focus again, everything seems a lot more pixelated
than before. She must have sent you inside the computer! You check the
system clock: 25 milliseconds until midnight. With that much time, you
should be able to collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day millisecond in the advent calendar; the second puzzle is
unlocked when you complete the first. Each puzzle grants one star. Good
luck!

You're standing in a room with "digitization quarantine" written in LEDs
along one wall. The only door is locked, but it includes a small
interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to
prove you're not a human. Apparently, you only get one millisecond to
solve the captcha: too fast for a normal human, but it feels like hours
to you.

The captcha requires you to review a sequence of digits (your puzzle
input) and find the sum of all digits that match the next digit in the
list. The list is circular, so the digit after the last digit is the
first digit in the list.

For example:

  - 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches
    the second digit and the third digit (2) matches the fourth digit.
  - 1111 produces 4 because each digit (all 1) matches the next.
  - 1234 produces 0 because no digit matches the next.
  - 91212129 produces 9 because the only digit that matches the next one
    is the last digit, 9.
    
What is the solution to your captcha?
'''
def aoc01_1():
    input = input_for_day(1)
    result = int(input[0]) if input[0] == input[len(input) - 1] else 0
    for i in range(0, len(input) - 1):
        if input[i] == input[i+1]:
            result += int(input[i])
    print("Day 01 #1: %s" % result)

'''
You notice a progress bar that jumps to 50% completion. Apparently, the
door isn't yet satisfied, but it did emit a star as encouragement. The
instructions change:

Now, instead of considering the next digit, it wants you to consider the
digit halfway around the circular list. That is, if your list contains 10
items, only include a digit in your sum if the digit 10/2 = 5 steps
forward matches it. Fortunately, your list has an even number of
elements.

For example:

  - 1212 produces 6: the list contains 4 items, and all four digits match
    the digit 2 items ahead.
  - 1221 produces 0, because every comparison is between a 1 and a 2.
  - 123425 produces 4, because both 2s match each other, but no other
    digit has a match.
  - 123123 produces 12.
  - 12131415 produces 4.
  
What is the solution to your new captcha?
'''
def aoc01_2():
    input = input_for_day(1)
    l = len(input)
    result = 0
    for i in range(0, len(input)):
        if input[i] == input[(l - (l - i) + l / 2) % l]:
            result += int(input[i])
    print("Day 01 #2: %s" % result)

'''
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your
direction. "You there! Your state appears to be idle. Come help us repair
the corruption in this spreadsheet - if we take another millisecond,
we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make
sure the recovery process is on the right track, they need you to
calculate the spreadsheet's checksum. For each row, determine the
difference between the largest value and the smallest value; the checksum
is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

  - The first row's largest and smallest values are 9 and 1, and their
    difference is 8.
  - The second row's largest and smallest values are 7 and 3, and their
    difference is 4.
  - The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
'''
def aoc02_1():
    rows = input_for_day(2)
    result = 0
    for row in rows:
        result += max(row) - min(row)
    print("Day 02 #1: %s" % result)

'''
"Great work; looks like we're on the right track after all. Here's a star
for your effort." However, the program seems a little worried. Can
programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some
information about the evenly divisible values in the spreadsheet.
Unfortunately, none of us are equipped for that kind of calculation -
most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where
one evenly divides the other - that is, where the result of the division
operation is a whole number. They would like you to find those numbers on
each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

  - In the first row, the only two numbers that evenly divide are 8 and 2
    ; the result of this division is 4.
  - In the second row, the two numbers are 9 and 3; the result is 3.
  - In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
'''
def aoc02_2():
    rows = input_for_day(2)
    result = 0
    for row in rows:
        for dividend in row:
            for divisor in row:
                if dividend != divisor and dividend % divisor == 0:
                    result += dividend / divisor
    print("Day 02 #2: %s" % result)

def aoc(day, challenge):
    [
        [aoc01_1, aoc01_2],
        [aoc02_1, aoc02_2],
    ][day - 1][challenge - 1]()