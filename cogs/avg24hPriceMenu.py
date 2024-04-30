import requests
import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands



class Questions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Avg24hPrice cog loaded")

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(fmt)} commands')

    '''
    # name 'e il nome del comando, gli argomenti oltre name e description gli argomenti necessari messi da utente
    @app_commands.command(name="questions", description="questions form")  # lo / command effettivo
    async def questions(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message('answered')
    '''

    @app_commands.command(name="fleaprice", description="Average Flea Price")  # lo / command effettivo
    async def fleaprice(self, interaction: discord.Interaction, item: str):

        encoded_item = item.encode('utf-8').decode('utf-8')
        query = f"""
                    {{
                        items(name: "{encoded_item}") {{
                            id
                            name
                            shortName
                            avg24hPrice
                            low24hPrice
                            lastLowPrice
                        }}
                    }}
                    """

        headers = {"Content-Type": "application/json"}
        response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
        print(response.json())
        oggettiTrovati = response.json()['data']['items']
        risposta = ""
        if len(oggettiTrovati) > 10:
            risposta += "Coglione sii piú preciso non sono Bettina"
            embed = discord.Embed(description=risposta)
            await interaction.response.send_message(embed=embed)
            return
        if len(oggettiTrovati) == 0:
            risposta += "Non ho trovato un cazzo, git gud"
            embed = discord.Embed(description=risposta)
            await interaction.response.send_message(embed=embed)
            return
        for oggetto in oggettiTrovati:
            if int(oggetto["avg24hPrice"]) > 0:
                informazioni = f"""
                        Nome: {oggetto['name']}
                        Short Name: {oggetto['shortName']}
                        Prezzo Medio: {str('{:,}'.format(oggetto['avg24hPrice']).replace(',', '.'))} rubli
                        Piu Basso 24h: {str('{:,}'.format(oggetto['low24hPrice']).replace(',', '.'))} rubli
                        Ultimo Piu Basso: {str('{:,}'.format(oggetto['lastLowPrice']).replace(',', '.'))} rubli
                        \n
                        """
                risposta += informazioni

        print(risposta)
        embed = discord.Embed(description=risposta)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="map", description="Returns selected Map")  # lo / command effettivo
    @app_commands.choices(mappe=[
        Choice(name='Factory', value=0),
        Choice(name='Woods', value=1),
        Choice(name='Customs', value=2),
        Choice(name='Interchange', value=3),
        Choice(name='Reserve', value=4),
        Choice(name='Shoreline', value=5),
        Choice(name='The Lab', value=6),
        Choice(name='Lighthouse', value=7),
        Choice(name='Streets', value=8),
        Choice(name='Ground Zero', value=9)
    ])
    async def map(self, interaction: discord.Interaction, mappe: Choice[int]):

        if mappe.name == 'Factory':
            try:
                file = discord.File("maps/FactoryMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net"
                                                  "/escapefromtarkov_gamepedia/images/9/94/Factory_loot.png"
                                                  "/revision/latest?cb=20230804012739")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Woods':
            try:
                file = discord.File("maps/WoodsMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/0/05/Glory4lyfeWoods_map_v4_marked.png/revision/latest?cb"
                                                  "=20240417104814")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Customs':
            try:
                file = discord.File("maps/CustomsMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/5/55/CustomsLargeExpansionGloryMonki.png/revision/latest"
                                                  "?cb=20240211130541")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Interchange':
            try:
                file = discord.File("maps/InterchangeMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/2/27/Interchange2DMapLorathor.jpg/revision/latest?cb"
                                                  "=20220409224052")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Reserve':
            try:
                file = discord.File("maps/ReserveMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/7/7c/JindouzReserve_v1_2dmap.png/revision/latest?cb"
                                                  "=20240416184931")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Shoreline':
            try:
                file = discord.File("maps/ShorelineMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/1/17/Shoreline2DMapByMonkiUpdatedByJindouz.png/revision"
                                                  "/latest?cb=20240121170426")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'The Lab':
            try:
                file = discord.File("maps/LabMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/9/9e/LabsMapByMonkimonkimonk.png/revision/latest?cb"
                                                  "=20230327101655")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Lighthouse':
            try:
                file = discord.File("maps/LighthouseMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/1/13/Jindouz_Lighthouse_Map_V1.png/revision/latest?cb"
                                                  "=20230914172056")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Streets':
            try:
                file = discord.File("maps/StreetsMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/7/71/StreetsOfTarkov2DMapByJindouz.png/revision/latest?cb"
                                                  "=20240417104158")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)
        if mappe.name == 'Ground Zero':
            try:
                file = discord.File("maps/GroundZeroMap.png", filename="image.png")
                embed = discord.Embed(description="Link: https://static.wikia.nocookie.net/escapefromtarkov_gamepedia"
                                                  "/images/4/44/GroundZero3DMapByRe3mr.png/revision/latest?cb"
                                                  "=20240319113910")
                embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=embed)
            except Exception as e:
                print("Errore durante l'invio della foto:", e)

        return

    @app_commands.command(name="task", description="Find a Task")  # lo / command effettivo
    async def task(self, interaction: discord.Interaction, name: str):

        encoded_name = name.encode('utf-8').decode('utf-8')
        query = f"""
                        {{
                            tasks{{
                                name
                                wikiLink
                                objectives{{
                                    description
                                    maps{{
                                        name
                                    }}
                                }}
                            }}
                        }}
                        """

        headers = {"Content-Type": "application/json"}
        response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
        print(response.json())
        oggettiTrovati = {}
        oggettiTrovatiNonFiltrati = response.json()['data']['tasks']
        for oggettoDiMerda in oggettiTrovatiNonFiltrati:
            if encoded_name.lower() in oggettoDiMerda['name'].lower():
                oggettiTrovati[oggettoDiMerda['name']] = oggettoDiMerda
            '''
            pattern = re.compile(r'\b{}\b'.format(re.escape(name)), re.IGNORECASE)
            corrispondenze = pattern.findall(oggettoDiMerda['name'])
            if len(corrispondenze) > 0:
                oggettiTrovati[oggettoDiMerda['name']] = corrispondenze[0]
            '''
        risposta = ""
        counter = 0
        for oggetto in oggettiTrovati.values():
            informazioni = f"""
                        Task: {oggetto['name']}
                        Link Wiki: {oggetto['wikiLink']}
                        """
            for obiettivi in oggetto['objectives']:
                counter += 1
                informazioni += f"obiettivo {counter}: {obiettivi['description']}\n"
                for mappe in obiettivi['maps']:
                    informazioni += f"Mappe: {mappe['name']}\n"
            informazioni += '\n'
            risposta += informazioni
            counter = 0
        print(risposta)
        embed = discord.Embed(description=risposta)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(Questions(bot), guilds=[discord.Object(id=831990672713056307)])
