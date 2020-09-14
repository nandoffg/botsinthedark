# Bots in the Dark v.1.2
# AUTHOR: FERNANDO GOMES

from discord.ext import commands
import discord
import random

# from discord import Status
# import asyncio
# import requests
# from bs4 import BeautifulSoup
# import pymongo
# import datetime

print('Starting...')
client = discord.Client()
bot = commands.Bot(command_prefix='=')
bot.remove_command("help")

# INSERT BOT TOKE HERE IN QUOTES VVVVVVVVVVVVVV
token = "NzU0Nzg2OTUyNjc4NjA0OTYy.X150IA.gykEs6J5I5CsOHI6Ix-5ehgzt4c"


# print("Trying database connection...")
# bot.password = "bTqZ1Rr01Y9v2mOh"
# db_client = pymongo.MongoClient("mongodb+srv://aria-bot:" + bot.password +
#                                 "@aria-db.txtfq.gcp.mongodb.net/aria-bot-db?retryWrites=true&w=majority")
# db = db_client.admin
# serverStatusResult = db.command("serverStatus")
# mydb = db_client["aria-bot-db"]
#
# if db.authenticate("aria-bot", bot.password):
#     print("Connected to database")
# else:
#     print("Failure connecting to the database")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    bot.owner = bot.get_guild(
        750136732380561464).get_member(115581181017194500)
    dm_c = await bot.owner.create_dm()
    await dm_c.send("Bot restarted.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='=help'))


@bot.event
async def on_message(message):
    if not message.author.bot and isinstance(message.channel, discord.channel.DMChannel):
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='Hello there scoundrel!')
        embed.add_field(name="Bots in the Dark", value="\nI'm a bot with several useful functions.\nType `=h` or `=help` for more information on the "
                                                       "commands. If you want to add me to your Discord server, go [here]"
                                                       "(https://discord.com/oauth2/authorize?client_id=754786952678604962&scope=bot&permissions"
                                                       "=511040) to invite me. "
                                                       "\n\nI'm able to roll dice, spill out Blades rolls results, generate random fictional things "
                                                       "for your game, such as streets, buildings, "
                                                       "demons, scores, people and many others."
                                                       "\nIf you want to back this bot, go [here](www.patreon.com/fernandogomes).", inline=False)
        await message.channel.send(embed=embed)
    else:
        await bot.process_commands(message)


@bot.command(name='generate', aliases=["g"])
async def generate(ctx, option):
    opt = str(option.lower())
    if opt == "street":
        mood = ["dark", "cold", "bright", "lively", "quiet", "refined", "abandoned", "decrepit", "cramped", "noisy", "cozy", "warm"]
        sights = ["rain slick", "oil slick", "dancing shadows", "flickering lights", "mist", "fog", "frost", "fleeting shapes",
                  "echoes in the ghost field", "soot", "ash", "clouds", "grime", "crackling electricity", "wires", "mechanisms"]
        sounds = ["machinery", "workers", "fluttering cloth", "howling wind", "laughter", "song", "music", "whispers", "echoes", "strange voices",
                  "thunder", "driving rain", "bells", "clock chimes", "harbor horns"]
        smells = ["cook fires", "furnaces", "damp wood", "decay", "refuse", "animals", "hides", "blood", "chemicals", "distillates", "fumes",
                  "rain water", "ocean", "ozone", "electroplasmic discharges"]
        use = ["residential", "craft", "labor", "shops", "trade", "hospitality", "law", "government", "public space", "power and electricity",
               "manufacture", "transportation", "leisure", "vice", "entertainment", "storage", "cultivation", "academic", "arts"]
        type_of_street = ["narrow lane", "tight alley", "twisting street", "rough road", "bridge", "waterway", "closed court", "open plaza", "paved "
                                                                                                                                             "avenue",
                          "tunnel", "wide boulevard", "roundabout", "elevated road", "flooded street", "suspended way", "subterranean alley",
                          "floating lane",
                          "private street", "gated passage"]
        details = ["metal supports", "ironwork", "gates", "fences", "belching chimneys", "metal grates", "hatches", "doors", "clockwork mechanisms",
                   "ringing bells", "stairs", "ramps", "terraces", "wooden scaffolds", "skyways", "rooftop spaces", "rails", "train cars",
                   "hidden passages", "banners", "pennants", "festival decorations", "crowd", "parade", "riot", "street performers",
                   "makeshift stalls", "shelters", "crisscrossing routes", "gang markings", "patrol posts", "lookouts", "stocks",
                   "public punishment", "street crier", "visionary", "news stand", "public notices", "stray animals", "landscaping",
                   "muck", "mire", "construction", "demolition", "foul runoff", "fumes", "smoke", "orphans", "beggars", "ancient ruin",
                   "leering gargoyles", "spirit chimes", "wards", "eerie", "emptiness", "quarantine", "lockdown", "shrine offerings", "street ritual"]
        props = ["Nets", "Ropes", "Crates", "Boxes", "Cables", "Chains", "Drain Pipes", "Water Pump", "Oil Drums", "Brick Pile", "Iron Bars",
                 "Wooden Boards", "Cut Stones", "Loose Rocks", "Cement Buckets", "Sewer Grate", "Rotting Refuse", "Mud Puddles", "Discarded Junk",
                 "Carrion & Crows", "Sodden Trash", "Carriages", "Push Carts", "Moored Boats", "Cargo Barge", "Gondolas", "Wagons", "Crane & Pulleys",
                 "Cargo Bales", "Metal Ingots", "Industrial Forge", "Coal", "Fuel", "Waste Bins", "Street Lamps", "Electric Wires", "Junction Boxes",
                 "Spotlight Tower", "Clock Tower", "Messenger Post", "Withered Trees", "Monument", "Fountain", "Mossy Ruin", "Collapsed Building",
                 "Flimsy Hovel", "Barricade", "Gate", "Checkpoint", "Piled Rubble", "Canal Lock", "Lightning Barrier", "Food Stall",
                 "Vendor Stall", "Barrels", "Casks", "Makeshift Shrine", "News Stands", "Stockades"]
        phrase = "It's a **" + random.choice(mood) + " " + random.choice(type_of_street) + "**, with **" + random.choice(sights) + "**, **" \
                 + random.choice(sounds) + "** noises and smell of **" + random.choice(smells) + "**. It's mostly used for **" + \
                 random.choice(use) + "**, with " + random.choice(details) + " and " + random.choice(props).lower() + " in it."

        total = len(mood)*len(sights)*len(sounds)*len(smells)*len(use)*len(type_of_street)*len(details)*len(props)

        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        embed.add_field(name="Random seeds:", value=str(total), inline=False)
        await ctx.send(embed=embed)

    elif opt == "demon":
        demon_types = ["a humanoid with bestial or elemental features", "a humanoid with bestial or elemental features",
                       "a humanoid with bestial or elemental features", "an animal", "a monstrous being", "an amorphous being"]
        demon_desires = ["Mayhem", "Murder", "Justice", "Corruption", "Power", "Control", "Knowledge", "Pleasure", "Suffering", "War", "Revenge",
                         "Chaos", "Freedom", "Savagery", "Manipulation", "Deception" "Fear", "Achievement"]
        demon_features = ["Black shark eyes", "Scales (onyx, iridescent,crystalline, metallic, etc.)", "Razor-sharp claws", "Bony protrusions",
                          "Multiple eyes", "a Lashing tail", "Leathery wings", "Spines", "Dripping ichor from his body", "Glowing eyes or markings",
                          "Hair or fur (drifting as if underwater, burning with a cool fire, etc.)", "Feathers", "Multiple arms", "Tentacles",
                          "a Hard shell, metallic plates", "an effect on Lights, that dim or flare",
                          "an effect on Plants, that wither or grow wildly", "an effect on Mechanisms, that grind to a halt",
                          "an effect on Liquids, that freezes, boils, turns to blood or ashes"]
        demon_names = ["Korvaeth", "Sevraxis", "Argaz", "Zalvroxos", "Kethtera", "Arkeveron", "Ixis", "Kyronax", "Voldranai", "Esketra", "Ardranax",
                       "Kylastra", "Oryxus", "Ahazu", "Tyraxis", "Azarax", "Vaskari"]

        phrase = "You see **" + random.choice(demon_types).lower() + "** that has **" + random.choice(demon_features).lower() + \
                 "**. Their demon desire is **" + random.choice(demon_desires).lower() + "**. Their name is **" + \
                 random.choice(demon_names).capitalize() + "**."
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "ghost":
        ghost_traits = ["Jealous", "Desperate", "Violent", "Hysterical", "Skittish", "Fleeting", "Curious", "Deceptive", "Clever", "Probing",
                        "Knowledgeable", "Charming", "Prophetic", "Insightful", "True", "Revelatory", "Guiding", "Instructive", "Reactive",
                        "Territorial", "Dominant", "Insistent", "Bold", "Demanding", "Angry", "Volatile", "Aggressive", "Wild", "Savage", "Vengeful",
                        "Mad", "Chaotic", "Bizarre", "Destructive", "Insane", "Vile"]
        ghost_more_traits = ["Frost, Chill", "Cold wind", "Faint visions of the local past", "Electrical discharge", "Weird shadows", "Faint echoes",
                             "Mist", "Fog", "Rushing wind", "Intense visual echoes", "Intense magnetism", "Disturbing shadows", "Thunderous sounds",
                             "Freezing fog", "Storm winds", "Pitch darkness", "Lightning", "Clutching shadows", "Voices in your head"]

        phrase = "Add these characteristics on top of another person's: \nYou feel a **" + random.choice(ghost_traits).lower() + \
                 "** aura emanating from them." + "\nAround them you also see the effects of **" + random.choice(ghost_more_traits).lower() + "**."
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "fgod":
        gods = ["The One Within Many", "The Silver Fire", "The Rapturous Chord", "The Fallen Star", "The Lord of the Depths", "The Silent Song",
                "The Lady of Thorns", "Our Blood Spilled in Glory", "The Ram", "The Empty Vessel", "The Closed Eye", "The Hand of Sorrow",
                "That Which Hungers", "The Thousand Faces", "The Web of Pain", "The Pillars of Night", "The Burned King", "The Father of the Abyss",
                "The Forsaken Legion", "The Unbroken Sun", "The Revelation", "The Radiant Word", "The Shrouded Queen", "The Reconciler",
                "The Cloud of Woe", "The Broken Circle", "The Conqueror", "She Who Slays in Darkness", "The Dream Beyond Death",
                "The Blood Dimmed Tide", "The Guardian of the Gates", "The Maw of the Void", "The Keeper of the Flame", "The Throne of Judgment",
                "The Lost Crown", "The Golden Stag"]
        cult_practices = ["Sacrifice: Fed to specially consecrated beasts / Savaged (eaten?) by frenzied cult mob.",
                          "Desecration: Mindless, pointless chaos; sewing the seeds of anarchy.",
                          "Desecration: Corruption of acolytes to prepare them for transformation.",
                          "Desecration: Manipulation of authorities / institutions to appropriate their power.",
                          "Desecration: Defilement of place / object / ritual to humiliate another order.",
                          "Desecration: Corruption of place / object / ritual / tradition to appropriate its power.",
                          "Desecration: Debasement or defilement of one sworn to an enemy order.",
                          "Consecration: Wards / runes / spirits bound to shun enemies of the order.",
                          "Consecration: Creation of blessed idols / artwork / ritual spaces / artifacts.",
                          "Consecration: Purify / bless cult followers with tattoos / scarification / mutilation.",
                          "Consecration: Baptism / blessing of an acolyte or object by immersion in spirit well.",
                          "Consecration: Purification of the gates that give passage to the god into this world.",
                          "Consecration: Purification by bathing in sacred fluid (blood, wine, milk, oil, etc.).",
                          "Destruction: Eradication of social / legal / cultural elements that threaten the order.",
                          "Destruction: Eradication of weapons / objects / sites / rituals that can harm the god.",
                          "Destruction: Shattering of ritual objects / altars / temples sacred to an enemy order.",
                          "Destruction: The breaking of the seals that keep the god from this world.",
                          "Destruction: Ritual eradication of a spirit or demon",
                          "Destruction: Ritual burning of sacred objects (rune-papers, effigies, flesh, hair).",
                          "Acquisition: The ghosts of prophets / mystics / founders / enemies of the order.",
                          "Acquisition: Properties aligned with sacred geometry or attuned by mystical events.",
                          "Acquisition: The severed body parts (heads, hands, tongues) of heretics or apostates.",
                          "Acquisition: The original holy writings of the prophet / master / saint.",
                          "Acquisition: The shards of a shattered sacred object (jewel, sword, skull, stone).",
                          "Acquisition: A collection of eyes / hearts / blood from mystics or demons.",
                          "Congregation: A reenactment / dumb-show of a sacred event.",
                          "Congregation: A group vision / dream-quest via essences, drugs, or meditation.",
                          "Congregation: A pilgrimage to a sacred place or being in the deathlands / at sea.",
                          "Congregation: Occupying a sacred nexus point during an astrological confluence.",
                          "Congregation: Sacred hymns or prayers for days without ceasing.",
                          "Congregation: An orgy of pleasure (sex, food, dance, music) and/or pain.",
                          "Sacrifice: Slain by arcane means (electrocuted, spirit shattered, death-cursed).",
                          "Sacrifice: Ritually killed and claimed as anointed spirit-champion.",
                          "Sacrifice: Progressively overdosed with mind-expanding drugs.",
                          "Sacrifice: Ritually bled upon the sacred altar.",
                          "Sacrifice: Pitted against an anointed champion in death arena."]

        phrase = "This is the Forgotten God: **" + random.choice(gods) + "**.\nTheir cult's practices are " + random.choice(cult_practices)
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random Forgotten God.')
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "horror":
        horrors = ["Reeking Tar", "Writhing Mass", "Radiant Being", "Crystalline Shards", "Creeping Growth", "Animated Stone", "Cloud of Burning Ash",
                   "Shadow Being", "Swarm of Insects", "Toxic Cloud", "Fiery Being", "Liquid Being", "Flayed Being", "Shambling Rags",
                   "Freezing Fire", "Impossible Geometry", "Monstrous Animal", "Shimmering Spheres", "Twisting Machinery", "Psychic Mist",
                   "Throbbing Viscera", "Metallic Being", "Coil of Thorns", "Hypnotic Lights", "Oozing Slug", "Tremulous Vibrations", "Lashing Hooks",
                   "Skeleton of Black Glass", "Flowing Quicksilver", "Clutching Darkness", "Floating Octopoid", "Cloying Vapors", "Swirling Mucus",
                   "Serpent Being", "Insectoid Being", "Consuming Orb"]
        phrase = "You see this **" + random.choice(horrors).lower() + "** forming in front of you."
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "bargain":
        bargains = ["What’s Our Take? - Your gang wants a bigger cut of this score. -1 or -2 Coin on this score's Payoff.",
                    "Walls Have Ears - Word gets out to a faction your crew is friendly with that you did a job against their ally if the Heat for "
                    "this score is 2 or more.",
                    "Hunter or Hunted - So intent on tailing your mark, you fail to notice you yourself are followed by a rival.",
                    "All Or Nothing - If the danger comes to pass you cannot resist it.",
                    "Now Or Never - If you don’t overcome the obstacle entirely, you must abandon it forever.",
                    "Quelle Horreur! - You’re in for some sleepless nights. -1d on the next long-term project clock roll.",
                    "Lay Out - You're gonna find yourself face-down or flat on your ass, no matter what else the outcome.",
                    "Leave Yourself Open - In the face of the danger at hand, you make a bolder move and expose yourself on doing so, you'll be in a lower position from now on.",
                    "SMASH - whatever you're using for this, it's broken, shattered, ruined. And it probably makes a bit of noise.",
                    "Ghostly attraction - Your activities attract ghosts or other things...",
                    "Hell hath no fury like a lover spurned... It's love at first sight. Your mark is besotted, you can do no wrong other than ignore them and become romantically stalked.",
                    "Bombs away - Things flung by rooftop revellers attract unwanted attention to your activities, making things loud & chaotic. +4 Heat for this score.",
                    "Once more unto the breach - No one trusts your judgement.For the rest of the score, no one can Assist you anymore.",
                    "Sign here - Accept the next devil's bargain or suffer -1D.",
                    "Falling or stalling - The floor beneath you cracks to the brink of collapse. Any action now is desperate.",
                    "Hot or not - Something you wear is on fire.",
                    "Bold or old - A thin needle pierces your flesh. Start a 4 part clock. Tick it with every action's consequence of that player. When it fills, the poison slams you (level 3 harm).",
                    "Player or played - You are a pawn in a bigger play. Next downtime an NPC faction takes extra advances to their project clocks."]
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name="Generating random Devil's Bargain")
        embed.add_field(name="Offer: **+1d** on roll in exchange for: ", value=random.choice(bargains), inline=False)
        await ctx.send(embed=embed)

    elif opt == "score":
        client_target = ["an Academic", "a Scholar", "a Laborer", "a Tradesman", "a Courier", "a Sailor", "a Merchant", "a Shopkeeper", "an Artist",
                         "a Writer", "a Doctor", "an Alchemist", "a Drug Dealer", "a Supplier", "a Mercenary", "a Thug", "a Fence", "a Gambler",
                         "a Spy", "an Informant", "a Smuggler", "a Thief", "a Crime Boss", "a Noble", "an Official", "a Banker", "a Captain",
                         "a Revolutionary", "a Refugee", "a Clergy", "a Cultist", "a Constable", "an Inspector", "a Magistrate", "a Ward Boss",
                         "a Ghost of someone (generate a person)", "an Occult Collector", "a Vampire", "anOther kind of Undead",
                         "a Demon (disguised)", "a Possessed", "a Hollow", "a Whisper", "a Cultist"]
        work = ["Stalking", "Surveillance", "Sabotage", "Arson", "Lift", "Plant", "Poison", "Arrange Accident", "Burglary", "Heist", "Impersonate",
                "Misdirect", "Assassinate", "Disappear", "Ransom", "Terrorize", "Extort", "Destroy", "Deface", "Raid", "Defend", "Rob", "Strong-arm",
                "Escort", "Security", "Smuggle", "Courier", "Blackmail", "Discredit", "Con", "Espionage", "Locate", "Hide", "Negotiate", "Threaten",
                "Curse", "Sanctify", "Banish", "Summon", "Extract Essence", "Place runes", "Remove Runes", "Perform ritual", "Stop Ritual", "Hollow",
                "Revivify"]
        twist = ["An element is a cover for heretic spirit cult practices", "An occultist has foreseen this job and warned the parties involved",
                 "Rogue spirits possess some/most/all of the people involved", "Rogue spirits haunt the location",
                 "The job furthers a demon’s secret agenda", "The job furthers a vampire’s secret agenda",
                 "An element is a front for a criminal enterprise", "A dangerous gang uses the location", "The job is a trap laid by your enemies",
                 "The job is a test for another job", "The job furthers a merchant lord’s secret agenda",
                 "The job furthers a crime boss’s secret agenda", "The job requires travel by electrorail", "Must visit the deathlands to do the job",
                 "The job requires sea travel", "The location moves around (site changes, it’s on a vehicle, etc.)",
                 "The job furthers a revolutionary’s secret agenda", "The job furthers a city official’s secret agenda"]
        connection = ["Friend", "Rival", "Vice purveyor", "Contact", "Doskvol notable", "Ghost", "Demon", "God"]
        faction = ["The Unseen", "The Silver Nails", "Lord Scurlock", "The Hive", "The Circle of Flame", "The Crows", "The Lampblacks",
                   "The Red Sashes", "The Dimmer Sisters", "The Grinders", "The Billhooks", "The Wraiths", "The Gray Cloaks", "Ulf Ironborn",
                   "The Fog Hounds", "The Lost", "City Council", "The Foundation", "Ironhook Prison", "Spirit Wardens", "Bluecoats", "Inspectors",
                   "Imperial Military", "Laborers", "Servants", "Sparkwrights", "Cyphers", "Ink Rakes", "A Consulate", "Ministry of Preservation",
                   "Leviathan Hunters", "Sailors", "Dockers", "Gondoliers", "Cabbies", "Rail Jacks", "The Brigade", "The Church of Ecstasy",
                   "The Weeping Lady", "The Forgotten Gods", "Path of Echoes", "Reconciled", "Skovlander Refugees", "Deathlands", "Scavengers"]

        phrase = "**" + random.choice(client_target).capitalize() + "** wants someone to do a/an **" + random.choice(work).lower() + "** job over **" \
                 + random.choice(client_target).lower() + "**. But **" + random.choice(twist).lower() + "** and/or is connected to a **" + \
                 random.choice(connection).lower() + "** and/or **" + random.choice(faction) + "**."
        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "people":
        looks = ["Large", "Lovely", "Weathered", "Chiseled", "Handsome", "Athletic", "Slim", "Dark", "Fair", "Stout", "Delicate", "Scarred", "Bony",
                 "Worn", "Rough", "Plump", "Wiry", "Striking", "Short", "Tall", "Sexy", "Wild", "Elegant", "Stooped", "Cute", "Plain", "Old", "Young",
                 "Stylish", "Strange", "Disfigured", "Maimed", "Glasses bearing", "Monocle bearing", "Prosthetic bearing", "Crippled", "Long Haired",
                 "Beard", "Wig bearing", "Shorn", "Bald", "Tattooed"]
        heritage = ["tycherosi", "severosi", "dagger islander", "iruvian", "skovlander", "skovlander", "akorosi", "akorosi", "akorosi", "akorosi",
                    "akorosi", "akorosi"]

        demo_trait = ["has feathers instead of hair", "has cat's eyes", "has claws instead of nails", "has a pale bluish skin",
                      "has black shark eyes",
                      'has a yellow cyst like sores that occasionally break and release "harmless” flies', "has transparent skin",
                      "has a mouth that extends ear to ear", "has stain glass finger nails", "has stain glass hair", "has two faces on one head",
                      "has several rows of differing animal teeth", "has scales. Scales everywhere",
                      "has an arm that is made of glass and is to all appearances hollowing. A different substance/organism replaces the hollow space"
                      " each time they sleep",
                      "has a a transparent film over the skin covering their heart. In place of their heart is a scale model of a leviathan hunter "
                      "ship, always tossing about in a squall",
                      "has facial features with umbilicals that constantly crawl about their head",
                      "talks with a chorus of voices, some old, some young, some pained some ecstatic", "has hands for feet",
                      "has fly limbs for eyelashes", "has a crown of avian beaks, each beak from a different bird",
                      "has the ability to heal wounds fine, whenever they get physically hurt, but the healing replaces the wounded tissue with "
                      "nonliving matter (steel cable for muscle fiber, paper for skin, etc.)",
                      "has skin that changes to a new, outlandish colour during the course of every day",
                      "has hair that is luminous", "has a third, smaller arm in place of their tongue",
                      "has differently sized handprints all over their body, some look like burns, some look like makeup, "
                      "some look like handprints pressing up from the inside. The fingers on each “hand” move and quiver",
                      "has an animal tail", "has skin that flakes as drops of bioluminescence. These skin flakes that turn into shreds of tree bark"
                                            " with insects on them before rapidly decomposing", "has mollusk chitin",
                      "has arms that have an extra elbow like "
                      "Steve Erickson’s Forkul Assail"]
        type_of_street = ["man", "man", "woman", "woman", "man", "man", "woman", "woman", "ambiguous", "concealed"]
        goals = ["Wealth", "Power", "Authority", "Prestige", "Fame", "Control", "Knowledge", "Pleasure", "Revenge", "Freedom",
                 "Achievement", "Happiness", "Infamy", "Fear", "Respect", "Love", "Change", "Chaos", "Destruction", "Justice", "Cooperation"]
        preferred_methods = ["Violence", "Threats", "Negotiation", "Study", "Manipulation", "Strategy", "Theft", "Arcane methods", "Commerce",
                             "Hard Work",
                             "Law", "Politics", "Sabotage", "Subterfuge", "Alchemy", "Blackmail", "Teamwork", "Espionage", "Chaos"]
        prof_comm = ["Baker", "Barber", "Blacksmith", "Brewer", "Butcher", "Carpenter", "Cartwright", "Chandler", "Clerk", "Cobbler", "Cooper",
                     "Cultivator", "Driver", "Dyer", "Embroiderer", "Fishmonger", "Gondolier", "Guard", "Leatherworker", "Mason", "Merchant",
                     "Roofer", "Ropemaker", "Rug Maker", "Servant", "Shipwright", "Criminal", "Tailor", "Tanner", "Tinkerer", "Vendor",
                     "Weaver", "Woodworker", "Goat Herd", "Messenger", "Sailor"]
        prof_rare = ["Advocate", "Architect", "Artist", "Author", "Bailiff", "Apiarist", "Banker", "Bounty Hunter", "Clockmaker", "Courtesan",
                     "Furrier", "Glass Blower", "Diplomat", "Jailer", "Jeweler", "Leech", "Locksmith", "Magistrate", "Musician", "Physicker",
                     "Plumber", "Printer", "Scholar", "Scribe", "Sparkwright", "Tax Collector", "Treasurer", "Whisper", "Composer", "Steward",
                     "Captain", "Spirit Warden", "Journalist", "Explorer", "Rail Jack", "Soldier"]

        style = ["a Tricorn Hat", "a Long Coat", "a Hood & Veil", "a Short Cloak", "a Knit Cap", "a Slim Jacket", "a Hooded Coat", "Tall Boots",
                 "Work Boots", "a Mask & Robes", "a Suit & Vest", "a Collared Shirt", "Suspenders", "a Rough Tunic", "a Skirt & Blouse",
                 "a Wide Belt", "a Fitted Dress", "a Heavy Cloak", "a Thick Greatcoat", "Soft Boots", "Loose Silks", "Sharp Trousers", "a Waxed Coat",
                 "a Long Scarf", "Leathers", "an Eelskin Bodysuit", "Hide & Furs", "a Uniform", "Tatters", "Fitted Leggings", "an Apron",
                 "Heavy Gloves", "a Face Mask", "a Tool Belt", "Crutches", "a Cane", "a Wheelchair"]
        traits = ["charming", "cold", "cavalier", "brash", "suspicious", "obsessive", "shrewd", "quiet", "moody", "fierce", "careless",
                  "secretive", "ruthless", "calculating", "defiant", "gracious", "insightful", "dishonest", "Patient", "vicious", "sophisticated",
                  "paranoid", "enthusiastic", "elitist", "savage", "cooperative", "arrogant", "confident", "vain", "daring", "volatile", "candid",
                  "subtle", "melancholic", "enigmatic", "calm"]
        interests = ["Fine whiskey, wine, beer", "Fine food, restaurants", "Fine clothes, jewelry, furs", "Fine arts, opera, theater",
                     "Painting, drawing, sculpture", "History, legends", "Architecture, furnishings", "Poetry, novels, writing",
                     "Pit-fighting, duels", "Forgotten gods", "Church of Ecstasy", "Path of Echoes", "Weeping Lady, charity",
                     "Antiques, artifacts, curios", "Horses, riding", "Gadgets, new technology", "Weapons collector", "Music, instruments, dance",
                     "Hunting, shooting", "Cooking, gardening", "Gambling, cards, dice", "Natural philosophy", "Drugs, essences, tobacco",
                     "Lovers, romance, trysts", "Parties, social events", "Exploration, adventure", "Pets (birds, dogs, cats)",
                     "Craft (leatherwork, etc.)", "Ships, boating", "Politics, journalism", "Arcane books, rituals", "Alchemy, medicine",
                     "Essences, alchemy", "Demon lore legends", "Pre-cataclysm legends"]
        quirks = ["Reclusive. Prefers to interact via messengers", "Massive debts (to banks / criminals / family)",
                  "Blind to flaws in friends, allies, family, etc", "Once hollowed, then restored. Immune to spirits",
                  "Has chronic illness that requires frequent care", "Secretly (openly?) controlled by possessing spirit",
                  "Serves a demon’s agenda (knowingly or not)", "Proud of heritage, traditions, native language",
                  "Concerned with appearances, gossip, peers", "Drug / alcohol abuser. Often impaired by their vice",
                  "Holds their position due to blackmail", "Relies on council to make decisions", "Involved with war crimes from the Unity War",
                  "Leads a double life using cover identity", "Black sheep / outcast from family or organization",
                  "In prison or under noble’s house arrest", "Well-traveled. Connections outside Doskvol",
                  "Revolutionary. Plots against the Imperium", "Inherited their position. May not deserve / want it",
                  "Celebrity. Popularized in print / song / theater", "Surrounded by sycophants, supplicants, toadies",
                  "Superstitious. Believes in signs, magic numbers", "Devoted to their family", "A fraud. Some important aspect is fabricated",
                  "Deeply traditional. Opposed to new ideas", "Is blindly faithful to an ideal, group, or tradition",
                  "Keeps detailed journals, notes, records, ledgers", "Intense, unreasonable phobia or loathing",
                  "Married into important / powerful family", "Holds their position to spy for another faction",
                  "Cursed, haunted, harassed by spirits or demon", "Visionary. Holds radical views for future",
                  "Bigoted against culture / belief / social class", "Spotless reputation. Highly regarded",
                  "Scandalous reputation (deserved or not)", ]
        names_m = ["Adric", "Aldo", "Amosen", "Andrel", "Arden", "Arquo", "Arvus", "Branon", "Brance", "Bricks", "Carro", "Casslyn", "Cavelle",
                   "Corille", "Cross", "Crowl", "Drav", "Edlun", "Grine", "Helles", "Holtz", "Kelyr", "Kobb", "Kristov", "Laudius", "Milos", "Morlan",
                   "Narcus", "Noggs", "Orlan", "Phin", "Ring", "Roethe", "Skannon", "Stavrul", "Stev", "Timoth", "Tocker", "Veleris", "Vond",
                   "Weaver", "Wester"]
        name_f = ["Arlyn", "Ashlyn", "Brace", "Brena", "Candra", "Carissa", "Casslyn", "Clave", "Cyrene", "Daphnia", "Emeline", "Hix",
                  "Kamelin", "Lauria", "Lenia", "Lizete", "Lorette", "Lucella", "Lynthia", "Mara", "Myre", "Naria", "Odrienne",
                  "Polonia", "Quess", "Remira", "Sesereth", "Sethla", "Syra", "Talitha", "Tesslyn", "Thena", "Una", "Vaurin",
                  "Veretta", "Vestine", "Vey", "Volette", "Zamira"]
        fam_names = ["Ankhayat", "Arran", "Athanoch", "Basran", "Boden", "Booker", "Bowman", "Bowmore", "Breakiron", "Brogan", "Clelland", "Clermont",
                     "Coleburn", "Comber", "Daava", "Dalmore", "Danfield", "Dunvil", "Farros", "Grine", "Haig", "Helker", "Helles", "Hellyers",
                     "Jayan", "Jeduin", "Kardera", "Karstas", "Keel", "Kessarin", "Kinclaith", "Lomond", "Maroden", "Michter", "Morriston",
                     "Penderyn", "Prichard", "Rowan", "Sevoy", "Skelkallan", "Skora", "Slane", "Strangford", "Strathmill", "Templeton", "Tyrconnell",
                     "Vale", "Walund", "Welker"]
        aliases = ["Bell", "Birch", "Bricks", "Bug", "Chime", "Coil", "Cricket", "Cross", "Crow", "Echo", "Flint", "Frog", "Frost", "Grip", "Gunner",
                   "Hammer", "Hook", "Junker", "Mist", "Moon", "Nail", "Needle", "Ogre", "Pool", "Ring", "Ruby", "Silver", "Skinner", "Song", "Spur",
                   "Tackle", "Thistle", "Thorn", "Tick-Tock", "Twelves", "Vixen", "Whip", "Wicker"]

        clothing = []
        prof = ""
        x = 0
        while x < 2:
            pick = random.choice(style).lower()
            if pick not in clothing:
                clothing.append(pick)
                x += 1
        for x in range(1, 11):
            if x <= 2:
                prof = random.choice(prof_rare).lower()
            else:
                prof = random.choice(prof_comm).lower()

        demonic = ''
        herit = random.choice(heritage).lower()
        if herit == 'tycherosi':
            demonic = 'This person ' + random.choice(demo_trait) + '.'

        gender = random.choice(type_of_street).lower()
        if gender == 'man':
            name = random.choice(names_m).capitalize()
        elif gender == 'woman':
            name = random.choice(name_f).capitalize()
        else:
            name = random.choice(name_f + names_m).capitalize()

        phrase = name + ' **"' + random.choice(aliases).capitalize() + '"** ' + random.choice(fam_names).capitalize() + \
                 " is a **" + random.choice(looks).lower() + " " + herit + " " + gender + \
                 "**. That is a **" + prof + "** that yearns for **" + random.choice(goals).lower() + "** through **" + \
                 random.choice(preferred_methods).lower() + "**. They come in **" + clothing[0] + "** and **" + clothing[1] + \
                 "** and are interested in **" + random.choice(interests).lower() + "**. \n" + random.choice(quirks) + ". \n" + demonic

        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)

    elif opt == "building":
        material = ["Gray Brick", "Stone & Timbers", "Cut Stone Blocks", "Wooden Boards", "Plaster Board & Timbers", "Metal Sheeting"]
        details = ["Tile Work", "Iron Work", "Glass Work", "Stone Work", "Wood Work", "Landscaping"]
        use_com = ["Bunk House", "Inn", "Tavern", "Gambling Hall", "Drug Den", "Brothel", "Market", "Workshop", "Bakery", "Butchery", "Forge",
                   "Tailory", "Work House", "Goat Stables", "Brewery", "Watch Post", "Court", "Jail", "Dock", "Ruin", "Row Houses", "Tenements",
                   "Apartment Building", "Small House", "Bath House", "Shrine", "Tattooist", "Physicker", "Fighting Pits", "Square", "Fountain",
                   "Grotto", "Warehouse", "Stockyard", "Factory", "Refinery", "Eelery", "Mushroom Garden"]
        use_rare = ["Market House", "Restaurant", "Bar", "Lounge", "Academy", "Salon", "Cafe", "Floristry", "Tobacconist", "Book Shop", "Jeweler",
                    "Clothier", "Gallery", "Apothecary", "Horse Stables", "Distillery", "Vintner", "Master Artisan", "Boat House", "Theater",
                    "Opera House", "Apartment Building", "Townhouse", "Manor House", "Villa", "Clinic", "Temple", "Cistern", "Watch Post",
                    "Park", "Monument", "Archive", "Spiritualist", "Bank", "Alchemist", "Power Plant", "Radiant Energy Garden"]
        more_details = ["Dripping Water", "Creaking Floorboards", "Roaring Fires", "Smoky Lamps", "Buzzing Electric Lights", "Ticking Clockworks",
                        "Plants", "Flowers", "Wall Hangings", "Artwork all around", "Shuttered Windows", "Heavy Curtains", "Thick Carpet",
                        "Dust all around", "Detritus all around", "Wear and tear", "Damage everywhere", "Threadbare", "that is Tattered",
                        "Utilitarian Furnishings", "Elegant Finery", "a Lush feeling to it", "a Comfortable feeling to it",
                        "Rough-Spun Simplicity", "Spartan Austerity", "Circular Stairs", "Ladders everywhere", "Secret Doors", "Catwalks",
                        "Skylights", "a Balcony", "a Cellar", "a Drafty feeling to it", "a Cold feeling to it", "a Stout feeling to it",
                        "a Quiet feeling to it", "a Cozy feeling to it", "a Warm feeling to it", "that is Vaulted", "that is Spacious",
                        "that is Low", "that is Cramped", "Rickety", "Ramshackle", "Strange Devices", "Weird Artifacts", "Spirit Wards",
                        "Old Runes", "Piled Jumble of Curios", "Antique Appointments", "Shrine", "Altar"]
        items = ["a Chalkboard", "Desks", "Papers", "Maps", "Charts", "Diagrams", "Books", "Scrolls", "Bookcases", "a Lamp", "an Inkwell",
                 "a Writing Desk", "a Clock", "a Cabinet", "Shelves", "a Table", "Chairs", "Notebooks", "a Bed", "a Bureau", "a Vanity", "Bunks",
                 "Stools", "Trunks", "a Basin", "a Pitcher", "a Mirror", "a Sofa", "a Divan", "a Music Box", "Couches", "a Table Lamp", "Drapery",
                 "Pillows", "Cushions", "a Counter", "a Sink", "Cabinets", "a Cookfire", "Pots", "Pans", "Utensils", "a Dining Table", "Chairs",
                 "Cutlery", "a Game Board", "Cards", "Dice", "a Larder", "Spices", "Meat Hooks", "Wine", "Beer", "Whiskey", "a Pedestal", "a Statue",
                 "Paintings", "a Bird Cage", "a Quill", "a Diary", "a Bell", "a Book", "a Candle", "a Fireplace", "a Rug", "an Armchair",
                 "Curtains", "Vases", "Flowers", "Instruments", "Music Sheets", "an Exam Chair", "Medical Tools", "a Burner", "Vials", "Beakers",
                 "a Workbench", "Tools", "Rags", "Weapons", "Ammunition"]
        phrase = ""
        picked_items = []
        x = 0
        if random.choice(range(1, 6)) == 1:
            while x < 4:
                pick = random.choice(items).lower()
                if pick not in picked_items:
                    picked_items.append(pick)
                    x += 1
            phrase = "It's a **" + random.choice(use_rare).lower() + "** made of **" + random.choice(material).lower() + "** and **" + \
                     random.choice(details).lower() + "**, and **" + random.choice(more_details).lower() + "**. Inside you see **" + \
                     picked_items[0] + "**, **" + picked_items[1] + "**, **" + picked_items[2] + "** and **" + \
                     picked_items[3] + "**."
        else:
            while x < 4:
                pick = random.choice(items).lower()
                if pick not in picked_items:
                    picked_items.append(pick)
                    x += 1
            phrase = "It's a **" + random.choice(use_com).lower() + "** made of **" + random.choice(material).lower() + "** and **" + \
                     random.choice(details).lower() + "**, and **" + random.choice(more_details).lower() + "**. Inside you see **" + \
                     picked_items[0] + "**, **" + picked_items[1] + "**, **" + picked_items[2] + "** and **" + \
                     picked_items[3] + "**."

        embed = discord.Embed(colour=discord.Colour.dark_red())
        embed.set_author(name='Generating random ' + opt)
        embed.add_field(name="Characteristics", value=phrase, inline=False)
        await ctx.send(embed=embed)


@bot.command(name="info", aliases=["i"])
async def info(ctx):
    embed = discord.Embed(colour=discord.Colour.darker_grey())
    embed.set_author(name='Bots in the Dark Info')
    embed.add_field(name='=info or =i', value='This is the Bots in the Dark Discord bot created by Fernando Gomes to be used for Blades in the'
                                              ' Dark RPG system. With it you can make Blades rolls, resistance rolls, generate random streets,'
                                              ' buildings, demons, ghosts, scores, bargains, etc.'
                                              ' It can also make generic dice rolls for other purposes.',
                    inline=False)
    await ctx.send(embed=embed)


@bot.command(name="blade", help="Rolls blades dices (d6) for user.", aliases=["b"])
async def blade(ctx, number):
    consequence = ""
    if number.lower() == ("f" or "fortune"):
        pass
    elif number.lower()[0] == "r":
        num_dices = int(number.lower().split('r')[1])
        if num_dices > 0:
            result = []
            for x in range(1, (num_dices + 1)):
                rolled = random.choice(range(1, 7))
                result.append(rolled)
            results = 6 - max(result)
            num_succ = result.count(6)
            if num_succ > 1:
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.set_author(name='Resistance ' + str(num_dices) + ' dice roll')
                embed.add_field(name="CRITICAL RESISTANCE:", value="You recover 1 stress!", inline=False)
                embed.add_field(name="What happens?", value='You resist a consequence and recover stress.', inline=False)
                embed.add_field(name="Your roll:", value=str(result) + '.',
                                inline=False)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.set_author(name='Resistance ' + str(num_dices) + ' dice roll')
                embed.add_field(name="Stress taken:", value=str(results), inline=False)
                embed.add_field(name="What happens?", value='You resist a consequence and suffer **%i stress**.' % (results), inline=False)
                embed.add_field(name="Your roll:", value=str(result) + '.',
                                inline=False)
                await ctx.send(embed=embed)

        elif num_dices == 0:
            result = []
            for x in range(1, 3):
                rolled = random.choice(range(1, 7))
                result.append(rolled)
            results = 6 - min(result)
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_author(name='Resistance ' + str(num_dices) + ' dice roll')
            embed.add_field(name="Stress taken:", value=str(results), inline=False)
            embed.add_field(name="What happens?", value='You resist a consequence and suffer %i stress.' % (results), inline=False)
            embed.add_field(name="Your roll:", value=str(result) + '.',
                            inline=False)
            await ctx.send(embed=embed)

    elif number:
        num_dices = int(number)
        if num_dices > 0:
            result = []

            for x in range(1, (num_dices + 1)):
                rolled = random.choice(range(1, 7))
                result.append(rolled)
            results = max(result)
            num_succ = result.count(6)
            if num_succ > 1:
                results = "++ CRITICAL SUCCESS! ++"
                consequence = "You do the thing with improved effect! Great job!."
            elif num_succ == 1:
                results = "Full Success!"
                consequence = "You do the thing with no consequences."
            else:
                num_fives = result.count(5)
                if num_fives > 0:
                    results = "Partial Success!"
                    consequence = "You do the thing but suffer a consequence."
                else:
                    num_fours = result.count(4)
                    if num_fours > 0:
                        results = "Partial Success!"
                        consequence = "You do the thing but suffer a consequence."
                    else:
                        results = "Failure!"
                        consequence = "You fail at doing the thing and suffer a consequence."

            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_author(name=str(number) + ' Dice Roll')
            embed.add_field(name="Result:", value=str(results), inline=False)
            embed.add_field(name="What happens?", value=str(consequence), inline=False)
            embed.add_field(name="Your roll:", value=str(result) + '.',
                            inline=False)
            await ctx.send(embed=embed)
        elif num_dices == 0:
            result = []
            for x in range(1, 3):
                rolled = random.choice(range(1, 7))
                result.append(rolled)
            results = ""
            resu = min(result)
            print(result)
            print(results)
            if resu == 6:
                results = "Full Success!"
                consequence = "You do the thing with no consequences."
            elif resu == 4 or resu == 5:
                results = "Partial Success!"
                consequence = "You do the thing but suffer a consequence."
            elif resu < 4:
                results = "Failure!"
                consequence = "You fail at doing the thing and suffer a consequence."

            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.set_author(name=str(number) + ' Dice Roll')
            embed.add_field(name="Result:", value="**" + str(results) + "**", inline=False)
            embed.add_field(name="What happens?", value=str(consequence), inline=False)
            embed.add_field(name="Your roll:", value=str(result) + '.',
                            inline=False)

            await ctx.send(embed=embed)


@bot.command(name="roll", help="Rolls dices for user.", aliases=["r"])
async def roll(ctx, dice):
    split = dice.split('d')
    num_dices = int(split[0])
    split = split[1].split('+')
    dice_sides = int(split[0])
    bonus = 0
    if len(split) > 1:
        bonus = int(split[1])
    result = []
    for x in range(1, (num_dices + 1)):
        rolled = random.choice(range(1, (dice_sides + 1)))

        result.append(rolled)

    results = sum(result) + bonus

    embed = discord.Embed(colour=discord.Colour.dark_red())
    embed.set_author(name='ROLLING')
    if bonus > 0:
        embed.add_field(name="You rolled:", value=str(result) + " + " + str(bonus) + '.',
                        inline=False)
        embed.add_field(name="Total:", value=str(results), inline=False)
        await ctx.send(embed=embed)
    else:
        embed.add_field(name="You rolled:", value=str(result) + '.',
                        inline=False)
        embed.add_field(name="Total:", value=str(results), inline=False)
        await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=["h"])
async def help(ctx, *command_helper):
    if len(command_helper) == 0:
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='HELP')
        embed.add_field(name='=help or =h', value='Shows this message. Type in `=help command` or `=h command` for help on that command.',
                        inline=False)
        embed.add_field(name='\nBots in the Dark', value='**Commands:**\n', inline=False)
        embed.add_field(name='=blade or =b', value='Makes a Blades in the Dark dice roll.', inline=False)
        embed.add_field(name='=generate or =g', value="Generates a random thing in the fiction.", inline=False)
        embed.add_field(name='=roll or =r', value="Makes a generic dice roll.", inline=False)
        embed.add_field(name='=info or =i', value="Displays general information on this bot.", inline=False)
        embed.add_field(name='Observations:', value='If a command require a special character like "--" or "-",'
                                                    'you have to provide them. Command arguments are separated by single spaces.', inline=False)
        await ctx.send(embed=embed)

    elif command_helper[0].lower() == "blade" or command_helper[0].lower() == "b":
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='HELP')
        embed.add_field(name='=blade or =b', value='''\nUsage: `=b <argument>`\n
                                                ''', inline=False)
        embed.add_field(name='<argument>', value='''\nNumber (#) of dice to roll. Type r# to make a resistance roll.''',
                        inline=False)
        embed.add_field(name='Examples:', value='''`=blade 4`
                                                    Rolls 4 dice and keep the highest result. The system looks for crits.
                                                    `=b 0`
                                                    Rolls 2 dice and keep the lowest result.
                                                    `=b r3`
                                                    Rolls 3 dice and keep the highest as a resistance roll and calculate the amount of stress taken.
                                                    `=b r0`
                                                    Rolls 2 dice and keep the lowest as a resistance roll and calculate the amount of stress taken.'''
                        , inline=True)
        await ctx.send(embed=embed)

    elif command_helper[0].lower() == "generate" or command_helper[0].lower() == "g":
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='HELP')
        embed.add_field(name='=generate or =g', value='''\nUsage: `=g <argument>`\n
                                                ''', inline=False)
        embed.add_field(name='<argument>', value='\nValid arguments are: street, building, people, demon, ghost, horror, fgod, score, bargain.',
                        inline=False)
        embed.add_field(name='Examples:', value='''`=generate street`
                                                    Generates a random street with several description details.
                                                    `=g people`
                                                    Generates a random person with several details, including name, alias, demonic traits, etc.
                                                    `=g bargain`
                                                    Offers a random Devil's Bargain.
                                                    `=generate score`
                                                    Generates a random score opportunity with several details about it.
                                                    
                                                    If you don't like one thing about the generated thing, generate another and go with a mix of both.
                                                    '''
                        , inline=True)
        await ctx.send(embed=embed)

    elif command_helper[0].lower() == "roll" or command_helper[0].lower() == "r":
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='HELP')
        embed.add_field(name='=roll or =r', value='''\nUsage: `=r <argument>`\n
                                                ''', inline=False)
        embed.add_field(name='<argument>', value='\nxdy+z.'
                                                 'This will roll x dice with y sides and add z to the sum of the roll.',
                        inline=False)
        embed.add_field(name='Examples:', value='''`=r 1d20+4`
                                                    Rolls 1 d20 dice and add 4 to the result.
                                                    `=r 4d6`
                                                    Rolls 4 d6 dice and sum up the results.
                                                    `=r 2d8+5`
                                                    Rolls 2 d8 dice and add 5 to the sum of the results.'''
                        , inline=True)
        await ctx.send(embed=embed)

    elif command_helper[0].lower() == "info" or command_helper[0].lower() == "i":
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='HELP')
        embed.add_field(name='=info or =i', value='Displays information regarding this bot.',
                        inline=False)
        await ctx.send(embed=embed)

    else:
        pass


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='ERROR')
        embed.add_field(name="Syntax error",
                        value='**Missing Argument.**  :x:\n"' + ctx.message.content + '"', inline=False)
        await ctx.send(embed=embed)
    if isinstance(error, discord.InvalidArgument):
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='ERROR')
        embed.add_field(name="Syntax error",
                        value='**Invalid argument or argument type.**  :x:\n"' + ctx.message.content + '"',
                        inline=False)
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        embed.set_author(name='ERROR')
        embed.add_field(name="Syntax error",
                        value='**Invalid command.**  :x:\n"' + ctx.message.content + '"',
                        inline=False)
        await ctx.send(embed=embed)


bot.run(token)
