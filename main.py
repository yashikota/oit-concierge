import os

import tweepy


def auth() -> tweepy.OAuthHandler:
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth


def get_mentions() -> list:
    api = tweepy.API(auth())
    mentions_list: list = list()

    mentions = api.mentions_timeline()
    for mention in mentions:
        mentions_list.append(mention.text)

    return mentions_list


def reply_to_mention(mentions_list):
    api = tweepy.API(auth())

    for mention in mentions_list:
        reply_text: str = judge(mention)
        if reply_text:
            api.update_status(status=reply_text, in_reply_to_status_id=mention.id)


def judge(text: str) -> str:
    if "VPN" in text:
        return "VPNのリンクはこちらです。\nhttps://example.com/VPN"
    elif "単位取得率":
        return "単位取得率はこちらです。(学内VPN必須)\nhttps://example.com/単位取得率"

    return "すみません。分かりません。"


def main():
    mentions_list: list = get_mentions()
    reply_to_mention(mentions_list)


if __name__ == "__main__":
    main()
