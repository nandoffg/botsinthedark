# import pymongo
#
#
# print("Trying database connection...")
# bot.password = "2WX0s7aJ2T4iRkL6"
# db_client = pymongo.MongoClient("mongodb+srv://bitd-bot:" + bot.password +
#                                 "@bitd.urg7i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = db_client.admin
# serverStatusResult = db.command("serverStatus")
#
# if db.authenticate("bitd-bot", bot.password):
#     print("Connected to database")
# else:
#     print("Failure connecting to the database")
#
# def update_data(collection, _filter, new_data):
#     mydb = db_client["bitd-bot-db"]
#     mydb[collection].replace_one(_filter, new_data)
#
# def get_data(collection):
#     mydb = db_client["bitd-bot-db"]
#     return mydb[collection].find_one()


@bot.command(name="clock", aliases=["c"])
async def clock(ctx, *title):
    name = ""
    if title:
        for i in title:
            name += i + " "
    else:
        name = "Unnamed Clock"

    embed = discord.Embed(colour=discord.Colour.dark_red())
    embed.set_author(name='New Clock: ' + str(name))
    embed.add_field(name='Instructions',
                    value='React to this message with the according clock parts amount you want to set up for your'
                          ' new clock.', inline=False)
    embed.set_thumbnail(url='https://cdn3.iconfinder.com/data/icons/times-with-hands/100/TIME-HANDS-9-L-512.png')
    clock = await ctx.send(embed=embed)
    clock_id = clock.id
    await clock.add_reaction('🕓')
    await clock.add_reaction('🕕')
    await clock.add_reaction('🕗')
    await clock.add_reaction('🕙')
    await clock.add_reaction('🕛')

    auth_id = str(ctx.message.author.id)
    users = get_data("clocks")["users"]
    ids = []
    new_clock = {'id': str(clock_id), 'parts': str(0), "filled": str(0), "name": str(name)}

    for i in users:
        ids.append(i["id"])

    if str(auth_id) in ids:
        data = users
        clocks = users[ids.index(auth_id)]["clocks"]
        clocks.append(new_clock)
        data[ids.index(auth_id)] = ({"id": auth_id, "clocks": clocks})
        update_data("clocks", get_data("clocks"), {"users": data})

    else:
        data = users
        clocks = []
        clocks.append(new_clock)
        data.append({'id': auth_id, "clocks": clocks})
        update_data("clocks", get_data("clocks"), {"users": data})


@bot.event
async def on_raw_reaction_add(payload):
    user = payload.member
    reaction = payload.emoji
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    embeds = message.embeds
    if bot.user == user:
        return
    data = get_data("clocks")["users"]
    a_ids = []
    old_parts = ""
    old_filled = ""
    old_name = ""
    author_id = ""
    clocks = []
    c_index = 0
    clock_message_id = 0
    print(data)
    for u in data:
        a_ids.append(u["id"])
        for clock in u["clocks"]:
            if str(payload.message_id) == clock["id"]:
                c_index = u["clocks"].index(clock)
                clock_message_id = clock["id"]
                old_parts = clock["parts"]
                old_filled = clock["filled"]
                old_name = clock["name"]
                author_id = u["id"]
                clocks = u["clocks"]
                break
            # c_index += 1

    if str(payload.message_id) == clock_message_id and not user.bot and str(reaction) in ['🕓', '🕕', '🕗', '🕙', '🕛']:

        if str(reaction) == '🕓':
            changed_entry = {'id': str(payload.message_id), 'parts': str(4), "filled": old_filled, "name": old_name}
            data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
            update_data("clocks", get_data("clocks"), {"users": data})
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/754797920670449785/821959778234269696/0.png")
            embed.set_author(name=old_name)
            embed.add_field(name='4-Part Clock', value=':fast_forward: to advance this clock.\n:rewind: to'
                                                       ' retrocede it.\n:x: to delete it.', inline=False)
            await message.edit(embed=embed)

        elif str(reaction) == '🕕':
            changed_entry = {'id': str(payload.message_id), 'parts': str(6), "filled": old_filled, "name": old_name}
            data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
            update_data("clocks", get_data("clocks"), {"users": data})
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/754797920670449785/821960305356570664/0.png")
            embed.set_author(name=old_name)
            embed.add_field(name='6-Part Clock', value=':fast_forward: to advance this clock.\n:rewind: to'
                                                       ' retrocede it.\n:x: to delete it.', inline=False)
            await message.edit(embed=embed)

        elif str(reaction) == '🕗':
            changed_entry = {'id': str(payload.message_id), 'parts': str(8), "filled": old_filled, "name": old_name}
            data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
            update_data("clocks", get_data("clocks"), {"users": data})
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/754797920670449785/821960680105574410/0.png")
            embed.set_author(name=old_name)
            embed.add_field(name='8-Part Clock', value=':fast_forward: to advance this clock.\n:rewind: to'
                                                       ' retrocede it.\n:x: to delete it.', inline=False)
            await message.edit(embed=embed)

        elif str(reaction) == '🕙':
            changed_entry = {'id': str(payload.message_id), 'parts': str(10), "filled": old_filled, "name": old_name}
            data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
            update_data("clocks", get_data("clocks"), {"users": data})
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/754797920670449785/821961092975951872/0.png")
            embed.set_author(name=old_name)
            embed.add_field(name='10-Part Clock', value=':fast_forward: to advance this clock.\n:rewind: to'
                                                        ' retrocede it.\n:x: to delete it.', inline=False)
            await message.edit(embed=embed)

        elif str(reaction) == '🕛':
            changed_entry = {'id': str(payload.message_id), 'parts': str(12), "filled": old_filled, "name": old_name}
            data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
            update_data("clocks", get_data("clocks"), {"users": data})
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/754797920670449785/821961539388309524/0.png")
            embed.set_author(name=old_name)
            embed.add_field(name='12-Part Clock', value=':fast_forward: to advance this clock.\n:rewind: to'
                                                        ' retrocede it.\n:x: to delete it.', inline=False)
            await message.edit(embed=embed)

        await message.clear_reactions()
        await message.add_reaction("⏩")
        await message.add_reaction("❌")
        # await message.add_reaction("✏")

    if str(payload.message_id) == clock_message_id and not user.bot and str(reaction) in ["⏪", "⏩", "❌"]:
        if str(reaction) in ["⏪", "⏩"]:

            if old_parts == "4":
                clocks_4 = {
                    0: "https://cdn.discordapp.com/attachments/754797920670449785/821959778234269696/0.png",
                    1: "https://cdn.discordapp.com/attachments/754797920670449785/821959782378373130/1.png",
                    2: "https://cdn.discordapp.com/attachments/754797920670449785/821959786038951987/2.png",
                    3: "https://cdn.discordapp.com/attachments/754797920670449785/821959791206727690/3.png",
                    4: "https://cdn.discordapp.com/attachments/754797920670449785/821959796332298280/4.png"
                }
                if str(reaction) == "⏩":
                    new_filled = str(int(old_filled) + 1)
                else:
                    new_filled = str(int(old_filled) - 1)

                changed_entry = {'id': str(payload.message_id), 'parts': old_parts, "filled": new_filled,
                                 "name": old_name}
                data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
                update_data("clocks", get_data("clocks"), {"users": data})
                if new_filled == "0":
                    await message.clear_reaction("⏪")
                elif new_filled == old_parts:
                    await message.clear_reaction("⏩")
                else:
                    await message.clear_reactions()
                    await message.add_reaction("⏪")
                    await message.add_reaction("⏩")
                    await message.add_reaction("❌")
                    # await message.add_reaction("✏")

                embed = embeds[0].set_thumbnail(url=clocks_4[int(new_filled)])
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            if old_parts == "6":
                clocks_6 = {
                    0: "https://cdn.discordapp.com/attachments/754797920670449785/821960305356570664/0.png",
                    1: "https://cdn.discordapp.com/attachments/754797920670449785/821960309773697074/1.png",
                    2: "https://cdn.discordapp.com/attachments/754797920670449785/821960314077052938/2.png",
                    3: "https://cdn.discordapp.com/attachments/754797920670449785/821960318091395072/3.png",
                    4: "https://cdn.discordapp.com/attachments/754797920670449785/821960322440495105/4.png",
                    5: "https://cdn.discordapp.com/attachments/754797920670449785/821960326882787328/5.png",
                    6: "https://cdn.discordapp.com/attachments/754797920670449785/821960331814764574/6.png"
                }
                if str(reaction) == "⏩":
                    new_filled = str(int(old_filled) + 1)
                else:
                    new_filled = str(int(old_filled) - 1)

                changed_entry = {'id': str(payload.message_id), 'parts': old_parts, "filled": new_filled,
                                 "name": old_name}
                data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
                update_data("clocks", get_data("clocks"), {"users": data})
                if new_filled == "0":
                    await message.clear_reaction("⏪")
                elif new_filled == old_parts:
                    await message.clear_reaction("⏩")
                else:
                    await message.clear_reactions()
                    await message.add_reaction("⏪")
                    await message.add_reaction("⏩")
                    await message.add_reaction("❌")
                    # await message.add_reaction("✏")

                embed = embeds[0].set_thumbnail(url=clocks_6[int(new_filled)])
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            if old_parts == "8":
                clocks_8 = {
                    0: "https://cdn.discordapp.com/attachments/754797920670449785/821960680105574410/0.png",
                    1: "https://cdn.discordapp.com/attachments/754797920670449785/821960682559373313/1.png",
                    2: "https://cdn.discordapp.com/attachments/754797920670449785/821960684883279902/2.png",
                    3: "https://cdn.discordapp.com/attachments/754797920670449785/821960687646408714/3.png",
                    4: "https://cdn.discordapp.com/attachments/754797920670449785/821960690129436695/4.png",
                    5: "https://cdn.discordapp.com/attachments/754797920670449785/821960692570914886/5.png",
                    6: "https://cdn.discordapp.com/attachments/754797920670449785/821960697734365214/6.png",
                    7: "https://cdn.discordapp.com/attachments/754797920670449785/821960695125245952/7.png",
                    8: "https://cdn.discordapp.com/attachments/754797920670449785/821960702168006676/8.png"
                }
                if str(reaction) == "⏩":
                    new_filled = str(int(old_filled) + 1)
                else:
                    new_filled = str(int(old_filled) - 1)

                changed_entry = {'id': str(payload.message_id), 'parts': old_parts, "filled": new_filled,
                                 "name": old_name}
                data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
                update_data("clocks", get_data("clocks"), {"users": data})
                if new_filled == "0":
                    await message.clear_reaction("⏪")
                elif new_filled == old_parts:
                    await message.clear_reaction("⏩")
                else:
                    await message.clear_reactions()
                    await message.add_reaction("⏪")
                    await message.add_reaction("⏩")
                    await message.add_reaction("❌")
                    # await message.add_reaction("✏")

                embed = embeds[0].set_thumbnail(url=clocks_8[int(new_filled)])
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            if old_parts == "10":
                clocks_10 = {
                    0: "https://cdn.discordapp.com/attachments/754797920670449785/821961092975951872/0.png",
                    1: "https://cdn.discordapp.com/attachments/754797920670449785/821961100597133342/1.png",
                    2: "https://cdn.discordapp.com/attachments/754797920670449785/821961107404095488/2.png",
                    3: "https://cdn.discordapp.com/attachments/754797920670449785/821961113058148392/3.png",
                    4: "https://cdn.discordapp.com/attachments/754797920670449785/821961118724915230/4.png",
                    5: "https://cdn.discordapp.com/attachments/754797920670449785/821961125498454036/5.png",
                    6: "https://cdn.discordapp.com/attachments/754797920670449785/821961129524854844/6.png",
                    7: "https://cdn.discordapp.com/attachments/754797920670449785/821961134889369610/7.png",
                    8: "https://cdn.discordapp.com/attachments/754797920670449785/821961139499958292/8.png",
                    9: "https://cdn.discordapp.com/attachments/754797920670449785/821961145337511939/9.png",
                    10: "https://cdn.discordapp.com/attachments/754797920670449785/821961149372170271/10.png"
                }
                if str(reaction) == "⏩":
                    new_filled = str(int(old_filled) + 1)
                else:
                    new_filled = str(int(old_filled) - 1)

                changed_entry = {'id': str(payload.message_id), 'parts': old_parts, "filled": new_filled,
                                 "name": old_name}
                data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
                update_data("clocks", get_data("clocks"), {"users": data})
                if new_filled == "0":
                    await message.clear_reaction("⏪")
                elif new_filled == old_parts:
                    await message.clear_reaction("⏩")
                else:
                    await message.clear_reactions()
                    await message.add_reaction("⏪")
                    await message.add_reaction("⏩")
                    await message.add_reaction("❌")
                    # await message.add_reaction("✏")

                embed = embeds[0].set_thumbnail(url=clocks_10[int(new_filled)])
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            if old_parts == "12":
                clocks_12 = {
                    0: "https://cdn.discordapp.com/attachments/754797920670449785/821961539388309524/0.png",
                    1: "https://cdn.discordapp.com/attachments/754797920670449785/821961545898393610/1.png",
                    2: "https://cdn.discordapp.com/attachments/754797920670449785/821961550411595826/2.png",
                    3: "https://cdn.discordapp.com/attachments/754797920670449785/821961555822379048/3.png",
                    4: "https://cdn.discordapp.com/attachments/754797920670449785/821961560053645322/4.png",
                    5: "https://cdn.discordapp.com/attachments/754797920670449785/821961563278802974/5.png",
                    6: "https://cdn.discordapp.com/attachments/754797920670449785/821961567402065960/6.png",
                    7: "https://cdn.discordapp.com/attachments/754797920670449785/821961571667673098/7.png",
                    8: "https://cdn.discordapp.com/attachments/754797920670449785/821961575388413992/8.png",
                    9: "https://cdn.discordapp.com/attachments/754797920670449785/821961578541744178/9.png",
                    10: "https://cdn.discordapp.com/attachments/754797920670449785/821961582061944832/10.png",
                    11: "https://cdn.discordapp.com/attachments/754797920670449785/821961586285609000/11.png",
                    12: "https://cdn.discordapp.com/attachments/754797920670449785/821961591322050580/12.png"
                }
                if str(reaction) == "⏩":
                    new_filled = str(int(old_filled) + 1)
                else:
                    new_filled = str(int(old_filled) - 1)

                changed_entry = {'id': str(payload.message_id), 'parts': old_parts, "filled": new_filled,
                                 "name": old_name}
                data[a_ids.index(author_id)]["clocks"][c_index] = changed_entry
                update_data("clocks", get_data("clocks"), {"users": data})
                if new_filled == "0":
                    await message.clear_reaction("⏪")
                elif new_filled == old_parts:
                    await message.clear_reaction("⏩")
                else:
                    await message.clear_reactions()
                    await message.add_reaction("⏪")
                    await message.add_reaction("⏩")
                    await message.add_reaction("❌")
                    # await message.add_reaction("✏")

                embed = embeds[0].set_thumbnail(url=clocks_12[int(new_filled)])
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

        elif str(reaction) == "❌":
            await message.delete()
            data[a_ids.index(author_id)]["clocks"].pop(c_index)
            update_data("clocks", get_data("clocks"), {"users": data})


           ###################################################################

            auth_id = str(ctx.message.author.id)
            users = get_data("clocks")["users"]
            ids = []
            new_clock = {'parts': str(name[1]), "filled": str(0), "name": str(name[0])}

            for i in users:
                ids.append(i["id"])

            if str(auth_id) in ids:
                data = users
                print(data)
                clocks = users[ids.index(auth_id)]["clocks"]
                print(clocks)
                clocks.append(new_clock)
                print(clocks)
                data[ids.index(auth_id)] = ({"id": auth_id, "clocks": clocks})
                print(data[ids.index(auth_id)])
                update_data("clocks", get_data("clocks"), {"users": data})

            else:
                data = users
                print(data)
                clocks = new_clock
                print(clocks)
                data.append({'id': auth_id, "clocks": clocks})
                print(data)
                update_data("clocks", get_data("clocks"), {"users": data})
