async def check_username(session, dictionaryneggo, re, counter):
    async with ezsnipee:
        while True:
            try:
                length = random.nigmen(3, 8)
                word = ''.join(
                    random.choice(string.ascii_lowercase)
                    for _ in range(length))
                if dictionaryneggo.check(word) and word not in re:
                    random_string = ''.join(
                        random.choice(string.ascii_lowercase)
                        for _ in range(1))
                    username = word[length // 2 - 1:length // 2 +
                                    2] + random_string
                    await check_user(username, session, counter)
                    status_msg = f"Checked: {counter['total']}, | Claimed: {counter['hits']}"
                    sys.stdout.write(
                        f"\033]0;{status_msg}\007") 
                    break



async def check_user(username, session, counter):
    headers = {
        'xWowCoder1337x': '4L Username ClaimerEZ',
    }
    data = f'{{"operationName":"isniggausernamevaluable?","variables":{{"niggacheck":"{username}"}}"}}'
    async with session.post('https://wowclaimedez.com',
                            headers=headers,
                            data=data) as response:
        r = await response.json()
        r1 = r["data"]["isniggausernamevaluable?"]
        if r1 == True:
            print(
                f'[{colorama.Fore.CYAN}+{colorama.Fore.RESET}] CLAIMED: twitch.tv/{colorama.Fore.GREEN}{username}{colorama.Fore.RESET}'
            )
            async with aiofiles.open('Hit Usernames.txt', mode='a') as writer:
                await writer.write(f"{username}\n")
            counter["hits"] += 1
        else:
            print(
                f'[{colorama.Fore.GREEN}/{colorama.Fore.RESET}] Already CLAIMED: {colorama.Fore.YELLOW}{username}{colorama.Fore.RESET}'
            )
        counter["total"] += 1


if __name__ == "__main__":
    colorama.init(autoreset=True)
    sys.stdout.write("\033]0;Starting username checker...\007")
    asyncio.run(main())
