import re


def find_emails(text):
    """
    It will parse the given string and return a list of emails if found

    Example:
    >>find_emails('hello\n find me here\nemail@gmail.com')
    ['email@gmail.com']

    :param text: string
    :return: list
    """
    return re.findall(r"([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", text)


def get_mentions(text):
    """
    It will return mentions from the text i.e @someone

    :param text: string
    :return: list

    example
    >>> get_mentions('Hi @hero, How are you? I hope @hero2 is fine. BTW say hi to @heroine for me')
    ['hero','hero2','heroine']
    """
    result = re.findall("(^|[^@\w])@(\w{1,15})", text)
    if len(result) != 0:
        result = [i[1] for i in result]
    return result


def get_hashtags(text):
    """
      It will return hashtags from the text i.e #something

      :param text: string
      :return: list

      example
      >>> get_hashtags('my first code #programmer #python #awesome #grepsr')
      ['programmer','python','awesome','grepsr']
      """

    result = re.findall("(^|[^@\w])#(\w{1,15})", text)
    if len(result) != 0:
        result = [i[1] for i in result]
    return result


def get_links(text):
    """
         It will return website links from the text

         :param text: string
         :return: list

         example
         >>> message = 'http://twitter.com Project URL: https://app.grepsr.com/app/project/message/70454'
         >>> get_links(message)
        ['http://twitter.com', 'https://app.grepsr.com/app/project/message/70454']

         """
    result = re.findall(r"(?P<url>https?://[^\s]+)", text)
    return result
