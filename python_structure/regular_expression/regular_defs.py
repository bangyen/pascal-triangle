import re

# https://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_04

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but scientists
 are unable to explain
 how it got its long __PART_OF_THE_BODY__.
 The giraffe's tremendous
 height, which might reach
 __NUMBER__ __PLURAL_NOUN__, comes
 from it legs and __BODYPART__.
"""

underscores_words = "_one_ _two_ _three_"


def one_word_in_a_line(word, line):
    """

    :param word: the word the regular expression will search
    :param line: the string the regular expression will search 'word' in
    :return: the list of matches
    """
    return re.findall(word, line)


def one_word_in_a_line_ignore_case(word, line):
    """
    'one_word_in_a_line' but no keys sensitive
    :param word: the word the regular expression will search
    :param line: the string the regular expression will search 'word' in
    :return: the list of matches
    """
    return re.findall(word, line, re.IGNORECASE)


def start_with(word, line):
    word = "^" + word
    return re.findall(word, line)


def start_with_multiline(word, line):
    word = "^" + word
    return re.findall(word, line, re.MULTILINE)


def end_with(word, line):
    word = word + "$"
    return re.findall(word, line)


def find_digit(line):
    """
    The '\d' search for the digit in 'line'
    :param line:
    :return:
    """
    return re.findall("\d", line, re.IGNORECASE)


def non_greedy_match(word):
    """
    The period matches any character, so this regular expression
    matches any character between the underscores. To match as much
    text as possible, it will have to use the asterisk.
    :param word:
    :return:
    """
    return re.findall("_.*_", word)


def non_greedy_match_question_mark(word):
    """
    The period matches any character, so this regular expression
    matches any character between the underscores. To match as much
    text as possible, it will have to use the asterisk.
    :param word:
    :return:
    """
    return re.findall("_.*?_", word)


def mad_libs(mls):
    """
    'mls' must contains hints surrounded by double underscores.
    'findall' with non-greedy matching finds all the hints, then
    loop through them and display the hints to the user. The input
    function collects their answers. Replace each hand with the answer
    in the original text.
    :param mls: game's text
    :return:
    """
    print("\nGAME: Mad Libs")
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {} ".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        # mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")


if __name__ == '__main__':
    print(one_word_in_a_line("Pit", "I'm working whit Pit"))
    print(one_word_in_a_line_ignore_case("Pit", "Pit is digging a pit"))
    print(start_with("Are", "Are you kidding me?"))
    print(start_with_multiline("If", zen))
    print(end_with("funny!", "Sometimes you are funny!"))
    print(find_digit("Arizona 479, 501, 870. California 209, 213, 650."))
    print(non_greedy_match(underscores_words))
    print(non_greedy_match_question_mark(underscores_words))
    mad_libs(text)
